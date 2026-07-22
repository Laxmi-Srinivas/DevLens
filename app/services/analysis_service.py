from app.analysis.repository import get_analysis
from app.models.github import GitHubRepos

def get_repos_analysis(repos:list[GitHubRepos]):
    return get_analysis(repos)