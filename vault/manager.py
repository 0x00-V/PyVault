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
    
    def add_bookmark(self, title, content, url):
        bookmark = BookmarkEntry(
            id = None,
            title = title,
            content = content,
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            url = url
        )
        self.entries.append(bookmark)
        recordToDatabase(bookmark)

    def delete_entry(self, id):
        for entry in self.entries:
            if entry.id == id:
                deleteEntry(id)
                self.entries.remove(entry)
                return "Entry Deleted."
        return "Not Found."
    
    def edit_entry(self, id, new_title="", new_content="", new_due_date="", new_priority="", new_url=""):
        for entry in self.entries:
            if entry.id == id:
                new_updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if entry.type == "note":
                    if new_title == "":
                        new_title = entry.title
                    if new_content == "":
                        new_content = entry.content                    
                    editEntry(entry, new_title, new_content, new_updated_at, new_due_date, new_priority, new_url)
                    entry.title = new_title
                    entry.content = new_content
                    entry.updated_at = new_updated_at
                elif entry.type == "task":
                    if new_title == "":
                        new_title = entry.title
                    if new_content == "":
                        new_content = entry.content
                    if new_due_date == "":
                        new_due_date = entry.due_date
                    if new_priority == "":
                        new_priority = entry.priority
                    editEntry(entry, new_title, new_content, new_updated_at, new_due_date, new_priority, new_url)
                    entry.title = new_title
                    entry.content = new_content
                    entry.updated_at = new_updated_at
                    entry.due_date = new_due_date
                    entry.priority = new_priority
                elif entry.type == "bookmark":
                    if new_title == "":
                        new_title = entry.title
                    if new_content == "":
                        new_content = entry.content
                    if new_url == "":
                        new_url = entry.url
                    editEntry(entry, new_title, new_content, new_updated_at, new_due_date, new_priority, new_url)
                    entry.title = new_title
                    entry.content = new_content
                    entry.updated_at = new_updated_at
                    entry.url = new_url
                else:
                    pass
                return "Entry updated."
        return "Entry not found."
        
                
                

    def get_entry_by_id(self, id):
        for entry in self.entries:
            if entry.id == id:
                return entry
    
    def get_entries_by_category(self, category):
        entries_by_cat = []
        for entry in self.entries:
            if entry.type == category:
                entries_by_cat.append(entry)
        return entries_by_cat
                
