import json
import discord
from discord.ext import commands
import os
import time
import subprocess
import requests

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot_token = "DISCORD_BOT_TOKEN_HERE"


@bot.command()
async def hw0103(ctx, a, b, c, d, e, f):
    print('cp2 bot')
    cmd = subprocess.Popen("./discord_bot/discord_bot_cp2_0103", stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    a = a.encode()
    b = ' '.join(b[1:-1].split(','))
    c = ' '.join(c[1:-1].split(','))
    e = ' '.join(e[1:-1].split(','))
    f = ' '.join(f[1:-1].split(','))
    b = b.encode()
    c = c.encode()
    d = d.encode()
    e = e.encode()
    f = f.encode()
    g = '\n'.encode()
    cmd.stdin.write(a)
    cmd.stdin.write(g)
    cmd.stdin.write(d)
    cmd.stdin.write(g)
    cmd.stdin.write(b)
    cmd.stdin.write(g)
    cmd.stdin.write(c)
    cmd.stdin.write(g)
    cmd.stdin.write(e)
    cmd.stdin.write(g)
    cmd.stdin.write(f)
    cmd.stdin.write(g)

    cmd.stdin.close()

    await ctx.send(cmd.stdout.readline().decode())
    await ctx.send(cmd.stdout.readline().decode())
    await ctx.send(cmd.stdout.readline().decode())
    await ctx.send(cmd.stdout.readline().decode())

@bot.command()
async def hw0102(ctx, *, a:str):
    print('cp2 bot')
    cmd = subprocess.Popen("./discord_bot/discord_bot_cp2_0102", stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    b = ''
    while a[-1].isdigit():
        b += a[-1]
        a = a[:-1]
    g = '\n'.encode()
    b = b[::-1]
    print(a)
    print(b)
    cmd.stdin.write(a[:-1].encode())
    cmd.stdin.write(g)
    cmd.stdin.write(b.encode())

    cmd.stdin.close()

    await ctx.send(cmd.stdout.readline().decode())

@bot.command()
async def pi(ctx,cmd):
    if cmd == "temp":
        r = os.popen('vcgencmd measure_temp').readlines()
        for i in r:
                await ctx.send(i)

@bot.command()
async def hw0202(ctx):
    print('cp2 bot')
    attachment_url = ctx.message.attachments[0].url
    file_request = requests.get(attachment_url)
    # print(file_request)
    r = open("./discord_bot/hw0202input.txt", "w+")
    r.write(file_request.content.decode('utf-8'))
    r.close()
    os.system("./discord_bot/discord_bot_cp2_0202 <./discord_bot/0202cmd.txt> ./discord_bot/hw0202output.txt")
    await ctx.send(file=discord.File(r'./discord_bot/hw0202output.txt'))
    #os.system('rm ./discord_bot/hw0202output.txt')
    #os.system('rm ./discord_bot/hw0202input.txt')
    
@bot.command()
async def hw0204(ctx,cmd):
    print('cp2 bot')
    attachment_url = ctx.message.attachments[0].url
    file_request = requests.get(attachment_url)
    # print(file_request)
    r = open("./discord_bot/hw0204input.bmp", "w+")
    r.write(file_request.content.decode('utf-8'))
    r.close()
    gg = subprocess.Popen("./discord_bot/discord_bot_cp2_0102", stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    gg.stdin.write('hw0204input.bmp'.encode())
    gg.stdin.write(cmd.encode())
    gg.stdin.close()
    await ctx.send(file=discord.File(r'./discord_bot/hw0204output.bmp'))
    #os.system('rm ./discord_bot/hw0202output.txt')
    #os.system('rm ./discord_bot/hw0202input.txt')

bot.run(bot_token)
