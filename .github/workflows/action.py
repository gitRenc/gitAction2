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
        baseUrl, owner, repo, startDate.strftime("%Y-%m-%dT%H:%M"), endDate.strftime("%Y-%m-%dT%H:%M"))

    try:
        response = requests.get(url)
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
    # ini tokennya bisa di taro di secret key github
    token = "kNRVJTZ975GrPqPuGfoyFE78"
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
                        "title": json_data["key"],
                        "status": json_data["fields"]["status"]["name"]
                    })
        else:
            return ("no issues")
    except:
        return ("Jira Api failed")

    return (issues)


async def postTeams():
    url = "https://ptwolkkclouddevelopment.webhook.office.com/webhookb2/cfa586db-88e3-4755-b058-579cc7ac7927@509671eb-b559-459a-87f0-5635b2ec0f07/IncomingWebhook/1abc1617584648dc908146d794fd4a94/645af85f-a16e-4d30-9f7a-bf0ca707c61e"
    headers = {
        "Content-Type": "application/json",
    }

    issues = await getJiraIssues()
    issuesString = ""
    startDate = datetime.now(timezone.utc) - timedelta(hours=24)
    endDate = datetime.now(timezone.utc)
    startDateFormated = startDate.strftime("%Y-%m-%d")
    endDateFormated = endDate.strftime("%Y-%m-%d")
    if (len(issues) > 0):
        for x in issues:
            x = "- {} - {}\n".format(x["title"], x["status"])
            issuesString += x
    content = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "medium",
                            "weight": "bolder",
                            "text": "Jira Issues"
                        },
                        {
                            "type": "ColumnSet",
                            "columns": [
                                {
                                    "type": "Column",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "spacing": "None",
                                            "text": "From : {}".format(startDateFormated),
                                            "isSubtle": "true",
                                            "wrap": "true"
                                        },
                                        {
                                            "type": "TextBlock",
                                            "spacing": "None",
                                            "text": "To: {}".format(endDateFormated),
                                            "isSubtle": "true",
                                            "wrap": "true"
                                        }
                                    ],
                                    "width": "stretch"
                                }
                            ]
                        },
                        {
                            "type": "TextBlock",
                            "text": "{}".format(issuesString),
                            "wrap": "true"
                        },
                        {
                            "type": "TextBlock",
                            "text": "latest build : halo",
                            "wrap": "true"
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.5"
                }
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=content)
        print(response)
    except:
        print("teams api failed")

    return "haha"


async def main():
    print(await postTeams())


asyncio.run(main())
