import sqlite3
from .models import *


conn = sqlite3.connect("./data/storage.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def recordToEntry(row):
    if row["type"] == "note":
        return NoteEntry(
            id=row["id"],
            title=row["title"],
            content=row["content"],
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )
    else:
        pass # Implement task and bookmark when I get back here

def readDatabase():
    cur.execute("SELECT * FROM entries")
    rows = cur.fetchall()
    entries = []
    for row in rows:
        entry = recordToEntry(row)
        entries.append(entry)
    return entries
        
