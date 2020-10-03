import os

import discord
import asynchio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def findtime(timespan):
    temp = ""
    time = 0
    for i in timespan:
        if(i.isnumeric() == True):
            temp += i
            continue
        if(i == "h"):
            time += int(temp)*3600
            temp = ""
            continue
        if(i == "m"):
            time += int(temp)*60
            temp = ""
            continue
        if(i == "s"):
            time += int(temp)
            temp = ""
            continue
    return time
async def startTR(dic, channel, guild):
    content1 = ""
    for i in dic:
        content1 += str(i) + " -=> " + str(int((dic[i] - datetime.datetime.utcnow()).seconds / 60)) + "m" + str(int((dic[i] - datetime.datetime.utcnow()).seconds % 60)) + "s" + "\n"
    id = await channel.send("```" + content1 + "```")
    do :
        content1 = ""
        needpop = 0
        await asyncio.sleep(1)
        for i in dic:
            time = int((dic[i] - datetime.datetime.utcnow()).seconds)
            content1 += str(i) + " => " + str(int(time / 60)) + "m" + str(int(time%60)) + "s" + "\n"
            if(dic[i] <= datetime.datetime.utcnow() + datetime.timedelta(seconds=2)):
                needpop = i
        if(needpop != 0):
            dic.pop(needpop)
        if(content1 == ""):
            try:
                await id.edit(content=" Utilise ``>tr t`` pour activer le timer ")
                return 0
            except discord.NotFound:
                return 0
        try:
            await id.edit(content="```" + content1 + "```")
        except discord.NotFound:
            return 0
@client.event
async def on_message(message):
    if (message.author.id == 280726849842053120 and message.content.find("Shard 0") != -1 and message.content.find("Shard 20") != -1):
        lines = message.content.split("\n")
        dic = {}
        for i in range(len(lines) - 7, len(lines)):
            stuff = lines[i].split(" : ")
            dic[stuff[0][-2:]] = message.created_at + datetime.timedelta(seconds=findtime(stuff[1]) - 1)
        await startTR(dic, message.channel, message.guild)
        return 0
    client.run(NzU5ODA3NTUzOTY5MzI0MTEz.X3C37Q.hofBuUp0sW589Ul6sTjxh1UAXYc-2VT9XmXITs)
