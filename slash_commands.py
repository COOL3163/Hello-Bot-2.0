import discord
from discord import app_commands
from discord.ext import commands
import keep_alive
from replit import db
import random
from os import getenv

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
        keys = db.keys()
        print(keys)
        await bot.change_presence(activity=discord.Game(name="Spawning dandruff!"))

    except Exception as e:
        print(e)

    keep_alive.keep_alive()


@bot.tree.command(name="pro", description="COOL3163 is pro")
async def pro(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hey {interaction.user.mention}! COOL3163 is pro")


@bot.tree.command(name="say", description="Say something through the bot")
@app_commands.describe(thingtosay="What should I say?")
async def say(interaction: discord.Interaction, thingtosay: str):
    await interaction.response.send_message(
        f"{interaction.user.mention} said: '{thingtosay}'")


@bot.tree.command(name="shoot", description="Make BigMatt69 shoot")
async def shoot(interaction: discord.Interaction):
    num = random.randint(1, 1000)
    embed = None
    if num == 1000:
        swished = db["swished"]
        embed = discord.Embed(
            title="Bigmatt69 shoots. Does it go in?",
            description=
            f"Fuck yeah! He swishes the ball in and gets all the bitches in the world. He has swished the shot {swished} times so far.",
            color=0xFFFFFF)
        db["swished"] = swished + 1
    else:
        bricked = db["bricked"]
        messages = ["Fuck no. His entire team is disappointed and they lose the match as a result.", "He goes for the stepback full court shot and starts twerking on the court. He starts BMing the other team, just to miss the ball and lose the game. What a loser.", "He goes for a layup but he catches a glimpse hot chicks on the other side of the court. As a result, he misses the ball and goes off court due 'exhaustion'.", "2 seconds left. BigMatt69 steps back, and attempts the impossible: A buzzer beater stepback full court shot. However, when he releases the ball, the opponent's bigass hand blocks him back to Antartica. As a result, their team has lost the game. His teammates are mad at him for having a skill issue, and therefore kicked him from the team.", "With a mighty heave, BigMatt69 launched the basketball towards the hoop, but alas, it sailed wide, missing the target by a comical margin, much to the amusement of his teammates and spectators alike.", "Witnessing BigMatt69's attempt at a basketball shot was akin to witnessing a great cosmic event—an awe-inspiring display of sheer inaccuracy as the ball soared through the air, completely missing the hoop and landing with a resounding thud, leaving everyone in disbelief and questioning the laws of physics.", "BigMatt69's shot sailed through the air with high hopes, but alas, it missed the mark by a mile, flying over the backboard and into the waiting arms of the opposing team, leaving his teammates dumbfounded.", "With the precision of a seasoned professional, BigMatt69 released the ball, only for it to ricochet off the rim, bounce off the backboard, and ultimately land nowhere near the basket, leaving him scratching his head in disbelief.", "As BigMatt69 lined up his shot, the crowd held its breath in anticipation, only to witness the ball graze the rim, dance along the edge, teasingly circling the hoop, but ultimately deciding to defy gravity and fall short, much to the disappointment of his cheering squad.", "It seemed as though an invisible force field had taken hold of BigMatt69's shots, as time and time again, they were inexplicably drawn away from the hoop, like a magnetic attraction to everything but the net, leaving him to wonder if he was cursed or simply destined for unconventional shot placements."]
        embed = discord.Embed(
            title="Bigmatt69 shoots. Does it go in?",
            description=
            f"{random.choice(messages)} He has bricked the shot {bricked} times so far and his team is absolutely sick of his skill issues.", color = 0xFFFFF)
        db["bricked"] = bricked + 1
        #bro
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="spawn", description="Make suolemendao spawn a peice of dandruff/hair rice")
async def spawn(interaction: discord.Interaction):
    try:
        #dandruff += 1
        db["dandruff1"] = db["dandruff1"] + 1
        dandruff = db["dandruff1"]
        embed = discord.Embed(
            title="suolemendao has spawned one peice of dandruff!  <:suolemen:1085082951362023434>",
            description=f"{dandruff} piece(s) of dandruff have been spawned",
            color=0xFFFFFF)
        embed.set_author(name=interaction.user.display_name,
                         icon_url=interaction.user.avatar)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/971255324415782942/1180482185069858867/Screenshot_2023-12-01_at_7.20.28_PM.png?ex=657d94b5&is=656b1fb5&hm=9edd68cc35693ea8fd2a68723380870a33a2eeb61baa76e7b77560633228e55b&"
        )
        await interaction.response.send_message(embed=embed)
        # await interaction.response.send_message(f"One dandruff as been spawned by suolemendao\n {dandruff} pieces of dandruff have been spawned since the bot has started")
    except Exception as e:
        print(e)


bot.run(getenv("TOKEN"))
