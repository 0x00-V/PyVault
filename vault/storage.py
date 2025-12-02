import sqlite3
import sys
from .models import *


conn = None
cur = None
try:
    conn = sqlite3.connect("./data/storage.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    type TEXT NOT NULL,
    is_completed INTEGER,
    due_date TEXT,
    priority TEXT,
    url TEXT
    )
    """)
    conn.commit()
except sqlite3.OperationalError as e:
    sys.exit(e)


def recordToEntry(row):
    if row["type"] == "note":
        return NoteEntry(
            id=row["id"],
            title=row["title"],
            content=row["content"],
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )
    elif row["type"] == "task":
        return TaskEntry(
            id=row["id"],
            title=row["title"],
            content=row["content"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            is_completed=row["is_completed"],
            due_date=row["due_date"],
            priority=row["priority"]
        )
    elif row["type"] == "bookmark":
        return BookmarkEntry(
            id=row["id"],
            title=row["title"],
            content=row["content"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            url=row["url"]
        )
    else:
        pass


def recordToDatabase(entry):
    try:
        if entry.type == "note":
            cur.execute("""INSERT INTO entries (title, content, created_at, updated_at, type) VALUES (?, ?, ?, ?, ?)""", (entry.title, entry.content, entry.created_at, entry.updated_at, entry.type))
            conn.commit()
            entry.id = cur.lastrowid
        elif entry.type == "task":
            cur.execute("""INSERT INTO entries (title, content, created_at, updated_at, type, is_completed, due_date, priority) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (entry.title, entry.content, entry.created_at, entry.updated_at, entry.type , entry.is_completed, entry.due_date, entry.priority))
            conn.commit()
            entry.id = cur.lastrowid
        elif entry.type == "bookmark":
            cur.execute("""INSERT INTO entries (title, content, created_at, updated_at, type, url) VALUES (?, ?, ?, ?, ?, ?)""", (entry.title, entry.content, entry.created_at, entry.updated_at, entry.type , entry.url))
            conn.commit()
            entry.id = cur.lastrowid
        else:
            pass
    except sqlite3.OperationalError as e:
        sys.exit(e)

def deleteEntry(entry_id):
    try:
        cur.execute("""DELETE FROM entries WHERE id = ?""", (entry_id,))
        conn.commit()
    except sqlite3.OperationalError as e:
        sys.exit(e)

def editEntry(entry, new_title, new_content, new_updated_at, new_due_date, new_priority, new_url):
    try:
        if entry.type == "note":
            cur.execute("""UPDATE entries SET title = ?, content = ?, updated_at = ? WHERE id = ?""", (new_title, new_content, new_updated_at, entry.id))
            conn.commit()
        elif entry.type == "task":
            cur.execute("""UPDATE entries SET title = ?, content = ?, updated_at = ?, due_date = ?, priority = ? WHERE id = ?""", (new_title, new_content, new_updated_at, new_due_date, new_priority, entry.id))
            conn.commit()
        elif entry.type == "bookmark":
            cur.execute("""UPDATE entries SET title = ?, content = ?, updated_at = ?, url = ? WHERE id = ?""", (new_title, new_content, new_updated_at, new_url, entry.id))
            conn.commit()
        else:
            pass
    except sqlite3.OperationalError as e:
        sys.exit(e)        




def readDatabase():
    try:
        cur.execute("SELECT * FROM entries")
        rows = cur.fetchall()
        entries = []
        for row in rows:
            entry = recordToEntry(row)
            entries.append(entry)
        return entries
    except sqlite3.OperationalError as e:
        sys.exit(e)