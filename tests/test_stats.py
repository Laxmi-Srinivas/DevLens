from app.utils.stats import get_user_stats

repos = [
    {
        "name": "Repo1",
        "language": "Python",
        "stargazers_count": 5,
        "forks_count": 2,
    },
    {
        "name": "Repo2",
        "language": "Python",
        "stargazers_count": 3,
        "forks_count": 1,
    }
]

stats=get_user_stats(repos)
def test_total_repositories():
    assert stats["total_repositories"]==2

def test_total_stars():
    assert stats["total_stars"]==8

def test_total_forks():
    assert stats["total_forks"]==3

def test_language_count():
    assert stats["languages"]["Python"]==2

def test_most_starred_repo():
    assert stats["most_starred_repo"]=="Repo1"
