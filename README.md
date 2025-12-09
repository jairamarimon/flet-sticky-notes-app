# Flet Sticky Notes App 📝

A simple **sticky notes application** built with **Python + Flet + SQLite**.  
You can add, edit, and delete notes, and all notes are **persistently stored** in a local SQLite database.

---

## Features

- Add new notes
- Edit existing notes
- Delete notes
- Persistent storage using SQLite
- Modern UI with Flet
- Lightweight and cross-platform

---

## Installation

1. Clone the repository via SSH:

   ```bash
   git clone git@github.com:jairamarimon/flet-sticky-notes-app.git
   cd flet-sticky-notes-app
   ```
   
2. Create a Python virtual environment (recommended):

    ```bash
    python -m venv .venv
    ```
    Activate the virtual environment:
    
    macOS/Linux:
    
      ```bash
      source .venv/bin/activate
      ```
    Windows:
    
      ```bash
      .venv\Scripts\activate
      ```
3. Install dependencies:

    ```bash
    pip install flet
    ```
---

## Usage
Run the app:

```bash
flet run
```

- Add a note in the text field and click Add Note.
- Edit a note by clicking the Edit button.
- Delete a note by clicking the Delete button.
- All notes are automatically saved in notes.db.

---
## Project Structure
```bash
notes_app/
│── main.py        # App entry point
│── db.py          # SQLite database functions
│── ui.py          # Flet UI components
│── notes.db       # SQLite database (auto-created)
│── README.md      # This file
```
