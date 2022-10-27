import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.commun import *

def search_for_updates():
    clear()
    setTitle("{c}UCITAVA SE... ")
    r = requests.get("https://github.com/Lukaaaaaaaaaaaaaa/Lua-Tool/tree/main/LuaTool")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        setTitle("")
        print(f'''                    \n'''.replace('█', f'{m}█{y}'))
        discserver()
        soup = BeautifulSoup(requests.get("https://github.com/Lukaaaaaaaaaaaaaa/Lua-Tool/tree/main/LuaTool").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(f'\n{y}[--->{y}]{c}discord.gg/bvcbgq6V\n{y}[--->{y}]{c}discord.gg/qhsDZMNb\n{y}[--->{y}]{c}JOIN US DISCORD SERVER\n\n{y}[--->{y}]{m} AKO ZELITE NASTAVITI PRITISNITE ENTER!')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n{y}[--->{y}]{m} UCITAVANJE...")
            setTitle(f'UCITAVANJE...')

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("MULTI_TOOL.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("MULTI_TOOL.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("MULTI_TOOL.zip")
                cwd = os.getcwd()+'\\MULTI_TOOL\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), '@TIO.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('MULTI_TOOL')
                setTitle('MULTI_TOOL Update Complete!')
                input(f"\n{y}[!{y}]{m} ZAVRSENO !", end="")
                os.startfile("@TIO.exe")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/Lukaaaaaaaaaaaaaa/Lua-Tool/tree/main/LuaTool")
                with open("Discord-All-Tools-In-One-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Discord-All-Tools-In-One-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Discord-All-Tools-In-One-main.zip")
                cwd = os.getcwd()+'\\Discord-All-Tools-In-One-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                setTitle('@TIO Update Complete!')
                input(f"\n{y}[!{y}]{m} Update Successfully Finished!")
                if os.path.exists(os.getcwd()+'setup.bat'):
                    os.startfile("setup.bat")
                elif os.path.exists(os.getcwd()+'start.bat'):
                    os.startfile("start.bat")
                os._exit(0)
