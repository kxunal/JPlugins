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

#REMAKE BY NOBITA XD AND TRYTOLIVEALONE


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command("cdel", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(
    filters.command(["del"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def del_msg(client: Client, message: Message):
    msg_src = message.reply_to_message
    if msg_src:
        if msg_src.from_user.id:
            try:
                await client.delete_messages(message.chat.id, msg_src.id)
                await message.delete()
            except BaseException:
                pass
    else:
        await message.delete()


@Client.on_message(
    filters.command("cpurge", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(
    filters.command(["purge"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def purge(client: Client, message: Message):
    X = await edit_or_reply(message, "`Starting To Purge Messages!`")
    msg = message.reply_to_message
    if msg:
        itermsg = list(range(msg.id, message.id))
    else:
        await X.edit("`Reply To Message To Purge!`")
        return
    count = 0

    for i in itermsg:
        try:
            count = count + 1
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=i, revoke=True
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            await X.edit(f"**ERROR:** `{e}`")
            return

    done = await X.edit(
        f"**Fast Purge Completed!**\n**Successfully Delete** `{str(count)}` **Message.**"
    )
    await asyncio.sleep(2)
    await done.delete()


@Client.on_message(
    filters.command("cpurgeme", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(
    filters.command(["purgeme"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def purgeme(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await edit_or_reply(message, "Please enter a number")
    n = int(n)
    if n < 1:
        return await edit_or_reply(message, "Enter the number of messages you want to delete!")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await edit_or_reply(message, "Can't find message.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()


add_command_help(
    "•─╼⃝𖠁 ᴘᴜʀɢᴇ",
    [
        ["del", "Dᴇʟᴇᴛᴇ ᴀ ᴍᴇꜱꜱᴀɢᴇ, ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ."],
        ["purge", "Dᴇʟᴇᴛᴇ ᴀ ᴍᴇꜱꜱᴀɢᴇ, ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ."],
        ["purgeme <number>", "Dᴇʟᴇᴛᴇ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇꜱ, ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ."],
    ],
          ) 
