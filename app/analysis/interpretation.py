def generate_strengths(scores)->list[str]:
    strengths=[]
    repository_score=scores["metrics"]["repository"]
    language_score=scores["metrics"]["languages"]
    stars_score=scores["metrics"]["stars"]
    followers_score=scores["metrics"]["followers"]

    if repository_score >=12:
        strengths.append("Maintains a broad portfolio of public repositories.")
    if language_score >=12:
        strengths.append("Demonstrates experience across multiple programming languages.")
    if stars_score>=20:
        strengths.append("Projects attract strong community interest.")
    if followers_score>=4:
        strengths.append("Has a growing presence in the developer community.")

    profile_completeness_score=scores["profile_completeness"]
    if profile_completeness_score>=75:
        strengths.append("GitHub profile is well presented with strong professional information.")

    repo_quality_score=scores["repo_quality_score"]
    if repo_quality_score>=80:
        strengths.append("Creates well-maintained repositories.")
    if not strengths:
        strengths.append("This GitHub profile has room for improvement.")
    return strengths
    
def generate_weaknesses(scores)->list[str]:
    weaknesses=[]
    repository_score=scores["metrics"]["repository"]
    language_score=scores["metrics"]["languages"]
    stars_score=scores["metrics"]["stars"]
    followers_score=scores["metrics"]["followers"]

    if repository_score <=5:
        weaknesses.append("Portfolio contains relatively few public repositories.")
    if language_score <=6:
        weaknesses.append("Portfolio could showcase a wider variety of technologies.")
    if stars_score<20:
        weaknesses.append("Projects have received limited community engagement.")
    if followers_score<2:
        weaknesses.append("Projects have opportunities to gain greater community visibility.")

    profile_completeness_score=scores["profile_completeness"]
    if profile_completeness_score<=50:
        weaknesses.append("GitHub profile could include more professional information.")

    repo_quality_score=scores["repo_quality_score"]
    if repo_quality_score<60:
        weaknesses.append("Some repositories could benefit from improved documentation or maintenance.")
    if not weaknesses:
        weaknesses.append("No significant weaknesses identified.")
    return weaknesses
    
def generate_recommendations(scores):
    recommendations=[]
    repository_score=scores["metrics"]["repository"]
    language_score=scores["metrics"]["languages"]
    stars_score=scores["metrics"]["stars"]
    followers_score=scores["metrics"]["followers"]

    if repository_score <=5:
        recommendations.append("Build additional public projects that demonstrate your skills.")
    if language_score <=6:
        recommendations.append("Incorporate a broader mix of frameworks and languages to demonstrate technical versatility.")
    if stars_score<20:
        recommendations.append("Build projects that solve real problems and share them with the developer community.")
    if followers_score<2:
        recommendations.append("Share your project links on social platforms or developer forums to get more people looking at your work.")

    profile_completeness_score=scores["profile_completeness"]
    if profile_completeness_score<=50:
        recommendations.append("Complete your GitHub profile with a professional bio and other profile details.")

    repo_quality_score=scores["repo_quality_score"]
    if repo_quality_score<60:
        recommendations.append("Review your existing project folders to clean up code, update files, and make them easier to navigate.")
    if not recommendations:
        recommendations.append("Keep doing what you are doing—your profile looks great.")
    return recommendations

def generate_summary(scores):
    score = scores["total_score"]
    if score >= 90:
        return (
            "This GitHub profile demonstrates an exceptional software engineering portfolio with strong technical depth, professional presentation, and significant community impact."
        )
    elif score >= 75:
        return (
            "This GitHub profile represents a strong software engineering portfolio with well-maintained projects and good community recognition. There are a few opportunities to further strengthen the profile."
        )
    elif score >= 60:
        return (
            "This GitHub profile demonstrates a solid software engineering portfolio with meaningful projects and good development practices. Continued improvements to documentation, profile presentation, and project diversity would further strengthen the portfolio."
        )
    elif score >= 40:
        return (
            "This GitHub profile is developing steadily. Building additional projects and improving repository quality will significantly enhance the portfolio."
        )
    else:
        return (
            "This GitHub profile is in the early stages of development. Continued work on projects and profile presentation will help build a stronger software engineering portfolio."
        )