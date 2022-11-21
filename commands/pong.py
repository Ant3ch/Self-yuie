import time
from colorings import *


async def pong(self, infos, args):
    before = time.monotonic()
    msg = await infos["channel"].send('pong')
    ping = (time.monotonic() - before) * 1000
    await msg.edit(content=f'your ping is: {round(ping, 2)}ms')
    print(colorings.THISTLE + colorings.color(f"ping test : &b&{round(ping, 2)}ms") + colorings.RESET)
