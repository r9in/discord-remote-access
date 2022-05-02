import discord
from discord.ext import commands
from subprocess import Popen, PIPE

token = "TOKEN-HERE"
owner = YOURIDHERE
channel = CHANNELIDHERE

client = commands.Bot(command_prefix="", case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    print('logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

@client.event
async def on_message(message):
    if message.author.id == owner and message.channel.id == channel:
        if 'cd' in message.content:
            await message.channel.send(send_terminal(message.content + '&& echo DIRECTORY: **$(pwd)** && ls'))
        else:
            await message.channel.send(send_terminal(message.content))

def send_terminal(message):
    pipe = Popen(message, shell=True,encoding="utf8", stdout=PIPE).stdout
    output = pipe.read()
    return output

try:
    client.run(token)
except KeyboardInterrupt:
    pass
