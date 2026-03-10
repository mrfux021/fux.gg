from discord.ext import commands
import discord

class RP(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def registrar(self, ctx, nome, idade:int):

        role = discord.utils.get(ctx.guild.roles, name="Cidadão")

        if role:
            await ctx.author.add_roles(role)

        await ctx.send(f"Registro criado: {nome}, {idade} anos.")

async def setup(bot):
    await bot.add_cog(RP(bot))
