import os
import requests
import json
import asyncio
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta, timezone


async def getGithubMerged():
    baseUrl = "https://api.github.com/search/issues"
    owner = "gitRenc"
    repo = "gitAction2"

    # time in UTC
    # 18.00 utc = 02.00 wita
    startDate = datetime.now(timezone.utc) - timedelta(hours=24)
    endDate = datetime.now(timezone.utc)

    url = "{}?q=repo:{}/{}+is:pr+is:merged+merged:{}..{}".format(
        baseUrl, owner, repo, startDate, endDate)
    response = requests.get(url)
    try:
        json_data = json.loads(response.text)
        titles = []
        for item in json_data['items']:
            titles.append(item["title"])
        return titles
    except:
        return "github Api failed"


async def getJiraIssues():
    #
    # token link : https://id.atlassian.com/manage-profile/security/api-tokens
    #
    baseUrl = "https://richtesting.atlassian.net/rest/api/2/issue"
    projectKey = "ARA"
    token = "aad7AkZFyZcYTxThqmUX194D"
    email = "richbytesting@gmail.com"
    auth = HTTPBasicAuth(email, token)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    # query for jira request
    params = {
        "field": "status",
        "project": projectKey
    }

    issues = []
    titles = await getGithubMerged()
    try:
        if len(titles) > 0:
            for items in titles:
                url = "{}/{}".format(baseUrl, items)
                response = requests.get(
                    url, headers=headers, auth=auth, params=params)
                if (response.status_code == 200):
                    json_data = json.loads(response.text)
                    issues.append({
                        json_data["key"]: json_data["fields"]["status"]["name"]
                    })
        else:
            return ("no issues")
    except:
        return ("Jira Api failed")

    return (issues)


async def main():
    print(await getJiraIssues())


asyncio.run(main())
