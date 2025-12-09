# notes.py
import flet as ft
from db import insert_note, update_note, delete_note, load_notes


def create_note_card(note_id: int, text: str, notes_list: ft.Column, page: ft.Page):
    note_text_ref = ft.Ref[ft.Text]()
    card_ref = ft.Ref[ft.Container]()

    def delete_note_action(e):
        delete_note(note_id)
        notes_list.controls.remove(card_ref.current)
        page.update()

    def edit_note_action(e):
        edit_field = ft.TextField(
            value=note_text_ref.current.value,
            multiline=True,
            min_lines=2,
            max_lines=6,
            expand=True
        )

        def save_edit(ev):
            new_text = edit_field.value.strip()
            if new_text == "":
                return
            update_note(note_id, new_text)
            note_text_ref.current.value = new_text
            card_ref.current.update()
            dialog.open = False
            page.update()

        def cancel(ev):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Edit Note"),
            content=edit_field,
            actions=[
                ft.TextButton("Cancel", on_click=cancel),
                ft.ElevatedButton("Save", on_click=save_edit),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

    card = ft.Container(
        ref=card_ref,
        bgcolor=ft.Colors.YELLOW_200,
        border_radius=8,
        padding=15,
        width=300,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=6,
            color=ft.Colors.AMBER_300,
            offset=ft.Offset(1, 2),
        ),
        content=ft.Column(
            [
                ft.Text(ref=note_text_ref, value=text, selectable=True),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.EDIT, tooltip="Edit", on_click=edit_note_action),
                        ft.IconButton(icon=ft.Icons.DELETE, tooltip="Delete", on_click=delete_note_action),
                    ],
                    alignment="end",
                ),
            ]
        )
    )

    return card


def build_notes_page(page: ft.Page):
    page.title = "Sticky Notes App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.GREY_50
    page.padding = 20
    page.vertical_alignment = "start"

    notes_list = ft.Column(scroll="auto", spacing=15, expand=True)

    # PRELOAD NOTES
    for note_id, content in load_notes():
        notes_list.controls.append(create_note_card(note_id, content, notes_list, page))

    note_input = ft.TextField(
        label="Write a note...",
        multiline=True,
        min_lines=2,
        max_lines=4,
        expand=True,
    )

    def add_note_action(e):
        text = note_input.value.strip()
        if not text:
            return

        new_id = insert_note(text)
        notes_list.controls.insert(0, create_note_card(new_id, text, notes_list, page))
        note_input.value = ""
        page.update()

    add_button = ft.ElevatedButton("Add Note", icon=ft.Icons.ADD, on_click=add_note_action)

    return ft.Column(
        [
            ft.Text("Sticky Notes", size=32, weight="bold"),
            ft.Row([note_input, add_button], alignment="start"),
            ft.Divider(),
            notes_list,
        ],
        expand=True
    )
