import os, time, os.path
from colorama import Fore
from util.plugins.commun import * 

def autologin() :
    from selenium import webdriver
    setTitle("Auto Login")
    clear()
    autologintitle()
    print(f"""{y}[>{y}]{m} NAPISI TOKEN OD ACC U KOJI SE ZELIS LOGIRATI""")
    entertoken = str(input(f"""{y}[--->{y}]{m} TOKEN: """))
    try:
        driver = webdriver.Chrome(executable_path=r'util/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            clear()
            autologintitle()
            print(f"""{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} KONEKCIJA JE NE USPIJESNA""")
            driver.close()
        else:
            clear()
            autologintitle()
            print(f"""{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} KONEKCIJA JE ESTABLISHED""")
        input(f"""{y}[--->{y}]{m} PRITISNI ENTER DA IZADJES""")
        main()
    except:
        print(f"""      {y}[{Fore.LIGHTCYAN_EX }>{y}]{m} NEKI JE PROBLEM S TOKENOM!""")
        time.sleep(2)
        clear()
        main()

autologin()
