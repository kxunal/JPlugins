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

# Credits: KUNAL AND NOBITA XD 
# Copyright (C) 2024 JAPANESE X USERBOT AND STORM USERBOT 
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 

import asyncio
from random import choice
from pyrogram.types import Message
from pyrogram import filters, Client
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd
from config import OWNER_ID, SUDO_USERS, CMD_HANDLER as cmd
from XDB.data import SUPERRAID
from XDB.data import SUPERRAID, MASTERS
from .help import *

@Client.on_message(
    filters.command(["raid"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def raid(x: Client, e: Message):
      NOBI = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(NOBI) == 2:
          ok = await x.get_users(kex[1])
          counts = int(NOBI[0])
          for _ in range(counts):
                reply = choice(SUPERRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(NOBI[0])
          for _ in range(counts):
                reply = choice(SUPERRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text(".Rᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  

reply_raid_users = []

@Client.on_message(filters.command(["rraid", "replyraid"], cmd) & (filters.me | filters.user(SUDO_USERS)))
async def activate_reply_raid(client: Client, message: Message):
    global reply_raid_users
    args = message.text.split()

    if len(args) > 1:
        user = await client.get_users(args[1])
        user_id = user.id
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        await message.reply_text(f"{cmd}rraid <username> or reply to a user")
        return

    if user_id in MASTERS:
        await message.reply_text("Nope, this guy is an owner ☠️")
    elif user_id == OWNER_ID:
        await message.reply_text("Nope, this guy is the owner of these bots 🥀")
    elif user_id in SUDO_USERS:
        await message.reply_text("Nope, this guy is a sudo user 💗")
    else:
        reply_raid_users.append(user_id)
        await message.reply_text("Activated reply raid ✅")

@Client.on_message(filters.command(["drraid", "draid", "dreplyraid"], cmd) & (filters.me | filters.user(SUDO_USERS)))
async def deactivate_reply_raid(client: Client, message: Message):
    global reply_raid_users
    args = message.text.split()

    if len(args) > 1:
        user = await client.get_users(args[1])
        user_id = user.id
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        await message.reply_text(f"{cmd}drraid <username> or reply to a user")
        return

    if user_id in reply_raid_users:
        reply_raid_users.remove(user_id)
        await message.reply_text("Reply raid de-activated ✅")

@Client.on_message(~filters.me & filters.incoming)
async def reply_raid_watcher(client: Client, message: Message):
    global reply_raid_users
    user_id = message.from_user.id

    if user_id in reply_raid_users:
        reply_text = choice(SUPERRAID)
        await message.reply_text(reply_text)


add_command_help(
    "•─╼⃝𖠁 Rᴀɪᴅ",
    [
        ["raid", "Tᴏ ꜱᴇɴᴅ Rᴀɪᴅ Mᴇssᴀɢᴇs."],
        ["rraid", "To activate reply raid,"],
        ["drraid", "To De Activate reply raid."],
    ],
)
