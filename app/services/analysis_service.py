from app.models.github import GitHubRepos,RepositoryAnalysis

def get_analysis(repos: list[GitHubRepos]):
    analysis_report={
        "average_stars": 0,
        "average_forks": 0,
        "repositories_with_description": 0,
        "repositories_with_homepage": 0,
        "archived_repositories": 0,
        "empty_repositories": 0,
        "repository_quality_score": 0
    }
    if not repos:
        return RepositoryAnalysis(
            average_stars=0,
            average_forks=0,
            repositories_with_description=0,
            repositories_with_homepage=0,
            archived_repositories=0,
            empty_repositories=0,
            repository_quality_score=0
        )
    total_repos=len(repos)
    total_stars=sum(repo.stars for repo in repos)
    total_forks=sum(repo.forks for repo in repos)
    analysis_report["average_stars"]=round(total_stars/total_repos,2)
    analysis_report["average_forks"]=round(total_forks/total_repos,2)
    for repo in repos:
        if repo.description:
            analysis_report["repositories_with_description"] += 1
        if repo.homepage:
            analysis_report["repositories_with_homepage"] += 1
        if repo.archived:
            analysis_report["archived_repositories"] += 1
        if repo.size == 0:
            analysis_report["empty_repositories"] += 1
    analysis_report["repository_quality_score"]=calculate_repository_score(analysis_report,total_repos)
    return RepositoryAnalysis(
        average_stars= analysis_report["average_stars"],
        average_forks= analysis_report["average_forks"],
        repositories_with_description= analysis_report["repositories_with_description"],
        repositories_with_homepage= analysis_report["repositories_with_homepage"],
        archived_repositories= analysis_report["archived_repositories"],
        empty_repositories= analysis_report["empty_repositories"],
        repository_quality_score= analysis_report["repository_quality_score"]
    )

def calculate_repository_score(report,total_repos):
    description_score=(report["repositories_with_description"]/total_repos)*20
    homepage_score=(report["repositories_with_homepage"]/total_repos)*10
    avg_stars=report["average_stars"]
    if avg_stars >= 20:
        average_stars_score=30
    elif avg_stars >=15 :
        average_stars_score=27
    elif avg_stars >=10:
        average_stars_score=23
    elif avg_stars >=7:
        average_stars_score=18
    elif avg_stars >=5:
        average_stars_score=15
    elif avg_stars >=3:
        average_stars_score=10
    elif avg_stars >=1:
        average_stars_score=5
    else: 
        average_stars_score=0
    avg_forks=report["average_forks"]
    if avg_forks >= 10:
        average_forks_score=20
    elif avg_forks >=7:
        average_forks_score=17
    elif avg_forks >=5:
        average_forks_score=14
    elif avg_forks >=3:
        average_forks_score=10
    elif avg_forks >=1:
        average_forks_score=5
    else: 
        average_forks_score=0
    archived_repos_score=(report["archived_repositories"]/total_repos)*100
    if archived_repos_score >81:
        archived_repos_score=-10
    elif archived_repos_score >61:
        archived_repos_score=-8
    elif archived_repos_score>41:
        archived_repos_score=-6
    elif archived_repos_score>21:
        archived_repos_score=-4
    elif archived_repos_score>1:
        archived_repos_score=-2
    else:
        archived_repos_score=0
    empty_repos_score=(report["empty_repositories"]/total_repos)*100
    if empty_repos_score >81:
        empty_repos_score=-10
    elif empty_repos_score >61:
        empty_repos_score=-8
    elif empty_repos_score>41:
        empty_repos_score=-6
    elif empty_repos_score>21:
        empty_repos_score=-4
    elif empty_repos_score>1:
        empty_repos_score=-2
    else:
        empty_repos_score=0
    
    repository_quality_score = (
        description_score
        + homepage_score
        + average_stars_score
        + average_forks_score
        + archived_repos_score
        + empty_repos_score
    )

    return max(0,min(100,round(repository_quality_score)))
    
