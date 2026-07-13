def sort_top_repos(repos:list):
    top_repos=[]
    for repo in repos:
        name=repo.get("name")
        stars=repo.get("stargazers_count")
        language=repo.get("language") or "Unknown"
        top_repos.append({"name":name,"stars":stars,"language":language})
    return sorted(top_repos, key=lambda x: x["stars"],reverse=True)[:5]
