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



from pyrogram import Client, filters
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd

from .help import *

@Client.on_message(
    filters.command(["banall"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def banall(client, message):
    if not message.from_user:
        return
    ok = await message.edit("Getting Chat Members......")
    mem = []
    async for x in client.get_chat_members(message.chat.id):
        mem.append(x.user.id)
    try:
        await ok.edit("Banning Chat Members....")
    except:
        await message.reply("Banning Chat Members")
    a = 0
    b = 0
    for y in mem:
        try:
            await client.ban_chat_member(message.chat.id, y)
            a += 1
        except:
            b += 1
            pass
    try:
        await ok.edit(f"**Done ✅**\n\n{a} Banned..!!\n \n{b} Failed..!!")
    except:
        await message.reply(f"**Done ✅\n\n{a} Banned..!!\n \n {b} Failed..!!")

add_command_help(
    "•─╼⃝𖠁 ʙᴀɴᴀʟʟ",
    [
        ["banall", "Tᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ."],
    ],
)
