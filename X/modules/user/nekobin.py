#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Credits: Athfan Khaleel
# Copyright (C) https://github.com/athphane/userbot
#REMAKE BY NOBITA XD AND TRYTOLIVEALONE 


import asyncio

import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from .help import *


@Client.on_message(
    filters.command(["neko", "nekobin", "bin", "paste"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def paste(bot: Client, message: Message):
    text = message.reply_to_message.text
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    "https://nekobin.com/api/documents", json={"content": text}, timeout=3
            ) as response:
                key = (await response.json())["result"]["key"]
    except Exception:
        await message.edit_text("`Pasting failed`")
        await asyncio.sleep(2)
        await message.delete()
        return
    else:
        url = f"https://nekobin.com/{key}"
        reply_text = f"Nekofied to **Nekobin** : {url}"
        delete = (
            True
            if len(message.command) > 1
               and message.command[1] in ["d", "del"]
               and message.reply_to_message.from_user.is_self
            else False
        )
        if delete:
            await asyncio.gather(
                bot.send_message(
                    message.chat.id, reply_text, disable_web_page_preview=True
                ),
                message.reply_to_message.delete(),
                message.delete(),
            )
        else:
            await message.edit_text(
                reply_text,
                disable_web_page_preview=True,
            )


add_command_help(
    "•─╼⃝𖠁 ᴘᴀꜱᴛᴇ",
    [
        [
            ".paste `or` .bin `or` .neko `or` .nekobin",
            "Cʀᴇᴀᴛᴇ ᴀ Nᴇᴋᴏʙɪɴ ᴘᴀꜱᴛᴇ ᴜꜱɪɴɢ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ.",
        ],
    ],
      )
