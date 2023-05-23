import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online. Logged in as {bot.user.name} ({bot.user.id})')

bot.run('MTExMDM0MTYzMTMwOTI3MTA3MQ.GyvhiE.qGFN9wmDIVdU2BeNh646-xhiOsVrzLK8swydoM')