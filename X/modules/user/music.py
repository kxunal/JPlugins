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

import asyncio

from pyrogram import filters, Client 
from pyrogram.types import Message

from X.helpers.PyroHelpers import ReplyCheck
from config import SUDO_USERS
from .help import *


@Client.on_message(
    filters.command(["music"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def send_music(bot: Client, message: Message):
    try:
        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                    message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("Give a song name")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await bot.get_inline_bot_results("deezermusicbot", song_name)

        try:
            # send to Saved Messages because hide_via doesn't work sometimes
            saved = await bot.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
            )

            # forward as a new message from Saved Messages
            saved = await bot.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.id
                if message.reply_to_message
                else None
            )
            await bot.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=ReplyCheck(message),
            )

            # delete the message from Saved Messages
            await bot.delete_messages("me", saved.id)
        except TimeoutError:
            await message.edit("Tʜᴀᴛ ᴅɪᴅɴ'ᴛ ᴡᴏʀᴋ ᴏᴜᴛ")
            await asyncio.sleep(2)
        await message.delete()
    except Exception as e:
        print(e)
        await message.edit("`Fᴀɪʟᴇᴅ ᴛᴏ ғɪɴᴅ ꜱᴏɴɢ`")
        await asyncio.sleep(2)
        await message.delete()


add_command_help("•─╼⃝𖠁 ᴍᴜꜱɪᴄ", [[".m ᴏʀ .music", "Sᴇᴀʀᴄʜ ꜱᴏɴɢꜱ ᴀɴᴅ ꜱᴇɴᴅ."]])
