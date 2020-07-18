import discord
from discord.ext import commands
import json


def add_link(key, content):
    with open('link.json', 'r') as f:
        link = json.load(f)

    link[key] = str(content)

    with open('link.json', 'w') as f:
        json.dump(link, f, indent=2)


def get_link(key):
    with open('link.json', 'r') as f:
        link = json.load(f)

    return link[str(key)]


class links(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('links are ready.')

    @commands.command()
    async def chem(self, ctx, arg):
        if arg == 'change':
            await ctx.send('enter the link:')
            user_link = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            add_link('chem', user_link.content)
            await ctx.send(f"added link {user_link.content}")
        else:

            await ctx.send('link , is :' , get_link('chem'))

    @commands.command()
    async def eng(self, ctx, arg):
        if arg == 'change':
            await ctx.send('enter the link:')
            user_link = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            add_link('eng', user_link.content)
            await ctx.send(f"added link {user_link.content}")
        else:
            await ctx.send(get_link('eng'))

    @commands.command()
    async def phy(self, ctx, *, arg):
        if arg == 'change':
            await ctx.send('enter the link:')
            user_link = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            add_link('phy', user_link.content)
            await ctx.send(f"added link {user_link.content}")
        else:
            await ctx.send(get_link('phy'))

    @commands.command()
    async def cs(self, ctx, *, arg):
        if arg == 'change':
            await ctx.send('enter the link:')
            user_link = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            add_link('cs', user_link.content)
            await ctx.send(f"added link {user_link.content}")
        else:
            await ctx.send(get_link('cs'))


def setup(bot: commands.Bot):
    bot.add_cog(links(bot))
