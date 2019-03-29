worker: python filename.py
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import discord

BOT_PREFIX = ("-")
TOKEN =('NTM2Mzg1OTY2NDQxNjI3NjQ4.D36nvw.66l6eB4GeXYgtLYyqlBugbBMLaA')
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
   
@client.command()
async def about(*args) :
 await client.say("```ABOUT | Myde is a fully customizable discord bot for your discord server that features a simple and intuitive web dashboard. It brings many features such as moderation, anti-spam/auto-moderation, role management, custom commands, music bot, and much more that will greatly simplify managing your server and provide many useful and interesting features for your members. MOD COMMANDS | Ban, Kick, Warn, Temp Ban, Mute | COMMANDS | Ping```")
 
@client.command()
async def meme(**args) :
	await client.say("https://i.kym-cdn.com/photos/images/newsfeed/000/724/681/8c7.gif")

@client.event
async def on_message(message):
    if message.content.startswith('-about'):
        embed = discord.Embed(title="ABOUT", description="Myde is a fully customizable discord bot for your discord server that features a simple and intuitive web dashboard. It brings many features such as moderation, anti-spam/auto-moderation, role management, custom commands, music bot, and much more that will greatly simplify managing your server and provide many useful and interesting features for your members", color=0x000000)
        embed.add_field(name="Mod Commands", value="none", inline=False)
        embed.add_field(name="Commands", value="square ping 8ball meme bitcoin", inline=False)
        await client.send_message(message.channel, embed=embed)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="-about"))
    print("Logged in as " + client.user.name)
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
       
client.loop.create_task(list_servers( ))
client.run('NTM2Mzg1OTY2NDQxNjI3NjQ4.D36nvw.66l6eB4GeXYgtLYyqlBugbBMLaA')
