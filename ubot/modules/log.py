import os

import wget

from .. import *

__MODULE__ = "ʟᴏɢs"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀɴɢ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ʟᴏɢs</code> (ᴏɴ/ᴏғғ)
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴄʜᴀɴɴᴇʟ ʟᴏɢs
"""

async def create_logs(client):
    logs = await client.create_supergroup(f"Kuro-Logs")
    url = wget.download("https://telegra.ph//file/90f9f55494a6380c880ae.jpg")
    photo_video = {"video": url} if url.endswith(".mp4") else {"photo": url}
    await client.set_chat_photo(
        logs.id,
        **photo_video,
    )
    await client.send_message(
        logs.id, "<b>✅ ʟᴏɢs ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ\nᴊᴀɴɢᴀɴ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ɪɴɪ ʏᴀ"
    )
    await set_vars(client.me.id, "ID_LOGS", logs.id)
    os.remove(url)


def NO_CMD_UBOT(results, group):
    def wrapper(func):
        query_mapping = {
            "PRIVATE_LOGS": (
                filters.private
                & filters.incoming
                & ~filters.me
                & ~filters.bot
                & ~filters.service
            ),
            "GROUP_LOGS": (
                filters.group & filters.incoming & filters.mentioned & ~filters.bot
            ),
        }
        results_query = query_mapping[results]

        @ubot.on_message(results_query)
        async def wrapped_func(client, message):
            await func(client, message)

        return wrapped_func

    return wrapper


async def send_log(client, chat_id, message, message_text, msg):
    try:
        await client.send_message(chat_id, message_text, disable_web_page_preview=True)
        await message.forward(chat_id)
    except Exception:
        await client.send_message(chat_id, f"{msg} ERROR: GAGAL MENERUSKAN PESAN")


@NO_CMD_UBOT("PRIVATE_LOGS", 2)
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ᴘʀɪᴠᴀᴛᴇ"
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        message_link = (
            f"tg://openmessage?user_id={message.from_user.id}&message_id={message.id}"
        )
        message_text = f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> <code>{type}</code>
    <b>•> ʟɪɴᴋ ᴘᴇsᴀɴ:</b> [ᴋʟɪᴋ ᴅɪsɪɴɪ]({message_link})
    
<b>⤵️ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘеsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ: {user_link}</b>
"""
        await send_log(client, int(logs), message, message_text, "LOGS_PRIVATE")


@NO_CMD_UBOT("GROUP_LOGS", 3)
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ɢʀᴏᴜᴘ"
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        message_link = message.link
        message_text = f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> <code>{type}</code>
    <b>•> ʟɪɴᴋ ᴘᴇsᴀɴ:</b> [ᴋʟɪᴋ ᴅɪsɪɴɪ]({message_link})
    
<b>⤵️ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘеsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ: {user_link}</b>
"""
        await send_log(client, int(logs), message, message_text, "LOGS_GROUP")


@PY.UBOT("logs")
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "ʜᴀʀᴀᴘ ʙᴀᴄᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴɴʏᴀ."
        )

    query = {"on": True, "off": False, "none": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply("ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'.")

    value = query[command]

    vars = await get_vars(client.me.id, "ID_LOGS")

    if not vars:
        await create_logs(client)

    if command == "none" and vars:
        await client.delete_channel(vars)
        await set_vars(client.me.id, "ID_LOGS", value)

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(
        f"<b>✅ <code>LOGS</code> ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ:</b> <code>{value}</code>"
    )
