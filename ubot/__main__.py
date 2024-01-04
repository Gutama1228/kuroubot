import asyncio
import os
import sys

from asyncio import get_event_loop_policy

from atexit import register
from pyrogram import idle
from pyrogram.errors import RPCError

from ubot import *
        

async def loader_user(_ubot, user_id):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=90)
        await ubot_.join_chat("kynansupport")
    except RPCError:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    except:
        pass


async def main():
    userbots = await get_userbots()
    #tasks = [start_ubot(int(_ubot["name"]), _ubot) for _ubot in userbots]
    #await asyncio.gather(*tasks)
    for _ubot in userbots:
        await loader_user(_ubot, int(_ubot["name"]))
    
    await bot.start()
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())


if __name__ == "__main__":
    LOOP = asyncio.get_event_loop_policy().get_event_loop()
    LOOP.run_until_complete(main())
