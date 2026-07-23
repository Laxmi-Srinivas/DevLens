from fastapi import HTTPException
from app.models.github import GitHubUser, GitHubRepos,AnalysisResponse
from app.utils.stats import get_user_stats
from app.utils.sorting import sort_top_repos
from app.utils.insights import calculate_insights
from app.analysis.score import calculate_profile_score
from app.analysis.grading import calculate_grade
from app.analysis.levels import calculate_developer_level
from app.analysis.interpretation import generate_strengths, generate_weaknesses, generate_summary, generate_recommendations
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
    grade=calculate_grade(scores["total_score"])
    developer_level=calculate_developer_level(scores["total_score"])
    strengths=generate_strengths(scores)
    weaknesses=generate_weaknesses(scores)
    recommendations=generate_recommendations(scores)
    summary=generate_summary(scores)
    return AnalysisResponse(
        total_score=scores["total_score"],
        grade=grade,
        developer_level=developer_level,
        strengths=strengths,
        areas_for_improvement=weaknesses,
        metrics=scores["metrics"],
        repo_quality_score=scores["repo_quality_score"],
        profile_completeness=scores["profile_completeness"],
        recommendations=recommendations,
        summary=summary
    )