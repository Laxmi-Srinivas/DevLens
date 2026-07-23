from app.analysis.repository import get_analysis
from app.models.github import GitHubRepos, AnalysisResponse
from app.analysis.score import calculate_profile_score
from app.analysis.grading import calculate_grade
from app.analysis.levels import calculate_developer_level
from app.analysis.interpretation import generate_strengths, generate_weaknesses, generate_summary, generate_recommendations

def get_repos_analysis(repos:list[GitHubRepos]):
    return get_analysis(repos)


def build_analysis(user, repos):
    scores = calculate_profile_score(user, repos)

    return AnalysisResponse(
        total_score=scores["total_score"],
        grade=calculate_grade(scores["total_score"]),
        developer_level=calculate_developer_level(scores["total_score"]),

        strengths=generate_strengths(scores),
        areas_for_improvement=generate_weaknesses(scores),

        metrics=scores["metrics"],
        repo_quality_score=scores["repo_quality_score"],
        profile_completeness=scores["profile_completeness"],

        recommendations=generate_recommendations(scores),
        summary=generate_summary(scores),
    )