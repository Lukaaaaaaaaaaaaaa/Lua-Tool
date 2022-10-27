import time, os, requests, random, os.path
from colorama import Fore
from util.plugins.commun import * 

def settingstheme():
    setTitle("Settings Changer")
    clear()
    settingscyclertitle()

    print(f"""{y}[>{y}]{m} OO DOLE MOZES PROMJENITI:\n\n          {y}[01{y}]{m} STATUS\n          {y}[02{y}]{m} BOJA TEME\n          {y}[03{y}]{m} LANGUAGE\n\n""")
    choice = input(f"""{y}[--->{y}]{m} ODABERI STO ZELIS PROMJENITI: """)

    if choice == "1":
        print(f"\n{y}[>{y}]{m} NAPISI TOKEN KOJEM ZELIS PRMJENII STATUE")
        token = input(f"{y}[--->{y}]{m} TOKEN: ")
        print(f"\n{y}[>{y}]{m} KOLIKO STATUES ZELIS PROMJENITI (max 4)")
        statue_number = int(input(f"{y}[--->{y}]{m} KOLICINA: "))
        print(f"\n{y}[>{y}]{m} KOLKO PUTA DA SE MJENJA U SEKUNDAMA (Recommended time: 5)")
        times = int(input(f"{y}[--->{y}]{m} VRIJEME: "))
        print("\n")
        statues = []

        headers = {'Authorization': token, 'Content-Type': 'application/json'}

        if statue_number >= 1 and statue_number <= 4:
            for loop in range(0, statue_number):
                print(f"""{y}[>{y}]{m} IZABERI CUSTOM STATUS #{loop+1}""")
                choice = str(input(f"""{y}[--->{y}]{m} STATUS #{loop+1}: """))
                statues.append(choice)
        else:
            print(f"""\n{y}[>{y}]{m} INVALID NUMBER""")
            input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
            main()

        input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER DA ZAPOCNES""")
        clear()
        while True:
            for i in range(len(statues)):
                CustomStatus = {"custom_status": {"text": statues[i]}}
                try:
                    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
                    print(f"""{y}[>{y}]{m} STATUS JE PROMJENJEN NA "{statues[i]}" """)
                    i += 1
                    time.sleep(times)
                except Exception as e:
                    print(f"{y}[>{y}]{m} ERROR: {e}")
                    time.sleep(times)

    elif choice == "2":
        print(f"""{y}[>{y}]{m} STAVI TOKEN KOJEM ZELIS PROMJENITI TEMU""")
        token = input(f"""{y}[--->{y}]{m} TOKEN: """)

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if r.status_code == 200:
            print(f"""\n{y}[>{y}]{m} NAPISI BROJ PROMJENA : """)
            amount = int(input(f"""{y}[--->{y}]{m} KOLICINA: """))
            print()
            from itertools import cycle
            modes = cycle(["light", "dark"])
            clear()
            for i in range(amount):
                print(f"""{y}[{i+1}{y}]{m} TEMA JE USPJESNO PROMJENJENA""")
                time.sleep(0.5)
                setting = {'theme': next(modes)}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            clear()
            settingscyclertitle()
            print(f"""{y}[>{y}]{m} PROMJENA JE USPJESNO PROMJENJENA""")
            input(f"""{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
            main()
        else:
            print(f"""          {y}[>{y}]{m} NETOCAN TOKEN""")
            input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
            main()
    elif choice == "3":
        print(f"""{y}[>{y}]{m} NAPISI TOKEN KOJEM ZELIS PROMJENITI LANGUAGE""")
        token = input(f"""{y}[--->{y}]{m} TOKEN: """)

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if r.status_code == 200:
            print(f"""\n{y}[>{y}]{m} NAPISI BROJ PROMJENA : """)
            amount = int(input(f"""{y}[--->{y}]{m} KOLICINA: """))
            print()
            clear()
            for i in range(amount):
                print(f"""{y}[{i+1}{y}]{w} JEZIK JE USPJESNO PROMJENJEN""")
                time.sleep(1)
                setting = {'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
            clear()
            settingscyclertitle()
            print(f"""{y}[>{y}]{m} PROMJENA JE USPJESNO ZAVRSENA""")
            input(f"""{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
            main()
        else:
          print(f"""          {y}[>{y}]{m} NETOCAN TOKEN""")
          input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
          main()
    else:
        print(f"""          {y}[>{y}]{m} POGRIJESNO STE ODABRALI""")
        input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
        main()
          
settingstheme()
