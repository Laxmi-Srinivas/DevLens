from pydantic import BaseModel

class GitHubUser(BaseModel):
    username: str
    name: str | None
    followers:int
    following:int
    public_repos:int
    bio:str | None
    location:str | None
    company:str | None

class GitHubRepos(BaseModel):
    name:str
    language:str | None
    stars:int
    forks:int

class GitHubStats(BaseModel):
    total_repositories: int
    total_stars: int
    total_forks: int
    languages: dict[str, int]
    most_starred_repo: str

class TopRepos(BaseModel):
    name:str
    stars:int
    language:str | None

class Insights(BaseModel):
    most_used_language:str
    language_percentages:dict[str,float]
    average_stars:float
    average_forks:float
    most_forked_repo:str
    largest_repo:str