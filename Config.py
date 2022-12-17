import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "9899444837"))
    API_HASH = os.environ.get("API_HASH", "4cae52cbd28acc0e9899444837e4ea94")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "5848742997:AAF5cLBNzNU8p2jFQK1z6_Zs0DiapkYbR0A")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME"Nixa_MusicBot)
    SUPPORT = os.environ.get("SUPPORT", "Crush_World_xD") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Bothub_xD") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/36e8f0663efdad1865b15.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/36e8f0663efdad1865b15.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID"5741694439)) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
