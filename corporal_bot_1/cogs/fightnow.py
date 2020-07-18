import discord
from discord.ext import commands
import random


class fight(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('fight is ready.')

    @commands.command()
    async def fight(self, ctx):
        await ctx.send('fight')
        await ctx.send("enter p to punch \n enter d to defend \n enter e to end if you are too scared")
        a = 100
        b = 100
        while a > 0 and b > 0:
            bot_decision = random.randint(1, 2)
            if bot_decision == 1:
                randombot_attack = random.randint(1, 100)
                a = a - randombot_attack
                await ctx.send(f'You took {randombot_attack} damage!!')
            elif bot_decision == 2:
                randombot_defense = random.randint(1, 75)
                b = b + randombot_defense
                await ctx.send(f'Bot gained {randombot_defense} health!!')
            if a <= 0:
                await ctx.send(f'{ctx.author} TOOK THE L')
                return

            user_choice = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

            if user_choice and user_choice.content in ["p", "punch"]:
                random_attack = random.randint(1, 100)
                b = b - random_attack
                await ctx.send(f'you dealt {random_attack} damage!!')
            elif user_choice and user_choice.content in ["d", "defend"]:
                random_defense = random.randint(1, 75)
                a = a + random_defense
                await ctx.send(f'you gained {random_defense} health!!')
            else:
                await ctx.send('fight ended')
                return
        if a > 0 and b > 0:
            return
        else:
            if a <= 0:
                await ctx.send(f'{ctx.author} TOOK THE L')
            else:
                await ctx.send(f'{ctx.author} YOU WIN!!')


def setup(bot: commands.Bot):
    bot.add_cog(fight(bot))
