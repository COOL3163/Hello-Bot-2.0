import discord
import os
import time as t
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
import numpy as np
import keep_alive


client = discord.Client()

client = commands.Bot(command_prefix = '!') 

@client.event
async def on_ready():
    print("bot online")
    print("AM PRO!!!!!")
    keep_alive.keep_alive()
    
    
@client.command(description = 'Bot latency')
async def ping(ctx):
  bot_latency = round(ctx.latency * 1000)
  await ctx.send("Pong!")
  await ctx.send(f'Latency is' + bot_latency + 'ms' )

@client.command(description = 'HELLO!')
async def hello(ctx):
  await ctx.send("Hello!")

@client.command(description = 'Alt command for hello')
async def hi(ctx):
  await ctx.send("Hello!")

@client.command(description = 'Catch a fish!')
async def fish(ctx):
  fishtype = 'salmon', 'cod', 'carp'
  fish = random.choice(fishtype)
  await ctx.channel.send('You caught a ' + fish + '!')

@client.command(description = 'Go hunting!')
async def hunt(ctx):
  huntanimal = 'deer', 'rabbit', 'duck', 'skunk', ''
  huntthing = random.choice(huntanimal)
  await ctx.channel.send('You caught a ' + huntthing + '!' )

@client.command()
async def ampro(ctx):
  await ctx.channel.send('am pro')
  await ctx.channel.send('what a noob')
@client.command(description = 'Try flipping heads')
async def flipheads(ctx):
  flipchanceheads = random()
  if flipchanceheads > 0.5:
    await ctx.channel.send("HEADS! You won!")
    
  else:
    await ctx.channel.send("TAILS! You lost!")

@client.command(description = 'Try flipping tails')
async def fliptails(ctx):
  flipchancetails = random()
  if flipchancetails > 0.5:
    await ctx.channel.send("TAILS! You won!")
    
  else:
    await ctx.channel.send("HEADS! You lost!")

@client.command(description = 'COOL3163 is COOL!!!')
async def cool(ctx):
  await ctx.channel.send(file=discord.File('COOL3163.png'))
  await ctx.channel.send("COOL3163 is cool and pro")

@client.command(description = 'dm someone')
async def dm(ctx, user: discord.User = None, *, value = None):
  if user == ctx.message.author:
    await ctx.send("You can't DM yourself noob")
  else:
    await ctx.message.delete()
    if user == None:
      await ctx.send(f'**{ctx.message.author},** Please mention somebody to DM.')
    else:
      if value == None:
        await ctx.send(f'**{ctx.message.author},** Please send a message to DM.')
      else:
        await user.send(value)
    

@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("Kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
        kick_message = f'You you were KICKED from {ctx.message.guild.name} think about why'
        await member.send(kick_message)
    except:
        await ctx.send("bot does not have the kick members permission!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

#The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True, administrator = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send("Banned "+member.mention)
    ban_message = f'You you were BANNED from {ctx.message.guild.name} think about why'
    await member.send(ban_message)

#The below code unbans player.
@client.command()
@commands.has_permissions(ban_members = True, administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


client.run("ODEzMzc2NzA2MTYxMjc4OTg2.YDOaFg.lgO5ZYFb8zq-6GgI9yKAzgv4Bik") 
