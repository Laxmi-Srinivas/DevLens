from fastapi import APIRouter
from app.services import github_service
from app.models.github import GitHubUser, GitHubRepos, GitHubStats,TopRepos,Insights

router=APIRouter()

@router.get("/github/{username}", response_model=GitHubUser)
def get_user(username:str):
    return github_service.get_user(username)

@router.get("/github/{username}/repos", response_model=list[GitHubRepos])
def get_user_repos(username:str):
    return github_service.get_user_repos(username)

@router.get("/github/{username}/stats", response_model=GitHubStats)
def get_userstats(username:str):
    return github_service.get_stats(username)

@router.get("/github/{username}/top-repos", response_model=list[TopRepos])
def get_top_repos(username:str):
    return github_service.get_top_repos(username)

@router.get("/github/{username}/insights", response_model=Insights)
def get_insights(username:str):
    return github_service.get_insights(username)