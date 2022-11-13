token = ""
prefix = ""

import os
import discord
from discord.ext import commands

print("[BOT] Logando na sua conta...")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

os.system('clear')


@bot.event
async def on_ready():
    print("\n\n[BOT] Show, agora só gozar e dar cl")
    print(f"[BOT] User: {bot.user.name}")
    print(f"[BOT] ID: {bot.user.id}\n\n")


@bot.command()
async def gozei(ctx, limit: int = None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"[Complete] Removed {passed} messages with {failed} fails")


bot.run(token, bot=False)
