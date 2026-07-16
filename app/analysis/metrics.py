from app.models.github import GitHubRepos

def repository_score(repo_count:int)->int:
    if repo_count <= 2:
        return 0
    elif repo_count <= 5:
        return 3
    elif repo_count <= 10:
       return 6
    elif repo_count <= 20:
        return 10
    elif repo_count <= 40:
        return 13
    return 15

def star_score(stars_count:int)->int:
    if stars_count < 1:
        return 0
    elif stars_count <=5:
        return 5
    elif stars_count <=20:
        return 10
    elif stars_count <=50:
        return 15
    elif stars_count <=100:
        return 20
    return 25

def language_score(repos: list[GitHubRepos])-> int:
    languages=set()
    for repo in repos:
        if repo.language is not None:
            languages.add(repo.language)
    count=len(languages)
    if count == 0:
        return 0
    elif count == 1:
        return 6    
    elif count == 2:
        return 10
    elif count <=7:
        return 15
    elif count >=8:
        return 13
    
def followers_score(followers_count:int)->int:
    if followers_count <= 10:
        return 0
    elif followers_count <= 50:
        return 1
    elif followers_count <= 100:
        return 2
    elif followers_count <= 500:
        return 3
    elif followers_count <= 1000:
        return 4 
    return 5
    