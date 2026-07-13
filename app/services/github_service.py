from fastapi import APIRouter
from fastapi import HTTPException
from app.models.github import GitHubUser, GitHubRepos
from app.utils.stats import get_user_stats
from app.utils.sorting import sort_top_repos
from app.utils.insights import cal_insights
import httpx


def fetch_user(username:str):
    response=httpx.get(f"https://api.github.com/users/{username}")
    
    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user not found"
        )

    data=response.json()

    return data    

def fetch_repos(username:str):
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
            forks=repo.get("forks_count")
        )
        for repo in data
    ]


def get_stats(username:str):
    return get_user_stats(fetch_repos(username))

def get_top_repos(username:str):
    return sort_top_repos(fetch_repos(username))

def get_insights(username:str):
    return cal_insights(fetch_repos(username))