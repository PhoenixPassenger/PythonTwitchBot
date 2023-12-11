from dotenv import load_dotenv
import os
from twitchio.ext import commands

# Load environment variables from .env file
load_dotenv()
ircToken = os.environ.get("irc_token")
clientId = os.environ.get("client_id")
prefix = os.environ.get("prefix")
initialChannels = os.environ.get("initial_channels")
print(f"Initial Channels: {initialChannels}")


bot = commands.Bot(
    token = ircToken,
    client_id =  clientId,
    prefix = prefix,
    initial_channels = [initialChannels]
)
@bot.event
async def event_ready():
    print('Estamos online')
@bot. command (name='bão?')
async def horario(ctx):
    await ctx.channel.send(f'Oba, {ctx.author.name} bão?')

bot.run()