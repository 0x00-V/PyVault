import sys
from datetime import datetime
from .storage import *
from .models import *

class Manager:
    def __init__(self):
        self.entries = readDatabase()

    def list_entries(self):
        return self.entries
    
    def add_note(self, title, content):
        note = NoteEntry(
            id = None,
            title = title,
            content = content,
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        self.entries.append(note)
        recordToDatabase(note)

    def add_task(self, title, content, is_completed, due_date, priority):
        task = TaskEntry(
            id = None,
            title = title,
            content = content,
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            is_completed = is_completed,
            due_date = due_date, 
            priority = priority
        )
        self.entries.append(task)
        recordToDatabase(task)
    
    def add_bookmark(self, title, content, url, source):
        bookmark = BookmarkEntry(
            id = None,
            title = title,
            content = content,
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            url = url, 
            source = source
        )
        self.entries.append(bookmark)
        recordToDatabase(bookmark)

    def get_entry_by_id(self, id):
        for entry in self.entries:
            if entry.id == id:
                return entry