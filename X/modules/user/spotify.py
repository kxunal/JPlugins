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

from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from X.helpers.basic import *
from X.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER
from config import SUDO_USERS
from X.utils import *
from urllib.parse import quote

import requests
import os
import json
import random

from .help import *

# Updated API details
@app.on_message(filters.command("Spotify", prefixes="."))
async def spotify_dl(client, message):
    try:
        # Extract song name from the message
        song_name = " ".join(message.command[1:])
        
        # Fetch data from SpotifyDL API
        api_url = f"https://spotifydl-nu.vercel.app/api/search?q={song_name}"
        response = requests.get(api_url)
        data = response.json()
        
        # Extract relevant information
        track_name = data["trackName"]
        artist = data["artist"]
        album = data["album"]
        audio_url = data["audio"]
        
        # Send audio to the chat
        await message.reply_audio(audio=audio_url, caption=f"🎵 **{track_name}** by {artist} from the album *{album}*")
    
    except Exception as e:
        print(f"Error: {str(e)}")

    
add_command_help(
    "•─╼⃝𖠁 Sᴘᴏᴛɪғʏ",
    [
       ["spotify", "Sᴇɴᴅ Sᴘᴏᴛɪғʏ Sᴏɴɢ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ."],
        ],
)
