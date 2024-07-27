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

# Credits: NOBITA XD AND KUNAL 
# Copyright (C) 2024 JAPANESE X USERBOT AND STORM USERBOT 
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 



import asyncio
from threading import Event

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import BLACKLIST_CHAT, BOTLOG_CHATID
from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from X.utils.misc import extract_args

from .help import *

commands = ["spam", "statspam", "slowspam", "fastspam"]
SPAM_COUNT = [0]


def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 50


@Client.on_message(
    filters.command(["dpsam", "delayspam"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def delayspam(client: Client, message: Message):
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**This command is not allowed to be used in this group**"
        )
    delayspam = await extract_args(message)
    arr = delayspam.split()
    if len(arr) < 3 or not arr[0].isdigit() or not arr[1].isdigit():
        await message.edit("`Something seems missing / wrong.`")
        return
    delay = int(arr[0])
    count = int(arr[1])
    spam_message = delayspam.replace(arr[0], "", 1)
    spam_message = spam_message.replace(arr[1], "", 1).strip()
    await message.delete()

    if not spam_allowed():
        return

    delaySpamEvent = Event()
    for i in range(0, count):
        if i != 0:
            delaySpamEvent.wait(delay)
        await client.send_message(message.chat.id, spam_message)
        limit = increment_spam_count()
        if not limit:
            break

    await client.send_message(
        BOTLOG_CHATID, "**#DELAYSPAM**\nDelaySpam was executed successfully"
    )


@Client.on_message(filters.command(commands, cmd) & filters.me)
async def sspam(client: Client, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    cooldown = {"spam": 0.15, "statspam": 0.1, "slowspam": 0.9, "fastspam": 0}

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await client.send_message(message.chat.id, text)

        if message.command[0] == "statspam":
            await asyncio.sleep(0.1)
            await sent.delete()

        await asyncio.sleep(cooldown[message.command[0]])


@Client.on_message(
    filters.me & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], cmd)
)
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await edit_or_reply(
            message, "**reply to a sticker with amount you want to spam**"
        )
        return
    if not message.reply_to_message.sticker:
        await edit_or_reply(
            message, "**reply to a sticker with amount you want to spam**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)


add_command_help(
    "•─╼⃝𖠁 ꜱᴘᴀᴍ",
    [
        ["spam <ᴀᴍᴏᴜɴᴛ ꜱᴘᴀᴍ> <ᴛᴇxᴛ>", "Sᴘᴀᴍᴍɪɴɢ ᴛᴇxᴛꜱ ɪɴ ᴄʜᴀᴛ!!"],
        [
            "delayspam <ꜱᴇᴄᴏɴᴅ> <ꜱᴘᴀᴍ ᴄᴏᴜɴᴛ> <ᴛᴇxᴛ>",
            "Sᴇɴᴅɪɴɢ ꜱᴘᴀᴍ ᴛᴇxᴛꜱ ᴡɪᴛʜ ᴀ ꜱᴘᴇᴄɪғɪᴇᴅ ᴅᴇʟᴀʏ ᴘᴇʀɪᴏᴅ!",
        ],
    ],
  )
