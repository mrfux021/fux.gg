from discord.ext import commands
import discord

class RP(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def registrar(self, ctx, nome, idade:int):

        cargo = discord.utils.get(ctx.guild.roles, name="Cidadão")

        if cargo:
            await ctx.author.add_roles(cargo)

        await ctx.send(
            f"✅ Registro criado!\nNome: {nome}\nIdade: {idade}"
        )

def setup(bot):
    bot.add_cog(RP(bot))