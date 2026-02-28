import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

def generate_storyboard(screenplay):

    prompt = f"""
    Select 3 key scenes from the screenplay and describe each visually 
    in cinematic detail suitable for storyboard generation.

    Screenplay:
    {screenplay}
    """

    response = model.generate_content(prompt)
    return response.text