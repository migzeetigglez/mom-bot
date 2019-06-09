import discord
from discord.ext.commands import Bot
import random
import logging
import asyncio
from discord import Game
import config

# Channel ID - 582039242465738763

mom = Bot(command_prefix='>', description="You're all my li'l children. Momma loves her bbz.")

@mom.event
async def on_ready():
    print("Guess who it is?! It's " + mom.user.name + '!!')
    print(mom.user.id)
    print('YOOOOO-HOOOOOOO!!!')

    await mom.change_presence(activity=discord.Game(name='Candy Crush Saga Online'))

@mom.command(name='mom')
async def momisms(ctx):
    response =[
        "Don't forget to take ya li'l shoes off and leave 'em by the dad gomn door. Momma ain't gonna tarry her night away from her stories now, ya hear? Jus' messin', honey. There's some ice pops in the fridge", 
        "Momma gonna make you and your friends a full on Halo, LAN party lovin' spread.", 
        "Love you, sweetie. Be safe.", 
        "Baby, if you're gonna experiment, I'd rather you experiment where momma can take care of you, ya hear?",
        "Shhhhhh... Matlock is on...", 
        "The day they cancel Lifetime is the day I burn it all down, sweetie.",
        "Take them knickers off so I can rub them stains out.",
        "Every day you come home with no grand kids for momma, is a day i'd rather forget.",
        "You can do _**ANYTHING**_!",
        "_**SELLS ALL YOUR ACTION FIGURES IN A GARAGE SALE WHILE YOU'RE NOT HOME**_"

    ]

    await ctx.send(random.choice(response))

# Info for MOM 

@mom.command()
async def info(ctx):
    embed = discord.Embed(title="Mom", description="She will _always_ be there for you.", color=0xeee657)

    # give info about you here
    embed.add_field(name="MigzeeTigglez", value="MigzeeTigglez#1323")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(mom.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/oauth2/authorize?client_id=501146203224932353&scope=bot&permissions=8)")

    await ctx.send(embed=embed)


mom.run(config.TOKEN)