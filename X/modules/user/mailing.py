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

# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de


#REMAKE BY : NOBITA XD AND TRYTOLIVEALONE

import asyncio
import os

from pyrogram import *
from pyrogram.types import *
from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from X import *

from .help import *


@Client.on_message(
    filters.command(["copy"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await edit_or_reply(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "Nyolongbang_bot"
    await client.unblock_user(bot)
    xnxx = await client.send_message(bot, link)
    await xnxx.delete()
    await asyncio.sleep(8)
    await Tm.delete()
    async for sosmed in client.search_messages(bot, limit=1):
        try:
            await sosmed.copy(
                message.chat.id,
                reply_to_message_id=message.id,
            )
        except Exception:
            await Tm.edit(
                "<b>Video not found please try again in a few moments</b>"
            )
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@Client.on_message(
    filters.command(["curi"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def pencuri(client, message):
    dia = message.reply_to_message
    me = client.me.id
    if not dia:
        await edit_or_reply(message, "`Please reply to the media.`")
    anjing = dia.caption or None
    await edit_or_reply(message, "`Processing...`")
    if dia.text:
        await dia.copy("me")
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    try:
        await client.send_message("me", "**Pap of the timer.**")
    except Exception as e:
        print(e)

  

add_command_help(
    "•─╼⃝𖠁 ᴍᴀʟɪɴɢ",
    [
        [
            "copy <ʟɪɴᴋ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟ.>",
            "Cʟᴏɴᴇ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ ᴍᴇᴅɪᴀ."],
        [   "curi <ʀᴇᴘʟʏ ᴍᴇꜱꜱᴀɢᴇ>",
            "Cʟᴏɴᴇ ғʀᴏᴍ ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ᴍᴇᴅɪᴀ ᴏʀ ᴛɪᴍᴇʀ ᴍᴇꜱꜱᴀɢᴇ."],
    ],
) 
