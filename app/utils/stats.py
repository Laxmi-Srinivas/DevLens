def get_user_stats(repos):
    stats={
        "total_repositories":len(repos),
        "total_stars":0,
        "total_forks":0,
        "languages":{},
        "most_starred_repo":""
    }
    max_stars=0
    for repo in repos:
        language=repo.language or "Unknown"
        stars=repo.stars
        if language not in stats["languages"]:
            stats["languages"][language]=0
        stats["languages"][language]+=1
        if max_stars < stars:
            stats["most_starred_repo"]=repo.name
            max_stars=stars
        stats["total_stars"]+=stars
        stats["total_forks"]+=repo.forks
        
        
    return stats