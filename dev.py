#Copyright ©️ 2022 Dev Arora. All Rights Reserved.
import os
import re
import pytz
import asyncio
import datetime

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from config import *

app = Client(
    name = "devbotz",
    api_id = API_ID,
    api_hash = API_HASH,
    session_string = SESSION
)

async def main_devchecker():
    async with app:
            while True:
                print("Checking...")
                xxx_hehe = f"<b>**🏷 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {(await app.get_chat(CHANNEL_ID)).title} ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ**</b>\n\n 📈 | <b><u>ʀᴇᴀʟ ᴛɪᴍᴇ ʙᴏᴛ's sᴛᴀᴛᴜs</u> 🍂</b>"
                for bot in BOT_LIST:
                    await asyncio.sleep(7)
                    try:
                        bot_info = await app.get_users(bot)
                    except Exception:
                        bot_info = bot

                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(15)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_hehe += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**"
                            await app.send_message(int(BOT_ADMIN_ID), f"**ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴀ ʜᴀɪ 😡\n[{bot_info.first_name}](tg://user?id={bot_info.id}) ᴏғғ ʜᴀɪ. ᴀᴄᴄʜᴀ ʜᴜᴀ ᴅᴇᴋʜ ʟɪʏᴀ ᴍᴀɪɴᴇ.**")
                            await app.read_chat_history(bot)
                        else:
                            xxx_hehe += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**"
                            await app.read_chat_history(bot)
                            await app.send_message(GRP_ID, "ALL YOUR BOTS ARE WORKING FINE")
                    except FloodWait as e:
                        ttm = re.findall("\d{0,5}", str(e))
                        await asyncio.sleep(int(ttm))
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%I:%M %p")
                daate = time.strftime(f"%d %b %Y")
                xxx_hehe += f"\n\n☁<u>ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ:</u>\n**ᴅᴀᴛᴇ: {daate}**\n**ᴛɪᴍᴇ: {last_update}**\n\n♻️ ʀᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴡɪᴛʜɪɴ 𝟷𝟶 ᴍɪɴᴜᴛᴇs.\n\n<b>**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{(await app.get_chat(CHANNEL_ID)).username} ๏**</b>"
                await app.edit_message_text(CHANNEL_ID, MESSAGE_ID, xxx_hehe)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(540)
                        
app.run(main_devchecker())

#Copyright ©️ 2022 Dev Arora. All Rights Reserved.