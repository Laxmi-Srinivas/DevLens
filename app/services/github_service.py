from fastapi import HTTPException
from app.models.github import GitHubUser, GitHubRepos,AnalysisResponse
from app.utils.stats import get_user_stats
from app.utils.sorting import sort_top_repos
from app.utils.insights import calculate_insights
from app.services.analysis_service import build_analysis
import httpx


def fetch_user(username:str)->dict:
    response=httpx.get(f"https://api.github.com/users/{username}")
    
    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user not found"
        )

    data=response.json()

    return data    

def fetch_repos(username:str)->list[dict]:
    response=httpx.get(f"https://api.github.com/users/{username}/repos")
    
    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user not found"
        )

    data=response.json()

    return data     

def get_user(username:str):

    data=fetch_user(username)

    return GitHubUser(
        username=data.get("login"),
        name=data.get("name"),
        following=data.get("following"),
        followers=data.get("followers"),
        public_repos=data.get("public_repos"),
        bio=data.get("bio"),
        location=data.get("location"),
        company=data.get("company")
    )

def get_user_repos(username:str):

    data=fetch_repos(username)

    return [
        GitHubRepos(
            name=repo.get("name"),
            language=repo.get("language"),
            stars=repo.get("stargazers_count"),
            forks=repo.get("forks_count"),
            description=repo.get("description"),
            homepage=repo.get("homepage"),
            archived=repo.get("archived"),
            size=repo.get("size")
        )
        for repo in data
    ]


def get_stats(username):
    repos = get_user_repos(username)
    return get_user_stats(repos)

def get_top_repos(username):
    repos = get_user_repos(username)
    return sort_top_repos(repos)

def get_insights(username):
    repos = get_user_repos(username)
    return calculate_insights(repos)



def get_user_analysis(username):
    user = get_user(username)
    repos = get_user_repos(username)

    return build_analysis(user, repos)