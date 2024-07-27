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

import humanize
from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS

from .help import *


async def progress_callback(current, total, bot: Client, message: Message):
    if int((current / total) * 100) % 25 == 0:
        await message.edit(f"{humanize.naturalsize(current)} / {humanize.naturalsize(total)}")


@Client.on_message(filters.command('upload', '.') & filters.me)
@Client.on_message(
    filters.command(["upload"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def upload_helper(bot: Client, message: Message):
    if len(message.command) > 1:
        await bot.send_document('self', message.command[1], progress=progress_callback, progress_args=(bot, message))
    else:
        await message.edit('No path provided.')
        await asyncio.sleep(3)

    await message.delete()


add_command_help(
    "•─╼⃝𖠁 Uᴘʟᴏᴀᴅ",
    [
        [".upload", "Uᴘʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ꜱʏꜱᴛᴇᴍ ғɪʟᴇ ᴘᴀᴛʜ."],
    ],
)
