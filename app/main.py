import sys
import json
import time
from pathlib import Path

from .visuals import typeout, typeout2, typeout3


def show_greetings():
    print()
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
    typeout("----- To use me write following instructons: github-activity <username>")
    typeout("----- Now we can stalk people even without openning our browser. HOOORAYYY")

def main():
    args=sys.argv[1:]
    if len(args)==0:
        show_greetings()
    if len(args!=1):
        typeout("----- Nuhuh. Github usernames consists of only 1 string.")
        typeout("----- To use me write following instructons: github-activity <username>")
        
    
    

    
if __name__ == "__main__":
    main()