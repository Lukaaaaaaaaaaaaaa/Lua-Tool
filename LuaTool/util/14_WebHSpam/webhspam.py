import requests
import time
from colorama import Fore
import os
import ctypes
from util.plugins.commun import * 

def webhookspam():
    setTitle("WebHook Spammer")
    clear()
    webhspamtitle()
    print(f"""{y}[>{y}]{m} NAPISI WEBHOOK ZA SPAMANJE """)
    webhook = input(f"""{y}[--->{y}]{m} WEBHOOK: """)
    print(f"""\n{y}[>{y}]{m} NAPISI PORUKU ZA SPAMANJE """)
    message = input(f"""{y}[--->{y}]{m} PORUKA: """)
    print(f"""\n{y}[>{y}]{m} KOLIKO PORUKA!(s) """)
    timer = input(f"""{y}[--->{y}]{m} KOLICINA: """)
    input(f"""\n\n{y}[--->{y}]{m} PRITISNI ENTER""")

    try:
        timeout = time.time() + 1 * float(timer)

        while time.time() < timeout:
            response = requests.post(
                webhook,
                json = {"content" : message},
                params = {'wait' : True}
            )
            clear()
            time.sleep(1)
            if response.status_code == 204 or response.status_code == 200:
                print(f"""{y}[>{y}]{m} PORUKE SU POSLANE !""")
            elif response.status_code == 429:
                print(f"""{y}[>{y}]{m} RATE LIMITED ({response.json()['retry_after']}ms)""")
                time.sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"""{y}[>{y}]{m} NIJE TOCAN KOD: {response.status_code}""")
    except:
        print(f"""      {y}[>{y}]{m} TVOJ REQUEST JE NE ISPRAVAN !""")
        time.sleep(2)
        clear()
        main()

    clear()
    webhspamtitle()
    print(f"""{y}[>{y}]{m} VAS WEBHOOK JE ISPAMAN! """)
    input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER UKOLIKO ZELIS IZACI!""")
    main()
    
webhookspam()
