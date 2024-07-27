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

from asyncio import sleep

from pyrogram import filters, Client 


from X.helpers.aiohttp_helper import AioHttp
from config import SUDO_USERS
from .help import *


def replace_text(text):
    return text.replace('"', "").replace("\\r", "").replace("\\n", "").replace("\\", "")


@Client.on_message(filters.me & filters.command(["ud"], "."))
@Client.on_message(
    filters.command(["ud"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def urban_dictionary(bot, message):
    if len(message.text.split()) == 1:
        await message.edit("Usage: `ud example`")
        return
    try:
        text = message.text.split(None, 1)[1]
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={text}"
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        resp = (
            f"**Text: {replace_text(word)}**\n"
            f"**Meaning:**\n`{replace_text(definition)}`\n\n"
            f"**Example:**\n`{replace_text(example)}` "
        )
        await message.edit(resp)
        return
    except Exception as e:
        await message.edit("`The Urban Dictionary API could not be reached`")
        print(e)
        await sleep(3)
        await message.delete()



add_command_help(
    "•─╼⃝𖠁 ᴅɪᴄᴛɪᴏɴᴀʀʏ",
    [
        [".ubran | .ud", "Dᴇғɪɴᴇ ᴛʜᴇ ᴡᴏʀᴅ ʏᴏᴜ ꜱᴇɴᴅ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ."],
    ],
        )
