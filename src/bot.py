import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Estamos listos doc {0.user}'.format(client))


@client.event
async def on_menssage(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(channel, 'Hello!')



client.run('NzE1OTM4NzAyMTMxNzI0Mjg4.Xt-gmg.TbvM-Od5RoBC5L9AaBKV_StigUU')

