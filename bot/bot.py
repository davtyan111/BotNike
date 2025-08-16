# bot.py

import time
import requests
from config import URL
from bot.handlers_inline import handle_update

offset = 0

print("🤖 Бот запущен...")

while True:
    try:
        r = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 15})
        data = r.json()
        if data.get("ok"):
            for update in data["result"]:
                offset = update["update_id"] + 1
                handle_update(update)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(3)
