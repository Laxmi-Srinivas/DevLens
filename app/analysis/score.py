from app.analysis.metrics import repository_score, star_score, language_score, followers_score
from app.analysis.repository import get_analysis
from app.analysis.profile import calculate_profile_completeness
def calculate_profile_score(user, repos):
    final_score={
        "metrics":{
            "repository":repository_score(user.public_repos),
            "stars":star_score(sum(repo.stars for repo in repos)),
            "languages":language_score(repos),
            "followers":followers_score(user.followers),
        },
        "repo_quality_score":0,
        "profile_completeness":0,
        "total_score":0
            
    }
    repo_quality_score=get_analysis(repos).repository_quality_score
    profile_completeness=calculate_profile_completeness(user)
    final_score["repo_quality_score"]=repo_quality_score
    final_score["profile_completeness"]=profile_completeness
    metrics_score = (sum(final_score["metrics"].values()) / 60) * 100
    final_score["total_score"] = round(metrics_score * 0.60 + repo_quality_score * 0.25 + profile_completeness * 0.15)
    return final_score