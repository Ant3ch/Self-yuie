import time
import discord
from colorings import *
import requests
from tools import tools
import asyncio
from commands.__importer__ import *


class Commander:

    def __init__(self, prefixes, config):
        self.prefixes = prefixes
        self.config = config
        self.colorings = colorings
        self.tools = tools

    async def __analyse__(self, infos):
        """Check prefix in message from user"""
        return await analyse(self, infos)

    def __argAnalyse__(self, infos: str, base_values: list[str, str], aliases: [str, str] = None) -> dict:
        return argsAnalyse(self, infos, base_values, aliases)

    async def pong(self, infos, args):
        """ping pong sends the ping..."""""
        return await pong(self, infos, args)

    async def embeding(self, infos, args):
        """Command to do really cool embed!!"""
        return await embeding(self, infos, args)

    async def connect(self,infos,args):
        pass

    async def joke(self,infos,args):

           joke = requests.get('https://v2.jokeapi.dev/joke/Any?lang=fr').json()
           setup = joke['setup']
           answ = joke['delivery']
           await self.fake_typing(infos['channel'],1)
           await infos['channel'].send(setup)
           await self.fake_typing(infos['channel'], 3.8)
           await infos['channel'].send(answ)


    async def fake_typing(self,channel,time):
        async with channel.typing():
            await asyncio.sleep(time)
    COMMANDS = {
        'ping': pong,
        'embed': embeding,
        'connect':connect,
        'joke':joke,
    }
