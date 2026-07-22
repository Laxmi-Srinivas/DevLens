def calculate_developer_level(score: int) -> str:
    if score <= 20:
        return "Beginner"

    elif score <= 35:
        return "Junior Developer"

    elif score <= 50:
        return "Intermediate Developer"

    elif score <= 65:
        return "Advanced Developer"

    elif score <= 80:
        return "Senior-Level Portfolio"

    elif score <= 90:
        return "Open Source Contributor"

    return "Elite Developer"