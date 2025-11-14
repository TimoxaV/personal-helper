from datetime import datetime

class Note:
    def __init__(self, title, text, tags=None, created_at=None):
        self.title = title
        self.text = text
        self.tags = tags or []
        self.created_at = datetime.now()

    def __str__(self):
        tag_str = ", ".join(self.tags) if len(self.tags) > 0 else "No tags"
        return f"[{self.title}] ({tag_str}) — {self.text}"

    def __repr__(self):
        return f"Note({self.__str__()})"

    def to_dict(self):
        return {
            "title": self.title,
            "text": self.text,
            "tags": self.tags,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def from_dict(data):
        return Note(
            title=data["title"],
            text=data["text"],
            tags=data.get("tags", []),
            created_at=datetime.strptime(
                data["created_at"], "%Y-%m-%d %H:%M:%S"
            )
        )
