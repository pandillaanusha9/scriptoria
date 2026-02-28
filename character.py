import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

def generate_characters(screenplay):

    prompt = f"""
    Extract all characters from this screenplay.

    For each character provide:
    - Name
    - Age
    - Personality
    - Backstory
    - Motivation
    - Emotional arc

    Screenplay:
    {screenplay}
    """

    response = model.generate_content(prompt)
    return response.text