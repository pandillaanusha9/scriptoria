def estimate_budget(screenplay):

    base_budget = 50000

    if "outdoor" in screenplay.lower():
        base_budget += 20000

    if "vfx" in screenplay.lower():
        base_budget += 30000

    if screenplay.lower().count("scene") > 10:
        base_budget += 25000

    return f"Estimated Production Budget: ${base_budget}"