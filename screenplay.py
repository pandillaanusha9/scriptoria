from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create client (NEW WAY)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_screenplay(title, genre, idea):

    prompt = f"""
    You are a professional screenwriter.

    Create a structured screenplay.

    Title: {title}
    Genre: {genre}
    Idea: {idea}

    Include:
    - Logline
    - Three Act Structure
    - Scene breakdown
    - Dialogues formatted properly
    """

    # Generate content using new SDK format
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text