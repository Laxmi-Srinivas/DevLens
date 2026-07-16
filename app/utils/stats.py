def get_user_stats(repos:list):
    stats={
        "total_repositories":len(repos),
        "total_stars":0,
        "total_forks":0,
        "languages":{},
        "most_starred_repo":""
    }
    max_stars=0
    for repo in repos:
        language=repo.get("language") or "Unknown"
        stars=repo.get("stargazers_count",0)
        if language not in stats["languages"]:
            stats["languages"][language]=0
        stats["languages"][language]+=1
        if max_stars < stars:
            stats["most_starred_repo"]=repo.get("name")
            max_stars=stars
        stats["total_stars"]+=stars
        stats["total_forks"]+=repo.get("forks_count",0)
        
        
    return stats