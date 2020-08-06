import discord
from discord.ext import commands
import random
import time

bingo_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


async def display_board_to_dms(ctx, whole_board, player_no, players):

    for i in range(player_no):
        for row in range(0, 5):
            printing = []
            for coloumn in range(0, 5):
                if whole_board[i][row][coloumn][1] == 1:
                    printing.append("/ ")

                else:
                    a = whole_board[i][row][coloumn][0]
                    if len(str(a)) == 1:
                        printing.append(str(a) + " ")
                    else:
                        printing.append(a)
            full_print = ""
            for x in printing:
                full_print = full_print + str(x)
                full_print = full_print + "   "
            await players[i].send(full_print)


def board_gen():
    board = [[[[], []], [[], []], [[], []], [[], []], [[], []]], [[[], []], [[], []], [[], []], [[], []], [[], []]],
             [[[], []], [[], []], [[], []], [[], []], [[], []]], [[[], []], [[], []], [[], []], [[], []], [[], []]],
             [[[], []], [[], []], [[], []], [[], []], [[], []]]]
    for row in range(0, 5):
        for coloumn in range(0, 5):
            board[row][coloumn][1] = 0
    no = 0
    order = 0
    random.shuffle(bingo_numbers)
    for row in range(0, 5):
        for coloumn in range(0, 5):
            board[row][coloumn][no] = bingo_numbers[order]
            order = order + 1
    print(board)
    return board


def cross_no(number, number_of_boards, boards):
    for row in range(0, 5):
        for coloumn in range(0, 5):
            for board_no in range(0, number_of_boards):
                if boards[board_no][row][coloumn][0] == number:
                    boards[board_no][row][coloumn][1] = 1


def print_board(board):
    for row in board:
        for coloumn in row:
            print(coloumn[0], end='    ')
        print()


async def dm_users(ctx, users, whole_board):
    for i in range(len(whole_board)):
        await users[i].send(whole_board[i])


class bingo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('bingo machine is ready.')

    @commands.command()
    async def start_bingo(self, ctx, player_no):

        whole_board = []
        player_no = int(player_no)
        for i in range(player_no):
            sub_board = board_gen()
            whole_board.append(sub_board)

        def check1(m):
            return m.content == 'JOIN' and m.channel == ctx.channel

        game = True
        run = True
        a = 0
        players = []
        while run:
            msg = await self.bot.wait_for('message', check=check1)
            time.sleep(1)
            a = a + 1
            if a == player_no:
                run = False
            players.append(msg.author)
        no_chosen = None
        chance = 0
        # main game loop
        while game:
            no_chosen = await self.bot.wait_for('message', check=lambda message: message.author == players[chance])
            chance = chance + 1

            cross_no(int(no_chosen.content), player_no, whole_board)
            await display_board_to_dms(ctx, whole_board, player_no, players)
            game = False
        print(whole_board)
        await ctx.send(players)


def setup(Bot):
    Bot.add_cog(bingo(Bot))
