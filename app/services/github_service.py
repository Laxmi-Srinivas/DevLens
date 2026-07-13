from fastapi import APIRouter
from fastapi import HTTPException
from app.models.github import GitHubUser, GitHubRepos
from app.utils.stats import get_user_stats
from app.utils.sorting import sort_top_repos
import httpx


def get_user(username:str):
    response=httpx.get(f"https://api.github.com/users/{username}")
    
    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user not found"
        )

    data=response.json()
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
    response=httpx.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user Not Found"
        )
    
    data=response.json()

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
    response=httpx.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user Not Found"
        )
    
    data=response.json()

    return get_user_stats(data)

def get_top_repos(username:str):
    response=httpx.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code !=200:
        raise HTTPException(
            status_code=404,
            detail="Github user not Found"
        )
    
    data=response.json()

    return sort_top_repos(data)