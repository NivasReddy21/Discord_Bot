import discord
from discord.ext import commands
import random
import pytz
from pytz import all_timezones
import wikipediaapi

from datetime import datetime

TOKEN = 'NjcxMDAwNTY4MzQ0NDc3Njk3.Xi7WEg.IugT8TYV4dSG_M31V1V9x3F5PN4'
# GUILD = 'bot_testing'

client = commands.Bot(command_prefix = '@')

@client.command(aliases=['hey', 'hello', 'hi', 'wassup', 'hey there'])
async def greeting(ctx):

    replies = ['hey', 'hello', 'hey there!!!', 'hola!', 'wassup.....']
    await ctx.send(f'{random.choice(replies) }')


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
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S") 
    # await ctx.send(f'{question}\n {current_time}')
    time_zone = pytz.timezone(question) 
    datetime_tz = datetime.now(time_zone)
    await ctx.send(f'Time at {question} is {datetime_tz}')

@client.command()
async def whois(ctx, *, question):
    
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(question)
    page_summary = page.summary
    await ctx.send(f'{page_summary[0:1000]}')




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


client.run(TOKEN)



