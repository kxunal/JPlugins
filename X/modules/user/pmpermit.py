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

from pyrogram import Client, filters
from X.Database.pm import *
from X.powers import get_id
from config import PM_PIC

from .help import *

hl = "."

JPX = PM_PIC
pm_watcher = 5

TEXT = """
╭═══════════════════╮
✧ 𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓✧
╰═══════════════════╯
╰• **ᴏᴡɴᴇʀ** » {}
• **ᴛʜɪs ɪs 𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 ᴘᴍ sᴇᴄᴜʀɪᴛʏ 🛡️**
➖➖➖➖➖➖➖➖➖➖➖ 
    **ʜᴇʏ ꜱᴀᴍᴜʀᴀɪ** 🥀
    **ɪғ ʏᴏᴜ sᴘᴀᴍ ʜᴇʀᴇ ᴡɪᴛʜᴏᴜᴛ ᴍʏ**
    **ᴍᴀꜱᴛᴇʀ's ᴀᴘᴘʀᴏᴠᴀʟ ʏᴏᴜ ᴡɪʟʟ ʙᴇ**
    **ʙʟᴏᴄᴋᴇᴅ** 
⚝  **ᴡᴀʀɴ ʟɪᴍɪᴛs** » {}      
⚝  **ʏᴏᴜʀ ᴡᴀʀɴs** » {}
➖➖➖➖➖➖➖➖➖➖➖
•
╰───❰ [ᴍᴀᴋᴇ ᴍᴇ ʏᴏᴜʀs](https://github.com/Team-Japanese/Japanese-X-Userbot) ❱
"""

@Client.on_message(filters.command("pmpermit", hl) & filters.me)
async def pmpermit(client, message):
    x = await is_pm_on()
    try:
        tg = message.text.split()[1].lower()
    except:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if not tg in ["on", "off"]:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if tg == "on":
        if x:
            return await message.edit("ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴘᴍᴘᴇʀᴍɪᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ...")
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ...")
    if not x:
        return await message.edit("ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴘᴍᴘᴇʀᴍɪᴛ ɪꜱ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ...")
    await toggle_pm()
    return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀʙʟᴇᴅ....")

@Client.on_message(filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], hl) & filters.me)
async def appr_dis(client, message):
    if str(message.chat.id)[0] == "-":
        try:
            id = await get_id(_, message)
        except:
            return await message.edit("ꜰᴏʀ ᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ᴍᴇ ɪ'ᴅ ᴏʀ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴜꜱᴇʀ..")
    else:
        id = message.chat.id
    tg = message.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await message.edit("ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀᴘᴘʀᴏᴠᴇᴅ....")
        await disapprove(id)
        return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ....")
    if x:
        return await message.edit("ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ...")
    await approve(id) 
    await reset_warns(id)
    return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ....")

@Client.on_message(filters.command("setwarns", hl) & filters.me)
async def setwarn(client, message):
    try:
        count = int(message.text.split()[1])
    except:
        return await message.edit(f"{hl}setwarns [ᴠᴀʟᴜᴇ]")
    if count == 0:
        return await message.edit("ɢɪᴠᴇ ᴍᴇ ɴᴜᴍᴇʀɪᴄᴀʟ ᴠᴀʟᴜᴇ ᴛᴏ ꜱᴇᴛ ᴡᴀʀɴꜱ..")
    await update_warns(count)
    await message.edit(f"ᴅᴍ ᴡᴀʀɴꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇᴛ ᴛᴏ {count}..")
    
@Client.on_message(filters.private, group=pm_watcher)
async def wtch(client, message):
    user_ = message.from_user
    if message.from_user.id == client.me.id:
        return
    if not await is_pm_on():
        return
    if user_.is_bot:
        return
    if await is_approved(message.from_user.id):
        return
    await add_warn(message.from_user.id)
    if await limit() <= await get_warns(message.from_user.id):
        await message.reply("ꜱᴘᴀᴍᴍᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ ᴀɴᴅ ʙʟᴏᴄᴋᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ....")
        await reset_warns(message.from_user.id)
        return await client.block_user(message.from_user.id)
    await message.reply_photo(JPX, caption=TEXT.format((await client.get_me()).first_name, await limit(), await get_warns(message.from_user.id)))


add_command_help(
    "•─╼⃝𖠁 Pᴍᴘᴇʀᴍɪᴛ",
    [
       ["pmpermit on", "Tᴏ ᴇɴᴀʙʟᴇ Pᴍ ᴘᴇʀᴍɪᴛ ᴍᴇssᴀɢᴇ."],
       ["pmpermit off", "Tᴏ Dɪsᴀʙʟᴇ Pᴍ ᴘᴇʀᴍɪᴛ ᴍᴇssᴀɢᴇ."],
       ["approve", "Tᴏ ᴀᴘᴘʀᴏᴠᴇ sᴏᴍᴇᴏɴᴇ ɪɴ ʏᴏᴜʀ ᴅᴍ."],
       ["disapprove", "Tᴏ Dɪsᴀᴘᴘʀᴏᴠᴇ sᴏᴍᴇᴏɴᴇ ɪɴ ʏᴏᴜʀ ᴅᴍ."],
        ],
)
