import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

def generate_sound_design(screenplay):

    prompt = f"""
    For each scene suggest:
    - Background music
    - Ambient sounds
    - Sound effects
    - Mood tone

    Screenplay:
    {screenplay}
    """

    response = model.generate_content(prompt)
    return response.text