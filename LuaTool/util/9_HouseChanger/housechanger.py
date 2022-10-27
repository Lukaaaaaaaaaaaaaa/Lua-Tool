import os
import requests
from colorama import Fore
from util.plugins.commun import * 

def hypesquadchanger():
    setTitle("HypeSquad Changer")
    clear()
    housechangertitle()
    print(f"""{y}[>{y}]{m} NAPISI STA OCES: \n\n""")
    print(f"""          {y}[01{y}]{m} BRAVERY\n""")
    print(f"""          {y}[02{y}]{m} BRILLIANCE\n""")
    print(f"""          {y}[03{y}]{m} BALANCE\n\n\n""")
    print(f"""{y}[>{y}]{m} IZABERI NESTO""")
    house = str(input(f"""{y}[--->{y}]{m} NAPISI: """))
    print(f"""\n{y}[>{y}]{m} NAPISI TOKEN KOJI ZELIS PROMJENITI""")
    token = str(input(f"""{y}[--->{y}]{m} TOKEN: """))

    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
      headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
      if house == "1" or house == "01":
          payload = {'house_id': 1}
      elif house == "2" or house == "02":
          payload = {'house_id': 2}
      elif house == "3" or house == "03":
          payload = {'house_id': 3}
      else:
          print(f"""          {y}[{Fore.LIGHTCYAN_EX }>{y}]{m} NEISPRAVNO SI ODABRAO""")
          input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER ZA EXITE""")
          main()
      r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
      if r.status_code == 204:
        print(f""" \n{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} HYPEDSQUAD CHANGED""")
        input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER ZA EXITE""")
        main()
    else:
      print(f"""          {y}[{Fore.LIGHTCYAN_EX }>{y}]{w} INVALID TOEN""")
      input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER ZA EXITE""")
      main()
          
hypesquadchanger()
