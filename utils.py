import os
import json

import asyncio
import aiohttp

from aiohttp import TCPConnector

api = "https://api.github.com"
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {token}",
}


async def github_utils(usernames, include):
    """
    Handler starts from here
    """
    tasks = []
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
        for username in usernames:
            task = asyncio.ensure_future(fetch_user(username, include, session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


async def fetch_commit_latest(username, repo, session):
    """
    Fetch commits related to repo
    """
    url = f"{api}/repos/{username}/{repo}/commits"
    try:
        async with session.get(url, headers=headers) as response:
            content = await response.read()
            response = json.loads(content)[0]
            data = dict()
            data["sha"] = response.get("sha")
            data["url"] = response.get("html_url")
            commit = response.get("commit")
            if commit:
                data["commit"] = {
                    "author": commit.get("author"),
                    "committer": commit.get("committer"),
                }
            return data
    except Exception as e:
        print(e)
        return url, "ERROR", str(e)


async def fetch_public_repos(username, include, session):
    """
    Fetch all repo repos
    """
    url = f"{api}/users/{username}/repos"
    try:
        async with session.get(url, headers=headers) as response:
            content = await response.read()
            response = json.loads(content)
            repos = list()
            for res in response:
                repo = dict()
                repo["id"] = res.get("id")
                repo["repo_name"] = res.get("name")
                repo["created_at"] = res.get("created_at")
                repo["updated_at"] = res.get("updated_at")
                repo["url"] = res.get("html_url")
                if include == "commit_latest":
                    commits = asyncio.ensure_future(
                        fetch_commit_latest(username, res.get("name"), session)
                    )
                    commit = await asyncio.gather(commits)
                    repo["commit_latest"] = commit
                repos.append(repo)
            repos = sorted(repos, key=lambda p: p["updated_at"], reverse=True)
            return repos
    except Exception as e:
        print(e)
        return url, "ERROR", str(e)


async def fetch_user(username, include, session):
    """
    Fetch all user details
    """
    url = f"{api}/users/{username}"
    try:
        async with session.get(url, headers=headers) as response:
            content = await response.read()
            response = json.loads(content)
            data = dict()
            data["id"] = response.get("id")
            data["login_name"] = response.get("login")
            data["url"] = response.get("html_url")
            repo = asyncio.ensure_future(fetch_public_repos(username, include, session))
            repos = await asyncio.gather(repo)
            data["public_repos"] = repos
            return data
    except Exception as e:
        print(e)
        return url, "ERROR", str(e)
