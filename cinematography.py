import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

def generate_cinematography(screenplay):

    prompt = f"""
    For each scene suggest:
    - Camera angle
    - Shot type
    - Lighting style
    - Color tone

    Screenplay:
    {screenplay}
    """

    response = model.generate_content(prompt)
    return response.text