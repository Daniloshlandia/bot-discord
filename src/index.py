import discord 
from discord.ext import commands 
import datetime
from urllib import parse, request
import re 


bot = commands.Bot(command_prefix='>', description="This is bot dash")

#welcome alert still dev 
@bot.command()
async def welcome_Alert(ctx):
    await ctx.send(bool)


# image command say hello done.
@bot.command()
async def hola(ctx):
    await ctx.send('Hello', file=discord.File('hello-yui.png', 'hello-yui.png'))

@bot.command()
async def sum(ctx,numOne: int,numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="dash info about this sever",
    timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?'+ query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11}', html_content.read().decode())
    print(search_results)
    # Encuentra el primer resultado del loop de busqueda tomando encuenta los parametros
    await ctx.send('https://www.youtube.com/watch?v=' + search_result[0])


# Events from api of discord ## issue 002 arreglar error sobre search_results regular expresions

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="dash esta online",
    url="https://www.twitch.tv/accountname"))
    print("Now online on twich")

bot.run('secret code')


