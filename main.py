from tokenize import Number
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".", self_bot=True, help_command=None)
token = "YOUR_TOKEN_HERE"

@client.command()
async def delete(ctx: commands.context.Context, arg):
    try: 
        toDelete = int(arg)
        channel: discord.DMChannel = ctx.channel
        count = 0
        async for message in channel.history():
            if message.author == client.user:
                count += 1
                if count > toDelete:
                    break
                await message.delete()
    except:
        ctx.send('Invalid number argument.')

    

client.run(token, bot=False)
