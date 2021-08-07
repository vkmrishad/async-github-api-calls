from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_users_api_case1():
    """
    Test api status_code and response length for zero usernames
    """
    response = client.get("/users?usernames=")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_users_api_case2():
    """
    Test api status_code and response length for two usernames
    """
    response = client.get("/users?usernames=vkmrishad,mojombo")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_users_api_case3():
    """
    Test api status_code and response length for three usernames
    """
    response = client.get("/users?usernames=vkmrishad,mojombo,justeat")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_users_api_include_case4():
    """
    Test api status_code and response length and latest commit for two usernames
    """
    response = client.get("/users?usernames=vkmrishad,justeat&include=commit_latest")
    assert response.status_code == 200
    assert len(response.json()) == 2

    # check latest commit included
    res = response.json()
    exists = False
    if res[0].get("public_repos", {})[0].get("commit_latest"):
        exists = True
    assert exists is True
