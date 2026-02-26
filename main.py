import discord 
from discord.ext import commands
import logging 
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if token is None:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
intents =discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("All done and running ")

@bot.command()
async def helloworld(ctx):
    await ctx.send(f"Hello {ctx.author.mention} Hope You Are Having A Wonderful Day!")

@bot.command()
async def website(ctx):
    await ctx.send(f"Hello {ctx.author.mention} You can visit out site at https://deerhack.deerwalk.edu.np/ ")

@bot.command()
async def helpme(ctx):
    await ctx.send(f"Here are a list of commands  !helloworld  !website !helpme")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def send(ctx,channel:discord.TextChannel,*,message:str ):
    if message:
        await channel.send(message)
    
    for attachment in ctx.message.attachments:
        await channel.send(file=await attachment.to_file())

    await ctx.message.add_reaction("✅")





bot.run(token,log_handler=handler,log_level=logging.DEBUG)

