from app.analysis.metrics import repository_score, star_score, language_score, followers_score

def calculate_profile_score(user, repos):
    final_score={
        "metrics":{
            "repository":repository_score(user.public_repos),
            "stars":star_score(sum(repo.stars for repo in repos)),
            "languages":language_score(repos),
            "followers":followers_score(user.followers)
        },
        "total_score":0
            
    }
    final_score["total_score"]=sum(final_score["metrics"].values())
    return final_score