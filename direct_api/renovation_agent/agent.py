from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig

import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def store_markdown(markdown_text: str, file_name: str, directory: str = ".") -> str:
    """
    Saves markdown text to a .md file.

    Args:
        markdown_text (str): The markdown content to save.
        file_name (str): Name of the file to create (e.g., 'plan.md').
        directory (str): Directory to save the file.

    Returns:
        str: Full path to the saved markdown file.
    """
    try:
        os.makedirs(directory, exist_ok=True)
        if not file_name.endswith(".md"):
            file_name += ".md"
        full_path = os.path.join(directory, file_name)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)

        logger.info(f"Markdown saved at {full_path}")
        return full_path

    except Exception as e:
        logger.error(f"Error saving markdown file: {e}")
        raise


root_agent = Agent(
    model="gemini-2.0-flash",
    name="renovation_agent",
    description="An agent that helps with renovation tasks by analyzing text/images and providing suggestions.",
    instruction="""
        You are a renovation assistant that helps users with their renovation tasks by analyzing text/images and providing suggestions. 
        You can answer questions about the images, suggest improvements, and provide general renovation advice. Use the provided images to inform your responses.""",
    tools=[store_markdown],
    generate_content_config=GenerateContentConfig(temperature=0.2),
)
