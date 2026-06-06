import json
import os
from datetime import datetime

NOTES_DIR = "notes"

def ensure_notes_folder():
    """Ensures that the directory for storing notes exists."""
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def save_note(title: str, content: str) -> str:
    """
    Saves or updates a note with the specified title and content.

    Args:
        title (str): The title of the note.
        content (str): The textual content of the note.

    Returns:
        str: A success message indicating the note was saved.
    """
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
    """
    Reads and retrieves the content of a saved note by its title.

    Args:
        title (str): The title of the note to read.

    Returns:
        str: The content of the note, or an error message if not found.
    """
    ensure_notes_folder()
    filename = title.lower().replace(" ", "_") + ".json"
    filepath = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(filepath):
        return f"No note found with title '{title}'."
    with open(filepath, "r") as f:
        note = json.load(f)
    return note["content"]

def list_notes() -> str:
    """
    Lists all the titles of the saved notes.

    Returns:
        str: A formatted list of saved note titles, or a message indicating no notes exist.
    """
    ensure_notes_folder()
    files = os.listdir(NOTES_DIR)
    if not files:
        return "No notes saved yet."
    titles = [f.replace("_", " ").replace(".json", "") for f in files]
    return "Your saved notes:\n" + "\n".join(f"- {t}" for t in titles)

def delete_note(title: str) -> str:
    """
    Deletes a saved note by its title.

    Args:
        title (str): The title of the note to delete.

    Returns:
        str: A success message, or an error message if the note was not found.
    """
    ensure_notes_folder()
    filename = title.lower().replace(" ", "_") + ".json"
    filepath = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(filepath):
        return f"No note found with title '{title}'."
    os.remove(filepath)
    return f"Note '{title}' deleted successfully."


TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Loads the list of tasks from the JSON file.

    Returns:
        list: A list of tasks.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """
    Saves the list of tasks to the JSON file.

    Args:
        tasks (list): The list of tasks to save.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title: str, due_date: str) -> str:
    """
    Adds a new task with a title and due date.

    Args:
        title (str): The title or description of the task.
        due_date (str): The deadline of the task (e.g., "YYYY-MM-DD" or "today").

    Returns:
        str: A success message indicating the task was added.
    """
    tasks = load_tasks()
    tasks.append({
        "title": title,
        "due_date": due_date,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_tasks(tasks)
    return f"Task '{title}' added with deadline {due_date}."

def list_tasks() -> str:
    """
    Retrieves and lists all tasks, sorted by their due date.

    Returns:
        str: A formatted list of tasks showing their status, title, and deadline.
    """
    tasks = load_tasks()
    if not tasks:
        return "No tasks found."
    sorted_tasks = sorted(tasks, key=lambda x: x["due_date"])
    result = "Your tasks:\n"
    for t in sorted_tasks:
        status_icon = "✓" if t["status"] == "done" else "•"
        result += f"{status_icon} {t['title']} — due {t['due_date']} [{t['status']}]\n"
    return result

def complete_task(title: str) -> str:
    """
    Marks a specific task as complete by its title.

    Args:
        title (str): The title of the task to complete.

    Returns:
        str: A success message, or an error message if the task was not found.
    """
    tasks = load_tasks()
    for t in tasks:
        if t["title"].lower() == title.lower():
            t["status"] = "done"
            save_tasks(tasks)
            return f"Task '{title}' marked as complete."
    return f"No task found with title '{title}'."

def delete_task(title: str) -> str:
    """
    Deletes a specific task from the task list by its title.

    Args:
        title (str): The title of the task to delete.

    Returns:
        str: A success message, or an error message if the task was not found.
    """
    tasks = load_tasks()
    updated = [t for t in tasks if t["title"].lower() != title.lower()]
    if len(updated) == len(tasks):
        return f"No task found with title '{title}'."
    save_tasks(updated)
    return f"Task '{title}' deleted."