# CONFIG
token = "" # Just google how to get discord token.
prefix = "~"


# Import the needed libs.
import asyncio
from discord.ext import commands
import discord
import random
import re

print("Loading..")

words = ['pog', 'message', 'sample', 'test', 'discord', 'minecraft', 'bot', 'mee6', 'poggr', 'poggers', 'troll', 'nootnoot', 'this is a message', 'give me free nitro', 'ignore me please', 'why are you reading this', 'made you look', 'hi', 'hello', 'this is another random message', 'this is a message with no context', 'this message serves no purpose', 'hi audit logs its me', 'its me', 'isnt this entertaining?', 'this message will self-destruct', 'this message will also self-destruct', 'this message will go poof', 'poof', 'my password is....', '#auditlog spam', 'dont mind me', 'this is a string', 'this is a bunch of garbage', 'this message is for mee6 levels', 'this message is for experience', '#freeexperience', 'xp', 'dont mind me... im collecting xp', 'just chilling', 'this is message number 999999999999999999999', 'm e s s a g e', 'hello, this is a message which wont last long', 'insert message here', 'insert creative quote here', 'insert useless message here', 'dont ask', 'no need to question', 'insert creative message here', 'typo', 'spam', 'this is not spam', 'give me nitro', 'look at me xp farming', 'this randomizer is cool', 'hello there', 'i see you', 'peek a boo', 'boo!']

#   Count bot config
counting_channel = 0000000000000000 #	Channel for auto counter
enabled = False
last_number = 0

# Declare the bot, pass it a prefix and let it know to only listen to itself.

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot Loaded.")

@bot.command()
async def farm(ctx, amount=10):
    await ctx.message.delete()
    for r in range(amount):
        message = await ctx.send(random.choice(words))
        await asyncio.sleep(random.uniform(0,3))
        await message.delete()
        await asyncio.sleep(random.uniform(61,65))

@bot.command()
async def count(ctx, option='on'):
    global enabled
    if option.lower() == 'on':
        await ctx.send('Counting Enabled..')
        enabled = True
    elif option.lower() == 'off':
        await ctx.send('Counting Disabled..')
        enabled = False
    elif option.lower() == 'reset':
        global last_number
        last_number = 0
        await ctx.send('Count variable reset.')
    else:
        await ctx.send('Counting Disabled..')

@bot.event
async def on_message(message):
    global last_number
    global enabled
    if bot.user.id != message.author.id and message.channel.id == int(counting_channel) and enabled:
        channel = bot.get_channel(int(counting_channel))
        try:
            number = int(re.search(r"(\d*)", message.content).group(0))
        except:
            pass
        else:
            if number == last_number + 1:
                last_number = number + 1
                print(f"Sending -> {number+1}")
                asyncio.sleep(random.uniform(0, 2))
                await channel.send(number+1)
            elif last_number == 0:
                last_number = number + 1
                print(f"Sending -> {number+1}")
                await asyncio.sleep(random.uniform(0, 2))
                await channel.send(number+1)
    await bot.process_commands(message)





bot.run(token, bot=False)  # Starts the bot by passing it a token and telling it it isn't really a bot. 
