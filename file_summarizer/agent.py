from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import os

def read_file(file_path: str) -> str:
    """
    Reads a file and returns its content.
    
    Args:
        file_path: The path to the file to read
    Returns:
        The content of the file as a string
    """
    file_path = file_path.strip().strip('"').strip("'")
    
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error: {str(e)}"


root_agent = Agent(
    name="file_summarizer",
    model="gemini-2.0-flash",
    description="Reads files and summarizes them",
    instruction="""
        You are a file summarizer agent.
        When given a file path:
        1. Use read_file tool to read it
        2. Give a 2-3 sentence summary
        3. List 5 key points as bullets
    """,
    tools=[FunctionTool(read_file)]
)
