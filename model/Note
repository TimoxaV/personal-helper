from datetime import datetime

class Note:
    def __init__(self, title, text, tags=None):
        self.title = title
        self.text = text
        self.tags = tags or []
        self.created_at = datetime.now()

    def __str__(self):
        tag_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"[{self.title}] ({tag_str}) — {self.text}"
