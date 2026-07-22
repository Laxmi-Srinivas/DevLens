def generate_strengths(scores)->list[str]:
    strengths=[]
    repository_score=scores["metrics"]["repository"]
    language_score=scores["metrics"]["languages"]
    stars_score=scores["metrics"]["stars"]
    followers_score=scores["metrics"]["followers"]

    if repository_score >=15:
        strengths.append("Maintains an active GitHub portfolio.")
    if language_score >=15:
        strengths.append("Works with multiple programming languages.")
    if stars_score>=20:
        strengths.append("Projects attract strong community interest.")
    if followers_score>=8:
        strengths.append("Has a growing presence in the developer community.")

    profile_completeness_score=scores["profile_completeness"]
    if profile_completeness_score>=80:
        strengths.append("Maintains a professional GitHub profile.")

    repo_quality_score=scores["repo_quality_score"]
    if repo_quality_score>=80:
        strengths.append("Creates well-maintained repositories.")
    if not strengths:
        strengths.append("This GitHub profile has room for improvement.")
    return strengths
    