import json
import os
from datetime import datetime

NOTES_DIR = "notes"

def ensure_notes_folder():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def save_note(title: str, content: str) -> str:
    ensure_notes_folder()
    filename = title.lower().replace(" ", "_") + ".json"
    filepath = os.path.join(NOTES_DIR, filename)
    note = {
        "title": title,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    with open(filepath, "w") as f:
        json.dump(note, f, indent=2)
    return f"Note '{title}' saved successfully."

def read_note(title: str) -> str:
    ensure_notes_folder()
    filename = title.lower().replace(" ", "_") + ".json"
    filepath = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(filepath):
        return f"No note found with title '{title}'."
    with open(filepath, "r") as f:
        note = json.load(f)
    return note["content"]

def list_notes() -> str:
    ensure_notes_folder()
    files = os.listdir(NOTES_DIR)
    if not files:
        return "No notes saved yet."
    titles = [f.replace("_", " ").replace(".json", "") for f in files]
    return "Your saved notes:\n" + "\n".join(f"- {t}" for t in titles)
def delete_note(title: str) -> str:
    '''This function is used to delete the notes from memory'''
    ensure_notes_folder()
    filename = title.lower().replace(" ", "_") + ".json"
    filepath = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(filepath):
        return f"No note found with title '{title}'."
    os.remove(filepath)
    return f"Note '{title}' deleted successfully."