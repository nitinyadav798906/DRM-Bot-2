import os

API_ID    = os.environ.get("API_ID", "21705536")
API_HASH  = os.environ.get("API_HASH", "c5bb241f6e3ecf33fe68a444e288de2d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7979826252:AAHqDDYYE2je4urXPATIubOLjroZX65HjXw") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
