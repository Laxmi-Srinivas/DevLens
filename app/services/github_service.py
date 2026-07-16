from fastapi import HTTPException
from app.models.github import GitHubUser, GitHubRepos,AnalysisResponse
from app.utils.stats import get_user_stats
from app.utils.sorting import sort_top_repos
from app.utils.insights import calculate_insights
from app.analysis.score import calculate_profile_score
from app.analysis.recommendations import generate_recommendations
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


def get_stats(username:str):
    return get_user_stats(fetch_repos(username))

def get_top_repos(username:str):
    return sort_top_repos(fetch_repos(username))

def get_insights(username:str):
    return calculate_insights(fetch_repos(username))

def get_user_analysis(username:str):
    user=get_user(username)
    repos=get_user_repos(username)

    scores=calculate_profile_score(user,repos)

    recommendations=generate_recommendations(user,repos,scores)
    
    return AnalysisResponse(
        total_score=scores["total_score"],
        metrics=scores["metrics"],
        recommendations=recommendations
    )