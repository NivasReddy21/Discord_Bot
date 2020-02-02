import discord
from discord.ext import commands
import random
import pytz
from pytz import all_timezones
import wikipediaapi
import requests, json
import os

class Main(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        
        print('Bot is online')
    
    @commands.Command(aliases = ['hey', 'hello', 'hey there!', 'wassup', 'hi'])
    async def greeting(self, ctx):
        
        replies = ['hey', 'hello', 'hey there!!!', 'hola!', 'wassup.....']
        await ctx.send(f'{random.choice(replies) }')        

    

def setup(client):
    client.add_cog(Main(client))