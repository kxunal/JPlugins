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

import time

from pyrogram import filters, Client
from pyrogram.types import Message
from X.helpers.basic import edit_or_reply
from config import SUDO_USERS

from .help import *


class Custom(dict):
    def __missing__(self, key):
        return 0


@Client.on_message(
    filters.command(["wordcount"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def word_count(bot: Client, message: Message):
    await message.delete()
    words = Custom()
    progress = await bot.send_message(message.chat.id, "`Processed 0 messages...`")
    total = 0
    async for msg in bot.iter_history(message.chat.id, 1000):
        total += 1
        if total % 100 == 0:
            await progress.edit_text(f"`Processed {total} messages...`")
            time.sleep(0.5)
        if msg.text:
            for word in msg.text.split():
                words[word.lower()] += 1
        if msg.caption:
            for word in msg.caption.split():
                words[word.lower()] += 1
    freq = sorted(words, key=words.get, reverse=True)
    out = "Word Counter\n"
    for i in range(25):
        out += f"{i + 1}. **{words[freq[i]]}**: {freq[i]}\n"

    await progress.edit_text(out)


add_command_help(
    "•─╼⃝𖠁 ᴍᴇᴛʀɪᴄꜱ",
    [
        [
            ".wordcount",
            "Fɪɴᴅꜱ ᴛʜᴇ 𝟸𝟻 ᴍᴏꜱᴛ ᴜꜱᴇᴅ ᴡᴏʀᴅꜱ ɪɴ ᴛʜᴇ ʟᴀꜱᴛ 𝟷𝟶𝟶𝟶 ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ. Uꜱᴇ ɪɴ "
            "ᴄʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ғɪɴᴅ ᴛʜᴇ ᴍᴇᴛʀɪᴄ ɪɴ.",
        ],
    ],
)
