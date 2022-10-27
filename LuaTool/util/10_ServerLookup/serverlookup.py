import requests
from colorama import Fore
from util.plugins.commun import * 

def serverlookup():
    setTitle("Server Lookup")
    clear()
    serverlookuptitle()
    print(f"""{y}[{Fore.LIGHTCYAN_EX }>{y}]{m} OVDJE JE SVE STO MOZETE PRONACI: \n\n""")
    print(f"""          {y}[>{y}]{m} INVITE LINK           {y}[>{y}]{m} INVITER USERNAME      {y}[>{y}]{m} GUILD BANNER          {y}[>{y}]{m} GUILD SPLASH\n""")
    print(f"""          {y}[>{y}]{m} CHANNEL NAME          {y}[>{y}]{m} INVITER ID            {y}[>{y}]{m} GULD DESCRIPTION      {y}[>{y}]{m} GUILD FEATURES\n""")
    print(f"""          {y}[>{y}]{m} CHANNEL ID            {y}[>{y}]{m} GUILD NAME            {y}[>{y}]{m} CUSTOM INVITE LINK\n""")
    print(f"""          {y}[>{y}]{m} EXPIRATION DATE       {y}[>{y}]{m} GUILD ID              {y}[>{y}]{m} VERIFICATION LEVEL\n\n\n\n""")
    print(f"{y}[>{y}]{m} POSTAVI DISCORD LINK: ")
    invitelink = input(f"""{y}[--->{y}]{m} INVITE LINK: """)

    try:
        res = requests.get(f"https://discord.com/api/v9/invites/{invitelink}")
    except:
        input(f"""          {y}[{Fore.LIGHTCYAN_EX }--->{y}]{m} JEDAN ERROR JE PRONADJEN!""")
        main()

    if res.status_code == 200:
        res_json = res.json()
        invite_link = f'https://discord.gg/{res_json["code"]}'
        invite_channel_name = res_json["channel"]["name"]
        invite_channel_id = res_json["channel"]["id"]
        invite_expires_at = res_json["expires_at"]

        inviter_username = f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'
        inviter_user_id = res_json["inviter"]["id"]

        server_name = res_json["guild"]["name"]
        server_id = res_json["guild"]["id"]
        banner = res_json["guild"]["banner"]
        description = res_json["guild"]["description"]
        custom_invite_link = res_json["guild"]["vanity_url_code"]
        verification_level = res_json["guild"]["verification_level"]
        splash = res_json["guild"]["splash"]
        features = res_json["guild"]["features"]

        print(f"""\n{y}[>{y}]{m} INVITATION INFORMATION:""")
        print(f"""          {y}[--->{y}]{m} INVITE LINK: {invite_link}""")
        print(f"""          {y}[--->{y}]{m} CHANNEL: {invite_channel_name} ({invite_channel_id})""")
        print(f"""          {y}[--->{y}]{m} EXPIRATION DATE: {invite_expires_at}\n\n""")

        print(f"""{y}[>{y}]{m} INVIER INFORMATION:""")
        print(f"""          {y}[--->{y}]{m} USERNAME: {inviter_username}""")
        print(f"""          {y}[--->{y}]{m} USER ID: {inviter_user_id}\n\n""")

        print(f"""{y}[>{y}]{m} SERVER INFORMATION:""")
        print(f"""          {y}[--->{y}]{m} NAME: {server_name}""")
        print(f"""          {y}[--->{y}]{m} SERVER ID: {server_id}""")
        print(f"""          {y}[--->{y}]{m} BANNER: {banner}""")
        print(f"""          {y}[--->{y}]{m} DESCRIPTION: {description}""")
        print(f"""          {y}[--->{y}]{m} CUSTOM INVITE LINK: {custom_invite_link}""")
        print(f"""          {y}[--->{y}]{m} VERIFICATION LEVEL: {verification_level}""")
        print(f"""          {y}[--->{y}]{m} SPLAYSH: {splash}""")
        print(f"""          {y}[--->{y}]{m} FEATURES: {features}""")
        
    else:
        input(f"""          {y}[{Fore.LIGHTCYAN_EX }>{y}]{m} JEDAN ERROR JE PRONADJEN!""")
        main()
    
    input(f"""\n\n{y}[--->{y}]{m} PRITISNI ENTER ZA NASTAVAK""")
    main()

serverlookup()
