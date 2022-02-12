import discord
from discord.ext import commands

from covid19 import Covid19
from weather import Weather
from coin import Coin


class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            print(f"{message.guild}/{message.channel}/{message.author.name}>{message.content}")
            if message.embeds:
                print(message.embeds[0].to_dict())
            
    @commands.command(name='covid19')
    async def _covid19(self, ctx: commands.Context):
        async with ctx.typing():
            covid19 = Covid19()
            covid19.getData()
            embed = covid19.create_embed()
            await ctx.send(embed=embed)

    @commands.command(name='weather')
    async def _weather(self, ctx: commands.Context):
        async with ctx.typing():
            weather = Weather()
            weather.getData()
            embed = weather.create_embed()
            await ctx.send(embed=embed)

    @commands.command(name='coin')
    async def _coin(self, ctx: commands.Context, base: str, quote: str):
        async with ctx.typing():
            coin = Coin()
            coin.getData(base, quote)
            embed = coin.create_embed()
            await ctx.send(embed=embed)
