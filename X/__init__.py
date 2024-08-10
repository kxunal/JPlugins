import asyncio
import logging
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict

from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client
from pytgcalls import GroupCallFactory

from config import (
    API_HASH,
    API_ID,
    DB_URL,
    BOTLOG_CHATID,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10,
    SUDO_USERS,
    BOT_TOKEN
)

# Function to initialize the bot and other services
async def main():
    DATABASE_URL = DB_URL
    CMD_HELP = {}
    SUDO_USER = SUDO_USERS
    clients = []
    ids = []
    LOG_FILE_NAME = "logs.txt"

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] - %(name)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        handlers=[
            RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
            logging.StreamHandler(),
        ],
    )
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)
    logging.getLogger("pytgcalls").setLevel(logging.WARNING)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
    logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

    LOGS = logging.getLogger(__name__)

    if (
        not STRING_SESSION1
        and not STRING_SESSION2
        and not STRING_SESSION3
        and not STRING_SESSION4
        and not STRING_SESSION5
    ):
        LOGS.warning("STRING SESSION NOT FOUND , SHUTDOWN BOT!")
        sys.exit()

    if not API_ID:
        LOGS.warning("API_ID NOT FOUND, SHUTDOWN BOT")
        sys.exit()

    if not API_HASH:
        LOGS.warning("API_HASH NOT FOUND, SHUTDOWN BOT")
        sys.exit()

    if not BOT_TOKEN:
        LOGS.warning("WARNING: BOT TOKEN NOT FOUND, SHUTDOWN BOT")
        sys.exit()

    if BOTLOG_CHATID:
        BOTLOG_CHATID = BOTLOG_CHATID
    else:
        BOTLOG_CHATID = "me"

    trl = Translator()

    # Create the ClientSession within an active event loop
    async with ClientSession() as aiosession:
        CMD_HELP = {}
        scheduler = AsyncIOScheduler()
        StartTime = time.time()
        START_TIME = datetime.now()
        TEMP_SETTINGS: Dict[Any, Any] = {}
        TEMP_SETTINGS["PM_COUNT"] = {}
        TEMP_SETTINGS["PM_LAST_MSG"] = {}

        app = Client(
            name="app",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="X/modules/bot"),
            in_memory=True,
        )

        bots = [
            Client(
                name=f"bot{i+1}",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=session,
                plugins=dict(root="X/modules"),
            )
            for i, session in enumerate([
                STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5,
                STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
            ])
            if session
        ]

        for bot in bots:
            if not hasattr(bot, "group_call"):
                setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())

        # Start the bots and the scheduler here
        await app.start()
        for bot in bots:
            await bot.start()

        scheduler.start()

        # Keep the script running
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
