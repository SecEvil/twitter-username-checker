from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def print_banner():
    banner = """
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
eViL        /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
"""
    print(banner)
    print("https://t.me/EvilHeere")
    print("https://t.me/spamingEVIL\n")

def is_username_available(username):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    url = f"https://twitter.com/{username}"
    try:
        driver.get(url)
        time.sleep(2)
        if "This account doesn’t exist" in driver.page_source:
            driver.quit()
            return True
        else:
            driver.quit()
            return False
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return False

print_banner()

with open("usernames.txt", "r") as f:
    usernames = [line.strip() for line in f.readlines()]

available = []

for uname in usernames:
    if is_username_available(uname):
        print(f"[✓] Available: {uname}")
        available.append(uname)
    else:
        print(f"[X] Taken: {uname}")

with open("available_usernames_selenium.txt", "w") as f:
    for name in available:
        f.write(name + "\n")

print("\nResults saved in available_user_evil.txt")
