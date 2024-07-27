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




import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import get_text

from .help import *


@Client.on_message(
    filters.command(["trump"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def trump_tweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.edit(f"**Trump :** ``What Should I Tweet For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Trump Has Tweeted** {text}"
    await message.edit(f"**Trump:** Wait I Am Tweeting Your Text")
    await client.send_photo(message.chat.id, tweet, caption=starkxd)
    await message.delete()


@Client.on_message(
    filters.command(["ctweet"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def custom_tweet(client: Client, message: Message):
    text = get_text(message)
    input_str = get_text(message)
    if text:
        if ":" in text:
            stark = input_str.split(":", 1)
        else:
            await message.edit("**Usage Syntax :** `username:tweet-text`")
            return
    if len(stark) != 2:
        await message.edit("**Usage Syntax :** `username:tweet-text`")
        return

    starky = stark[0]
    ipman = stark[1]
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={starky}&text={ipman}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**{starky} Has Tweeted** ``{ipman}``"
    await message.edit(f"**{starky}** : Wait I Am Tweeting Your Texts")
    await client.send_photo(message.chat.id, tweet, caption=starkxd)
    await message.delete()


add_command_help(
    "•─╼⃝𖠁 ᴍᴇᴍᴇꜱ",
    [
        ["trump", "ᴍᴀᴋᴇ ᴀ Qᴜᴏᴛᴇ ʙʏ Tʀᴜᴍᴘ."],
        ["ctweet", "Tᴡɪᴛᴛᴇ ʙʏ Uʀ ᴠᴀʟᴜᴇꜱ."],
    ],
)