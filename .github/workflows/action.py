import os
import requests


url = "https://api.github.com/search/issues"
params = {
    "q": "repo:gitRenc/gitAction2+is:pr+is:merged+merged:%3E=2023-01-27T06:59:50",
    "sort": "merged"
}
# q=repo:gitRenc/gitAction2+is:pr+is:merged+merged:%3E=2023-01-27T06:59:50
# sort=merged
try:
    response = requests.post(url, params=params)
    # Call the conversations.list method using the WebClient

    # Print result, which includes information about the message (like TS)
    print(response)
    print(response.json())
    print("api call done")
except:
    print("api call failed")
