import json
import os
from model.note import Note
from exception.exceptions import input_error, NoteNotFound


class NoteBook:
    def __init__(self):
        self.__notes = {}

    # ----------------------------
    # CRUD
    # ----------------------------
    @input_error
    def add_note(self, title, text, tags=None):
        if title in self.__notes:
            return f"Note '{title}' already exists."
        note = Note(title, text, tags)
        self.__notes[title] = note
        return f"Note '{title}' successfully added."

    @input_error
    def edit_note(self, title, new_text=None, new_tags=None):
        if title not in self.__notes:
            raise NoteNotFound(f"Note '{title}' not found.")
        note = self.__notes[title]
        if new_text:
            note.text = new_text
        if new_tags is not None:
            note.tags = new_tags
        return f"Note '{title}' updated."

    @input_error
    def delete_note(self, title):
        if title not in self.__notes:
            raise NoteNotFound(f"Note '{title}' not found.")
        del self.__notes[title]
        return f"Note '{title}' deleted."

    def get_all_notes(self):
        return list(self.__notes.values())

    # ----------------------------
    # Робота з тегами
    # ----------------------------
    @input_error
    def add_tag(self, title, tag):
        if title not in self.__notes:
            raise NoteNotFound(f"Note '{title}' not found.")
        note = self.__notes[title]
        if tag not in note.tags:
            note.tags.append(tag)
        return f"Tag '{tag}' added to note '{title}'."

    @input_error
    def remove_tag(self, title, tag):
        if title not in self.__notes:
            raise NoteNotFound(f"Note '{title}' not found.")
        note = self.__notes[title]
        if tag in note.tags:
            note.tags.remove(tag)
            return f"Tag '{tag}' removed from note '{title}'."
        return f"Tag '{tag}' not found in note '{title}'."

    # ----------------------------
    # Пошук і сортування
    # ----------------------------
    def search_notes(self, keyword):
        results = []
        keyword = keyword.lower()
        for note in self.__notes.values():
            if (keyword in note.title.lower() or
                keyword in note.text.lower() or
                any(keyword in tag.lower() for tag in note.tags)):
                results.append(note)
        return results

    def sort_by_tag(self, tag):
        tagged = [note for note in self.__notes.values() if tag in note.tags]
        not_tagged = [note for note in self.__notes.values() if tag not in note.tags]
        return tagged + not_tagged

    # ----------------------------
    # Збереження / завантаження
    # ----------------------------
    def save(self, filepath="data/notes.json"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    title: {
                        "text": n.text,
                        "tags": n.tags,
                        "created_at": n.created_at.isoformat()
                    } for title, n in self.__notes.items()
                },
                f,
                indent=4,
                ensure_ascii=False
            )

    def load(self, filepath="data/notes.json"):
        if not os.path.exists(filepath):
            return
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            for title, note_data in data.items():
                note = Note(
                    title=title,
                    text=note_data["text"],
                    tags=note_data.get("tags", [])
                )
                self.__notes[title] = note
