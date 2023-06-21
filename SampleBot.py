import re
import asyncio
import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

#bot events
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} Welcome to the server, My command prefix is simply ! try saying !help for a list of commands")

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} Ya dun, bye!")



#loads the cogs directory
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

#runs the bot
async def main():
    await load()
    await bot.start("yourTokenHere")

asyncio.run(main())
