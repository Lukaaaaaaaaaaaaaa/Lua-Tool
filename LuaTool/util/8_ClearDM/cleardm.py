import os, os.path, discord
from discord.ext import commands
from colorama import Fore
from util.plugins.commun import * 

setTitle("clear DM")
clear()
cleardmtitle()
print(f"""{y}[>{y}]{m} NAPISI TOKEN!""")
token = input(f"""{y}[--->{y}]{m} TOKEN: """)
print(f"""\n{y}[--->{y}]{m} NAPISI "!clear" U DM KOJI ZELIS IZBRISATI""")

global bot
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"\n{y}[>{y}]{m} Removed {passed} messages with {failed} fails")
    input(f"""\n{y}[--->{y}]{m} PRITISNI ENTER ZA EXIT!""")
    main()

bot.run(token, bot=False)