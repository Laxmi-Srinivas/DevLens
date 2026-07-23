from app.models.github import GitHubReport
from app.services.github_service import (
    get_user,
    get_user_repos,
    get_user_analysis
)
from app.services.analysis_service import get_repos_analysis
from app.utils.stats import get_user_stats
from app.services.analysis_service import build_analysis
from app.utils.sorting import sort_top_repos
from app.utils.insights import calculate_insights


def generate_report(username: str):
    user = get_user(username)

    repos = get_user_repos(username)

    return GitHubReport(
        user=user,
        stats=get_user_stats(repos),
        top_repositories=sort_top_repos(repos),
        insights=calculate_insights(repos),
        repository_analysis=get_repos_analysis(repos),
        analysis=build_analysis(user,repos)
    )