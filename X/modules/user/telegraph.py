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



from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply, get_text
from config import SUDO_USERS
from X.helpers.tools import *

from .help import *

telegraph = Telegraph()
r = telegraph.create_account(short_name="PyroMan-Userbot")
auth_url = r["auth_url"]


@Client.on_message(
    filters.command(["tg", "telegraph"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def uptotelegraph(client: Client, message: Message):
    X = await edit_or_reply(message, "`Processing . . .`")
    if not message.reply_to_message:
        await X.edit(
            "**Please reply to the message, to get the link from Telegraph.**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await X.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        U_done = (
            f"**Successfully uploaded to** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await X.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await X.edit(f"**ERROR:** `{exc}`")
            return
        wow_graph = f"**Successfully uploaded to** [Telegraph](https://telegra.ph/{response['path']})"
        await X.edit(wow_graph)


add_command_help(
    "•─╼⃝𖠁 ᴛᴇʟᴇɢʀᴀᴘʜ",
    [
        [
            f"telegraph ᴀᴛᴀᴜ {cmd}tg",
            "Rᴇᴘʟʏ ᴛᴏ ᴀ Tᴇxᴛ Mᴇꜱꜱᴀɢᴇ ᴏʀ Mᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.",
        ],
    ],
) 
