import os
import discord
from discord.ext import commands

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hi(ctx):
    await ctx.send("hi")


@bot.command()
async def react(ctx):
    msg = await ctx.send("hi")

    for emoji in ["❌", "❓", "👎"]:
        await msg.add_reaction(emoji)


bot.run(TOKEN)
