import os
import requests
from colorama import Fore
from util.plugins.commun import * 

setTitle("Webhook Deleter")
clear()
webhremovertitle()

def webhooksremover():
    try:
        print(f"""{y}[>{y}]{m} NAPISITE WEBHOOK KJI ZELITE IZBRISATI! """)
        webhook = input(f"""{y}[--->{y}]{m} WEBHOOK LINK: """)
        requests.delete(webhook.rstrip())
        print(f"""\n{y}[!{y}]{m} WEBHOOK JE IZBRISAN!""")
        input(f"""\n{y}[--->{y}]{m} PRITISNITE ENTER ZA EXIT!""")
        main()
    except:
        print(f"""\n{y}[>{y}]{m} WEBHOOK NE MOZE BITI IZBRISAN!""")
        input(f"""\n{y}[--->{y}]{m} PRITISNITE ENTER ZA EXIT!""")
        main()
          
webhooksremover()