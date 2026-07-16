def generate_recommendations(user, repos, scores):
    recommendations = []
    if not user.bio:
        recommendations.append("Add a professional GitHub bio mentioning your role and primary technologies.")
    if scores["metrics"]["stars"] <=5:
        recommendations.append("Focus on creating projects that solve real problems and share them publicly.")
    return recommendations