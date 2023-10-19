from applemusicpy import AppleMusic
from dotenv import load_dotenv
import os

load_dotenv()

def __init__():
    SECRET_KEY = os.getenv(SECRET_KEY)
    KEY_ID = os.getenv(KEY_ID)
    TEAM_ID = os.getenv(TEAM_ID)
    am = AppleMusic(SECRET_KEY, KEY_ID, TEAM_ID)

    return am