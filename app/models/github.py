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
    description: str | None
    homepage: str | None
    archived: bool
    size: int

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

class AnalysisResponse(BaseModel):
    total_score: int
    grade: str
    developer_level:str
    strengths:list[str]
    areas_for_improvement:list[str]
    metrics: dict[str, int]
    repo_quality_score:int
    profile_completeness:int
    recommendations: list[str]
    summary: str

class RepositoryAnalysis(BaseModel):
    average_stars: float
    average_forks: float
    repositories_with_description: int
    repositories_with_homepage: int
    archived_repositories: int
    empty_repositories: int
    repository_quality_score: int

class GitHubReport(BaseModel):
    user: GitHubUser
    stats: GitHubStats
    top_repositories: list[TopRepos]
    insights: Insights
    repository_analysis: RepositoryAnalysis
    analysis: AnalysisResponse