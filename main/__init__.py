#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("23308278", default=None, cast=int)
API_HASH = config("b9e478d024ad099bdeede4ef1b55a9b4", default=None)
BOT_TOKEN = config("6659822191:AAEmq3h_mPqcX7x0Sfa01xBwN7o1p0gcmNQ", default=None)
SESSION = config("AQC-HpEjear8g-zbnm-n4ZWwHry9_vmjBbKvJNk_BuK6BV4_JvoPVAvfiF8jghe-oCDOvoqNxmHWkVX3mOnkrkX2dIxtbeVYayxTPmFIFb5Jk3qgS_x3fjboDttstDfEVkHO_6cw286HChJB0F-zHAdigOHZ_qrQeL9kF5z5Mnlt1pQco2_0E40yxPVRu1Sc6x9L9qgYnksDOZtdWnVhQBpPPHSyC0Iff9yx4OjaAwvGrXW7b3qalAu9RqCCb9mvYOxgLnDhWg7m_bXuT1FRSAsh3EnJ3vXJKgv46u0HvN4v3gxltM7JAVbsfBJ51oGqnm6fMb9Xt5OwZaZhEYrTVjPXS2mvPAA", default=None)
FORCESUB = config("mantapvids", default=None)
AUTH = config("1281619082", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
