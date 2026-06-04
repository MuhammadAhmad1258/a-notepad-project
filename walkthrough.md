# Notepad App Backend Walkthrough

We have successfully created the backend for the Notepad App using the **Google Agent Development Kit (ADK)** and **FastAPI**. The server is currently running in the background.

## Created Files

All backend files are stored under `notepad_app/backend/`:
* [__init__.py](file:///c:/Users/SL%20LAPTOP/.antigravity/notepad_app/backend/agent/__init__.py): Initializes the `agent` module.
* [tools.py](file:///c:/Users/SL%20LAPTOP/.antigravity/notepad_app/backend/agent/tools.py): Contains the logic to save notes and tasks in a `data/` subdirectory.
* [agent.py](file:///c:/Users/SL%20LAPTOP/.antigravity/notepad_app/backend/agent/agent.py): Defines the Google ADK `Agent` with tools and instructions to process notes.
* [main.py](file:///c:/Users/SL%20LAPTOP/.antigravity/notepad_app/backend/main.py): Sets up the FastAPI endpoints and integrates the ADK agent runner.
* [.env](file:///c:/Users/SL%20LAPTOP/.antigravity/notepad_app/backend/.env): Holds the `GEMINI_API_KEY` configuration.

---

## How to Test the Setup

The FastAPI server is running in the background on your system at **`http://127.0.0.1:8000`**.

Follow these steps to test it:

### Step 1: Set your Gemini API Key
Open [notepad_app/backend/.env](file:///c:/Users/SL%20LAPTOP/.antigravity/notepad_app/backend/.env) and insert your Gemini API Key:
```env
GEMINI_API_KEY=AIzaSy...
```
*(Save the file after editing. The server will automatically reload and pick up the new key).*

### Step 2: Send a Note to the Agent
To test the task extractor, send a POST request with a note title and body containing actionable items.

In **PowerShell**, you can run:
```powershell
$body = @{
    title = "Weekly Tasks"
    content = "I need to fix the login bug tomorrow, write unit tests for the signup flow by Wednesday, and review the project documentation."
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/notes" -Method Post -Body $body -ContentType "application/json"
```

### Step 3: Check Saved Notes and Tasks
Verify the JSON files are created or check the API endpoints directly:

* **Get all saved notes**: Open [http://127.0.0.1:8000/notes](http://127.0.0.1:8000/notes) in your browser.
* **Get all extracted tasks**: Open [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks) in your browser.
