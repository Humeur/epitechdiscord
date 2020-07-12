import discord
import requests
import json
from discord.ext import commands

Client = commands.Bot(command_prefix="")

@Client.event
async def on_ready():
    print("EpitechBOT > Le bot de modération automatique d'Epitech est lancé !")

@Client.event
async def on_message(message):
    if len(message.attachments) > 0:
        r = requests.post("https://api.deepai.org/api/nsfw-detector",
        data={'image': message.attachments[0].url,
        },
        headers={'api-key': 'API_KEY_HERE'})
        r_json = r.json()
        nsfw_score = r_json['output']['nsfw_score']
        if nsfw_score > 0.7:
            await message.delete()
            print('EpitechBOT > NSFW message detected then deleted')

Client.run('TOKEN_HERE')
