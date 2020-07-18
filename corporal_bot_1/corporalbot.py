import discord
from discord.ext import commands
import random
import os
import time
import json

bot = commands.Bot(command_prefix='.')


def __init__(self, bot: commands.Bot):
    self.bot = bot


@bot.event
async def on_ready():
    print('bot is ready.')
    game = discord.Game("with mr.C")
    await bot.change_presence(status=discord.Status.online, activity=game)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzIwNTU2MDk2NjY5ODc2Mjc3.XuNQPg.g2kIqVlKos-kEuvAX3P03QlEyOw')
