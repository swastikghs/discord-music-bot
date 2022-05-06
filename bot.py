import discord
from discord.ext import commands
import os

#import all of the cogs
from complex_cog import Music

bot = commands.Bot(command_prefix='k!')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(Music(bot))


#start the bot with our token
bot.run("OTUwNDIwNzM3NTczOTMzMDU3.G2tLGi.tuxjmju4mnC-mw0XlEwG91INlvP27Uh64v4krM")