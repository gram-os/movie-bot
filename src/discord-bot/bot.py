import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from src.imsdb import imsdb_fetch as imsdb
import os
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL = os.getenv("HOMAGE_TO_CINEMA_CHANNEL")

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    scheduled_movie_script.start()
    print("Alfred del Toro at your service.")

@bot.command(name="getScript", help="send script for a random movie")
async def return_random_movie_script_command(ctx):
    await send_random_movie_script(ctx.channel)

@tasks.loop(hours=24)
async def scheduled_movie_script():
    movieChannel = bot.get_channel(CHANNEL)
    await send_random_movie_script(movieChannel)

async def send_random_movie_script(channel: discord.TextChannel):
    try:
        movie_script = imsdb.getMovieScript()
        for line in movie_script:
                await channel.send(line)
                await asyncio.sleep(2)
    except imsdb.ScriptNotFoundException:
        print("Error fetching movie script!")
    except imsdb.MoviesNotFoundException:
        print("Movie not found!")

def runBot():
    bot.run(TOKEN)
