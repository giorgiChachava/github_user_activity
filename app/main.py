import sys
import json
import time
from pathlib import Path
import requests
from .visuals import typeout, typeout2, typeout3


def show_greetings():
    typeout2("---------------------------")
    typeout3("""   /$$$$$$  /$$   /$$  /$$$$$$ 
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

def show_events(response):
    data = response.json()
    print(data)
    
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
            print("----- Username isn't registered on GitTub")
        else:
            print("----- Sorry there is an error and I am unable to help you...")
    

    
if __name__ == "__main__":
    main()