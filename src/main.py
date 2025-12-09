# main.py
import flet as ft
from db import init_db
from notes import build_notes_page


def main(page: ft.Page):
    page.add(build_notes_page(page))


if __name__ == "__main__":
    init_db()
    ft.app(target=main)
