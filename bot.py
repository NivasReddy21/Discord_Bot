import discord
from discord.ext import commands
import random
import pytz
from pytz import all_timezones
import wikipediaapi
import requests, json
# import os

from datetime import datetime

base_url = "http://api.openweathermap.org/data/2.5/weather?"


client = commands.Bot(command_prefix = '@')

# id = '669759094290120735'


# @client.command()

# async def load(ctx, extension):
    
#     client.load_extension(f'cogs.{extension}')

# @client.command()

# async def unload(ctx, extension):
    
#     client.unload_extension(f'cogs.{extension}')


# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')


@client.command(aliases=['hey', 'hello', 'hi', 'wassup', 'hey there'])
async def greeting(ctx):
    member = discord.User
    replies = ['hey', 'hello', 'hey there!!!', 'hola!', 'wassup.....']
    await ctx.send(f'{random.choice(replies)} {ctx.message.author.mention}')



@client.command(aliases=['8ball', 'answer me', 'predict'])
async def _8ball(ctx, *, question):
    
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt',
    'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely',
    'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 
    'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it',
    'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    
    
    await ctx.send(f'Question: {question}\n Answer: {random.choice(answers)}')    


@client.command('time')
async def date_time(ctx, *, question):

    time_zone = pytz.timezone(question) 
    datetime_tz = datetime.now(time_zone)
    await ctx.send(f'Time at {question} is {datetime_tz}')


@client.command(aliases=['whois', 'whatis'])
async def _whois(ctx, *, question):
    
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(question)
    page_summary = page.summary
    await ctx.send(f'{page_summary[0:1000]}')


@client.command()
async def weather(ctx, *, question):

    city_name = question
    complete_url = base_url + "appid=" + APIKEY + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json() 

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        temperature = round(current_temperature - 273)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        await ctx.send(f'Temperature: = {temperature} \n atmospheric pressure = {current_pressure} \n humidity = {current_humidity} \n description = {weather_description}')
        
@client.event
async def on_message(message):

    msg = message.content.lower()

    if(message.author != client.user):

        if ((msg.startswith('hi') or msg.startswith('hello') or msg.startswith('wassup') or msg.startswith('hey'))) :
            replies = ['hey', 'hello', 'hey there!!!', 'hola!', 'wassup.....']
            await message.channel.send(f'{random.choice(replies)} {message.author.mention}')   # never directly do message.channel.send() as it will go to infinity loop
        
        elif ((msg.startswith('gn') or 'good night' in msg)):
            await message.channel.send(f"Good Night,  {message.author.mention}" )

        elif ('bot' in msg):
            
            await message.channel.send("Hey {}! Did U jst call me?".format(message.author.mention))
        
        elif ('bye' in msg):
            await message.channel.send('Bye, see u soon............ {}'.format(message.author.mention))
        
        elif ('valar morghulis' in msg):

            await message.channel.send('Valar Dohaeris `Arya Stark`')

        await client.process_commands(message)

@client.command(aliases = ['pic'])
async def picture(message):
    imgs = ['img.jpg', 'Imgs.jpg', 'imgsss.jpg', 'pic.jpg']
    await message.channel.send(file=discord.File(random.choice(imgs)))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


client.run(TOKEN)



