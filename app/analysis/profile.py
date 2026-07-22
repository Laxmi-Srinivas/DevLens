from app.models.github import GitHubUser

def calculate_profile_completeness(user: GitHubUser)->int:
    profile_completeness=0
    if user.bio:
        profile_completeness+=25
    if user.name:
        profile_completeness+=25
    if user.company:
        profile_completeness+=25
    if user.location:
        profile_completeness+=25

    return profile_completeness
