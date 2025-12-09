# db.py
import sqlite3

DB_FILE = "notes.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def load_notes():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, content FROM notes ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def insert_note(content):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    inserted_id = cur.lastrowid
    conn.close()
    return inserted_id


def update_note(note_id, content):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE notes SET content=? WHERE id=?", (content, note_id))
    conn.commit()
    conn.close()


def delete_note(note_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
