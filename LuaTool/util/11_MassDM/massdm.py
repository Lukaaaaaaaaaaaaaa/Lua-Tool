import requests, threading
from colorama import Fore
from util.plugins.commun import setTitle, proxy, getheaders

setTitle("Mass DM")
clear()
massdmtitle()

def MassDM(token, channels, Message):
    for channel in channels:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
            try:
                setTitle(f"Messaging "+user)
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                    proxies=proxy(),
                    headers={'Authorization': token},
                    data={"content": f"{Message}"})
                print(f"{y}[>{y}]{m} MESSAGED: "+user+Fore.RESET)
            except Exception as e:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")


print(f"{y}[>{y}]{m} NAPISI TOKEN KOJI ZELIS DA BUDE ISPAMOVAN")
token = input(f"""{y}[--->{y}]{m} TOKEN: """)
print(f"\n{y}[>{y}]{m} PORUKA KOJA CE BITI POSLANA SVIM PRIJATELJIMA!")
message = str(input(f"{y}[--->{y}]{m} PORUKA: "))
clear()
processes = []
global channelIds
channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
if not channelIds:
    print(f"{y}[>{y}]{m} OVAJ RETARD NEMA DM BUDALA...")
    input(f"\n{y}[--->{y}]{m} PRITISNI ENTER ZA NASTAVAK")
    main()
for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
    t = threading.Thread(target=MassDM, args=(token, channel, message))
    t.start()
    processes.append(t)
for process in processes:
    process.join()
input(f"\n{y}[--->{y}]{m} PRITISNI ENTER ZA NASTAVAK")
main()