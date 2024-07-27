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

# Credits: NOBITA XD and TRYTOLIVEALONE 
# Copyright (C) 2024 JAPANESE X USERBOT
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 


import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message
import os
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd

from .help import *

@Client.on_message(
    filters.command(["lyrics"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def get_lyrics(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴜꜱᴇ %𝟸𝟶 ɪɴ ʙᴇᴛᴡᴇᴇɴ ʏᴏᴜʀ ꜱᴏɴɢ ɪғ ɪᴛ'ꜱ ᴍᴏʀᴇ ᴛʜᴇɴ 𝟷 ᴡᴏʀᴅ\nExᴀᴍᴘʟᴇ .ʟʏʀɪᴄꜱ ᴛᴜ%𝟸𝟶ʜᴀɪɴ%𝟸𝟶ᴋᴀʜᴀ")
        return

    question = message.text.split(" ", maxsplit=1)[1]

    lyrics_url = f'https://lyrist.vercel.app/api/{question}'

    async with aiohttp.ClientSession() as session:
        async with session.get(lyrics_url) as request:
            if request.status == 404:
                return await message.reply_text("Lʏʀɪᴄꜱ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ ᴛʜɪꜱ ꜱᴏɴɢ.")

            lyrics_data = await request.json()

            try:
                image = lyrics_data['image']
                lyrics = lyrics_data['lyrics']

                lyrics_file_path = f"{question}_lyrics.txt"  # Use 'question' instead of 'song_name'
                with open(lyrics_file_path, "w", encoding="utf-8") as file:
                    file.write(lyrics)

                await client.send_document(
                    chat_id=message.chat.id,
                    document=lyrics_file_path,
                    caption=f"Lʏʀɪᴄꜱ ғᴏʀ {lyrics_data['title']} by {lyrics_data['artist']}"
                )
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=image
                )

                os.remove(lyrics_file_path)

            except Exception as e:
                print(str(e))
                pass

add_command_help(
    "•─╼⃝𖠁 Lʏʀɪᴄs",
    [
        ["lyrics", "Gᴇᴛ ʟʏʀɪᴄꜱ ғᴏʀ ᴀ ꜱᴏɴɢ."],
    ],
)
