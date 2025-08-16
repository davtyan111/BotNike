import time
import requests
from config import URL
from bot.handlers_inline import handle_update
from database.init import init_db

init_db()  # создаёт таблицу при старте

offset = 0

while True:
    try:
        res = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 30})
        data = res.json()

        if "result" in data:
            for update in data["result"]:
                offset = update["update_id"] + 1
                handle_update(update)

    except Exception as e:
        print("❌ Ошибка:", e)

    time.sleep(1)
