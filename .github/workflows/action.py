import os
import requests


url = "https://api.github.com/search/issues?q=repo:gitRenc/gitAction2+is:pr+is:merged+merged:%3E=2023-01-27T06:59:50&sort=merged"
try:
    response = requests.post(url)
    # Call the conversations.list method using the WebClient

    # Print result, which includes information about the message (like TS)
    print(response)
except:
    print("api call failed")
