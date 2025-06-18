import requests
from decouple import config
from .models import TelegramUser

TOKEN = config('TELEGRAM_BOT_TOKEN')
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates():
    res = requests.get(URL + "getUpdates")
    data = res.json()

    for result in data.get("result", []):
        message = result.get("message", {})
        if message.get("text") == "/start":
            user_data = message.get("from", {})
            username = user_data.get("username")

            if username:  
                TelegramUser.objects.get_or_create(username=username)
            else:
                print(" Skipped: user has no username")
