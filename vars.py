import os

API_ID    = os.environ.get("API_ID", "21705536")
API_HASH  = os.environ.get("API_HASH", "c5bb241f6e3ecf33fe68a444e288de2d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7407487191:AAHTf4iqO7gQn_ENUAHl37VsOQxgY29SVaI") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
