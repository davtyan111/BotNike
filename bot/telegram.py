# bot/telegram.py

import time
import requests
from config import URL
from bot.handlers_inline import handle_message, handle_callback

offset = 0

def run_bot():
    global offset
    while True:
        try:
            response = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 10})
            data = response.json()

            if not data.get("ok"):
                time.sleep(5)
                continue

            for update in data.get("result", []):
                offset = update["update_id"] + 1

                if "message" in update:
                    handle_message(update["message"])

                elif "callback_query" in update:
                    handle_callback(update["callback_query"])

        except Exception as e:
            print("⛔ Ошибка в боте:", e)
            time.sleep(2)

if __name__ == "__main__":
    run_bot()
