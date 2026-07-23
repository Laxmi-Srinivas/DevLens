def sort_top_repos(repos):
    top_repos=[]
    for repo in repos:
        name=repo.name
        stars=repo.stars
        language=repo.language or "Unknown"
        top_repos.append({"name":name,"stars":stars,"language":language})
    return sorted(top_repos, key=lambda x: x["stars"],reverse=True)[:5]
