# bot/utils.py

import requests
from config import URL

def send_support_link(chat_id):
    keyboard = {
        "inline_keyboard": [[
            {
                "text": "💬 Связаться с поддержкой",
                "url": "https://t.me/DavtyanRaf"
            }
        ]]
    }
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": "Если возникли вопросы — напиши в поддержку:",
        "reply_markup": keyboard
    })
