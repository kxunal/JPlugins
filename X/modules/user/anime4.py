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

#CREDIT : GURU BOT THANKS FOR YOUR ANIME API 

#REMAKE BY : NOBITA XD AND TRYTOLIVEALONE
# Copyright (C) 2024 JAPANESE X USERBOT
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 







import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HANDLER as cmd
from config import SUDO_USERS

from .help import * 

API_URL = "https://api.nekosapi.com/v3/images/17"


@Client.on_message(
    filters.command(["anime4"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def anime4(client: Client, message: Message):
    # Send the "Processing..." message
    await message.edit("Fetching a random anime image...")

    # Make the API request
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()["data"]["attributes"]
        image_url = data["file"]
        title = data["title"]
    except (requests.exceptions.RequestException, KeyError):
        await message.edit("Failed to fetch a random anime image.")
        return

    # Send the image and title as a reply
    await client.send_photo(message.chat.id, image_url, caption=f"**Title:** {title}")

    # Edit the original message to indicate success
    await message.edit("Random anime image sent!")

add_command_help(
    "•─╼⃝𖠁 ᴀɴɪᴍᴇ4",
    [
       ["anime4", "Gɪᴠᴇ random anime pic."],
        ],
)
