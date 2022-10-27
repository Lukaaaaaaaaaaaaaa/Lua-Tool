import requests
import random
from time import sleep
from colorama import Fore

from util.plugins.commun import setTitle, getheaders, proxy

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{y}[{Fore.LIGHTGREEN_EX }>{y}]{m} GRUPA JE NAPRAVLJENA")
            elif response.status_code == 429:
                print(f"{y}[y{y}]{m} RATE LIMITED ({response.json()['retry_after']}ms)")
            else:
                print(f"{y}[!{y}]{m} ERROR: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} NAPRAVLJENE GRUPE")
            elif response.status_code == 429:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

groupspamtitle()
print(f"""{y}[>{y}]{m} NAPISITE TOKEN OD ACC KOJI ZELITE DA BUDE ISPAMOVAN""")
token = input(f"""{y}[--->{y}]{m} TOKEN: """)

print(f'\n{y}[{m}>{y}]{w} ZELITE LI IZABRATI USER (s) ZASPAMOVANJE ILI ZELITE POSTAVIT RANDOM?')
print(f'''
{y}[01{y}]{m} IZABERI USER(s) YOURSELF
{y}[02{y}]{m} RANDOM USERS
                    ''')
secondchoice = int(input(
    f'{y}[--->{y}]{m} IZABERI: '))

if secondchoice not in [1, 2]:
    input(f'{y}[>{y}]{m} POGRIJESAN BROJ')
    main()

#if they choose to import the users manually
if secondchoice == 1:
    setTitle(f"Creating groupchats")
    #if they choose specific users
    print(f'\n{y}[>{y}]{m} NAPISI USER S KOJIM OCES NAPRAVITI GROUPCHAT (id,id2,id3)')
    recipients = input(f'{y}[--->{y}]{m} USERS ID: ')
    user = recipients.split(',')
    if "," not in recipients:
        input(f"\n{y}[>{y}]{m} You didn't have any commas (,) format is id,id2,id3")
        main()
    input(f"\n\n\n{y}[--->{y}]{m} PRITISNI ENTER ZA NASTAVITI (\"ctrl + c\" at anytime to stop)")
    selector(token, user)

#if they choose to randomize the selection
elif secondchoice == 2:
    setTitle(f"PRAVI GRUPE")
    IDs = []
    #Get all users to spam groupchats with
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        IDs.append(friend['id'])
    input(f"\n{y}[--->{y}]{m} PRITISNI ENTER ZA NASTAVITI! (\"ctrl + c\" at anytime to stop)")
    randomizer(token, IDs)