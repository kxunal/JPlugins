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


from pyrogram import Client, enums, filters
from pyrogram.types import Message

from X.helpers.adminHelpers import DEVS
from config import BLACKLIST_CHAT
from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.command("interrupted", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(
    filters.command(["join"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def join(client: Client, message: Message):
    X = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**Successfully Joined Chat ID** `{X}`")
        await client.join_chat(X)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["leave", "kickme"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def leave(client: Client, message: Message):
    X = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("**This command is not allowed to be used in this group**")
    try:
        await xxnx.edit_text(f"{client.me.first_name} has left this group, bye!!")
        await client.leave_chat(X)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["leaveallgc"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def kickmeall(client: Client, message: Message):
    X = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await X.edit(
        f"**Successfully Exit {done} Group, Failed to Exit {er} Group**"
    )


@Client.on_message(
    filters.command(["leaveallch"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def kickmeallch(client: Client, message: Message):
    X = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await X.edit(
        f"**Successfully Exit {done} Channel, Failed to Exit {er} Channel**"
    )


add_command_help(
    "•─╼⃝𖠁 ɪᴏɪɴʟᴇᴀᴠᴇ",
    [
        [
            "kickme",
            "Lᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ʙʏ ᴅɪꜱᴘʟᴀʏɪɴɢ ᴀ ᴍᴇꜱꜱᴀɢᴇ ʜᴀꜱ ʟᴇғᴛ ᴛʜɪꜱ ɢʀᴏᴜᴘ, ʙʏᴇ!!.",
        ],
        ["leaveallgc", "Exɪᴛ ᴀʟʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘꜱ ʏᴏᴜ ʜᴀᴠᴇ ɪᴏɪɴᴇᴅ."],
        ["leaveallch", "Exɪᴛ ᴀʟʟ Tᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟꜱ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ɪᴏɪɴᴇᴅ."],
        ["join ", "Tᴏ Jᴏɪɴ ᴛʜᴇ Cʜᴀᴛ Vɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ."],
        ["leave ", "Tᴏ ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ Vɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ."],
    ],
)
