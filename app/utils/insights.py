from app.utils.stats import get_user_stats
def calculate_insights(repos):
    insights={
        "most_used_language":"None",
        "language_percentages":{},
        "average_stars":0,
        "average_forks":0,
        "most_forked_repo":"",
        "largest_repo":""
    }
    stats=get_user_stats(repos)
    if stats["total_repositories"]==0:
        return insights
    insights["most_used_language"]=max(stats["languages"],key=stats["languages"].get)

    for key,value in stats["languages"].items():
        insights["language_percentages"][key]=round(((value/stats["total_repositories"])*100),2)
    
    insights["average_stars"]=round((stats["total_stars"]/stats["total_repositories"]),2)
    insights["average_forks"]=round((stats["total_forks"]/stats["total_repositories"]),2)

    max_forks=0
    max_size=0
    for repo in repos:
        if max_forks < repo.forks:
            max_forks=repo.forks
            insights["most_forked_repo"]=repo.name
        if max_size < repo.size:
            max_size=repo.size
            insights["largest_repo"]=repo.name
    return insights

