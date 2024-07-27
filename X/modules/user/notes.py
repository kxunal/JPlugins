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

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO_USERS
from X.helpers import *
from X.helpers.SQL.notes_sql import *
from X.utils import *
from X import *

from .help import *


@Client.on_message(
    filters.command(["notes"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def list_notes(client, message):
    user_id = message.from_user.id
    notes = get_notes(str(user_id))
    if not notes:
        return await message.reply("No note.")
    msg = f"➣ List of notes\n\n"
    for note in notes:
        msg += f"◉ {note.keyword}\n"
    await message.reply(msg)


@Client.on_message(
    filters.command(["delnote"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def remove_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    if rm_note(str(user_id), notename) is False:
        return await message.reply(
            "Can't find note: {}".format(notename)
        )
    return await message.reply("Successfully Delete Note: {}".format(notename))


@Client.on_message(
    filters.command(["save"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def simpan_note(client, message):
    keyword = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("Please reply to messages")
    anu = await msg.forward(client.me.id)
    msg_id = anu.id
    await client.send_message(client.me.id,
        f"#NOTE\nKEYWORD: {keyword}"
        "\n\nThe following messages are saved as reply data for chats, please DO NOT delete them !!",
    )
    await sleep(1)
    add_note(str(user_id), keyword, msg_id)
    await message.reply(f"Saved successfully note {keyword}")


@Client.on_message(
    filters.command(["get"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def panggil_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    note = get_note(str(user_id), notename)
    if not note:
        return await message.reply("There are no such records.")
    msg_o = await client.get_messages(client.me.id, int(note.f_mesg_id))
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)

add_command_help(
    "•─╼⃝𖠁 ɴᴏᴛᴇꜱ",
    [
        ["save [ᴛᴇxᴛ/ʀᴇᴘʟʏ]",
            "Sᴀᴠᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ Gʀᴏᴜᴘꜱ. (ᴄᴀɴ ᴜꜱᴇ ꜱᴛɪᴄᴋᴇʀꜱ)"],
        ["get [ɴᴀᴍᴀ]",
            "Tᴀᴋᴇ ɴᴏᴛᴇ ᴛᴏ ꜱᴀᴠᴇᴅ"],
        ["notes",
            "Sᴇᴇ Nᴏᴛᴇꜱ Lɪꜱᴛ"],
        ["delnote [ɴᴀᴍᴀ]",
            "Dᴇʟᴇᴛᴇ ᴀ ɴᴏᴛᴇ ɴᴀᴍᴇ"],
    ],
      )
