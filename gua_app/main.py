import sys
import json
import time
import requests
from .visuals import typeout, typeout2, typeout3


def show_greetings():
    typeout2("---------------------------")
    typeout3(r"""   /$$$$$$  /$$   /$$  /$$$$$$
 /$$__  $$| $$  | $$ /$$__  $$
| $$  \__/| $$  | $$| $$  \ $$
| $$ /$$$$| $$  | $$| $$$$$$$$
| $$|_  $$| $$  | $$| $$__  $$
| $$  \ $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/  |__/
                    
                    """)
    time.sleep(0.3)
    typeout("----- Hello, I am here to help you search for peoples actvities on github")
    typeout("----- You can call me GUA.")
    typeout("----- To use me, write following instructons: github-activity <username>")
    typeout("----- Now we can stalk people even without openning our browser. HOOORAYYY")

def find_events(events):
    for event in events:
        user = event["actor"]["display_login"]
        repo = event["repo"]["name"]
        if event["type"] == "WatchEvent":
            typeout2(f"----- starred repo: {repo}")
        elif event["type"] == "CommitCommentEvent":
            typeout2(f"----- commented on a commit in repo: {repo}")
        elif event["type"] == "CreateEvent":
            typeout2(f"----- created a new repo: {repo}")
        elif event["type"] == "DeleteEvent":
            typeout2(f"----- deleted a repo: {repo}")
        elif event["type"] == "DiscussionEvent":
            typeout2(f"----- created a new discussion in repo: {repo}")
        elif event["type"] == "ForkEvent":
            typeout2(f"-----  forked repo: {repo}")
        elif event["type"] == "GollumEvent":
            typeout2(f"----- created a new wiki page in repo: {repo}")  
        elif event["type"] == "IssueCommentEvent":
            typeout2(f"----- commented on an issue in repo: {repo}")
        elif event["type"] == "IssuesEvent":
            typeout2(f"----- created a new issue in repo: {repo}")
        elif event["type"] == "MemberEvent":
            typeout2(f"----- added a new member to repo: {repo}")
        elif event["type"] == "PublicEvent":
            typeout2(f"----- made a repo public: {repo}")
        elif event["type"] == "PullRequestEvent":
            typeout2(f"----- created a pull request in repo: {repo}")
        elif event["type"] == "PullRequestReviewEvent":
            typeout2(f"-----  reviewed a pull request in repo: {repo}")
        elif event["type"] == "PullRequestReviewCommentEvent":
            typeout2(f"----- commented on a pull request in repo: {repo}")
        elif event["type"] == "PushEvent":
            typeout2 (f"----- Pushed a new version to repo: {repo}")
        elif event["type"] == "ReleaseEvent":
            typeout2(f"----- Released a new version to repo: {repo}")

def show_events(response):
    data = response.json()
    if (data == []):
        typeout("----- No recent activity found for this user.")
    find_events(data)

    
def main():
    args=sys.argv[1:]
    if len(args)==0:
        show_greetings()
    elif len(args)!=1:
        typeout("----- Nuhuh. Github usernames consists of only 1 string.")
        typeout("----- To use me, write following instructons: github-activity <username>")
    else:
        username=args[0]
        url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(url)
        
        if response.status_code == 200:
            show_events(response)
        elif response.status_code == 404:
            typeout("----- Username isn't registered on GitHub")
        else:
            typeout("----- Sorry there is an error and I am unable to help you...")
    

    
if __name__ == "__main__":
    main()