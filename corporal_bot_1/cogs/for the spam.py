import discord
from discord.ext import commands
import random

async def spam_type(ctx , word , number):
    for i in range(number):
        await ctx.send(word)

class spams(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('spam is ready.')

    @commands.command()
    async def spam(self, ctx, times, *, arg):
        if times == 'max':
            nos = int(len(arg)/250)
            nos = nos - 1
            await spam_type(ctx , arg , times)

        else:
            times = int(times)
            await spam_type(ctx , arg, times)


def setup(bot: commands.Bot):
    bot.add_cog(spams(bot))
