import discord
import asyncio
import requests
import json

client = discord.Client()
user = 'Vh1Xu47ThdGBdHZi'
key = '5BSi6mgVNV5cKzMV3uQHHz5fPZ0z40S2'


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='SickBot V0.3'))

@client.event
async def on_message(message):
    if message.channel = 'sick-bot-talk':
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'sickbot', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, message.author.mention+' '+r['response'])

print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'sickbot'})
client.run('NDMyNjMwMjMzNjUzNDQ0NjE4.Daw34g.rEBW--cS61N-o4XDNITdlIjwoTI')
