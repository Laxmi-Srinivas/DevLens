from app.utils.stats import get_user_stats
def cal_insights(repos:list):
    insights={
        "most_used_language":"",
        "language_percentages":{},
        "average_stars":0,
        "average_forks":0,
        "most_forked_repo":"",
        "largest_repo":""
    }
    stats=get_user_stats(repos)
    insights["most_used_language"]=max(stats["languages"],key=stats["languages"].get)

    for key,value in stats["languages"].items():
        insights["language_percentages"][key]=(value/stats["total_repositories"])*100
    
    insights["average_stars"]=stats["total_stars"]/stats["total_repositories"]
    insights["average_forks"]=stats["total_forks"]/stats["total_repositories"]

    max_forks=0
    max_size=0
    for repo in repos:
        if max_forks < repo.get("forks_count"):
            max_forks=repo.get("forks_count")
            insights["most_forked_repo"]=repo.get("name")
        if max_size < repo.get("size"):
            max_size=repo.get("size")
            insights["largest_repo"]=repo.get("name")
    return insights

