class BaseModel:
    def __init__(self, id, title, content, tags, created_at, updated_at):
        self.id = id
        self.title = title
        self.content = content
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at
    
class NoteEntry(BaseModel):
    pass

class TaskEntry(BaseModel):
    def __init__(self, id, title, content, tags, created_at, updated_at, is_completed, due_date, priority):
        BaseModel.__init__(self, id, title, content, tags, created_at, updated_at)
        self.is_completed = is_completed
        self.due_date = due_date
        self.priority = priority

class BookmarkEntry(BaseModel):
    def __init__(self, id, title, content, tags, created_at, updated_at, url, source):
        BaseModel.__init__(self, id, title, content, tags, created_at, updated_at)
        self.url = url
        self.source = source

