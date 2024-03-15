__MODULE__ = "fun"
__HELP__ = """
 Bantuan Untuk Fake Admin
 
• Perintah : <code>{0}giben</code> [user_id/username/reply user]
• Penjelasan : Untuk fake global ban.

• Perintah : <code>{0}gimut</code> [user_id/username/reply user]
• Penjelasan : Untuk fake global mute.

• Perintah : <code>{0}gikik</code> [user_id/username/reply user]
• Penjelasan : Untuk fake global kick.

• Perintah : <code>{0}gikes</code> [user_id/username/reply user]
• Penjelasan : Untuk fake global broadcast.
"""


@PY.UBOT("giben")
@ubot.on_message(filters.user(DEVS) & filters.command("Cigiben", "") & ~filters.me)
async def _(client, message):
    await giben(client, message)

@PY.UBOT("gimut")
@ubot.on_message(filters.user(DEVS) & filters.command("Cigimut", "") & ~filters.me)
async def _(client, message):
    await gimut(client, message)

@PY.UBOT("gikik")
@ubot.on_message(filters.user(DEVS) & filters.command("Cigikik", "") & ~filters.me)
async def _(client, message):
    await gikik(client, message)

@PY.UBOT("gikes")
@ubot.on_message(filters.user(DEVS) & filters.command("Cigikes", "") & ~filters.me)
async def _(client, message):
    await gcast_cmd(client, message)
