import os

API_ID    = os.environ.get("API_ID", "12475131")
API_HASH  = os.environ.get("API_HASH", "719171e38be5a1f500613837b79c536f)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8012231272:AAFITViiSvq-2hXqbCaS4VBwHahNsim-woE") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
