from services.screenplay import generate_screenplay
from services.character import generate_characters
from services.sound import generate_sound_design
from services.cinematography import generate_cinematography
from services.budget import estimate_budget
from services.storyboard import generate_storyboard

def generate_full_plan(title, genre, idea):

    screenplay = generate_screenplay(title, genre, idea)

    characters = generate_characters(screenplay)

    sound = generate_sound_design(screenplay)

    cinematography = generate_cinematography(screenplay)

    storyboard = generate_storyboard(screenplay)

    budget = estimate_budget(screenplay)

    return {
        "screenplay": screenplay,
        "characters": characters,
        "sound": sound,
        "cinematography": cinematography,
        "storyboard": storyboard,
        "budget": budget
    }