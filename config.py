import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Cha Hae-In")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "TheSungJinwoo")
ALIVE_NAME = getenv("ALIVE_NAME", "Cha Hae-In Music")
BOT_USERNAME = getenv("BOT_USERNAME", "ChaHaeInBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FirstMonarch")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AnimeFunChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AinCradNetwork")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . +").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1daa11f5c22f9bac4d60a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Eqrazer/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/9ed109ac540d36fbd44e0.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/dff230db49b1340590b71.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5ef0c2e786365709ae1dd.png")
