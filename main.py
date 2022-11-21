import os
import discord
from commands.commander import *
from colorings import *
from tools import *

config = {}


def load():
    global config
    for files in os.listdir("./config/"):
        with open(f"./config/{files}") as file:
            config[files.split('.')[0]] = file.read()


load()


def readconf(key, text: str):
    global config
    dico = {}
    d = text.split("\n")
    while ("" in d):
        d.remove("")
    for val in d:
        if val[0] == "#":
            d.remove(val)

    for val in d:
        val = val.replace(' ', '').split("=")
        dico[val[0]] = eval(val[1])

    config[key] = dico


# config to read

# share file
readconf("share", config['share'])

if not config['share']['selfing']:
    config['share']['people_id'].append(int(config['id']))


class MyClient(discord.Client):

    async def on_ready(self):
        user = await self.fetch_user(int(config["id"]))

        if not config['share']['selfing'] and not config['share']['noOnlineMessage']:
            try:
                await user.send(delete_after=10, content=tools.embed("Online", "the bot is alive ! ", color=(0, 255, 0),
                                                                     redirect_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
            except discord.Forbidden:
                await user.send_friend_request()
        else:
            config['share']['people_id'].append(int(self.user.id))
            config['id'] = self.user.id

        print(colorings.GREEN + 'logged into', colorings.MAGENTA + str(self.user) + colorings.RESET)

    async def on_message(self, message: discord.Message):
        if message.author.id != self.user.id and config['share']['selfing']:
            return

        if not config['share']['public']:
            if message.author.id not in config['share']['people_id']:
                    return

        author = message.author
        content = message.content
        channel = message.channel
        id_ = message.id
        guild = message.guild
        infos = {"content": content, "author": author, "channel": channel, "bot": self, 'id': id_, 'guild': guild,
                 'latency': self.latency,'message':message, }
        await commander.__analyse__(infos)


commander = Commander(config.get('prefix'), config)

client = MyClient()
client.run(config['token'])
