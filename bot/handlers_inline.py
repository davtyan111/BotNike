# bot/handlers_inline.py
import requests
from config import URL
from database.db import get_user_orders
from bot.logic_inline import process_callback, send_message, send_tariff_buttons, send_start_inline_buttons

user_state = {}

def handle_update(update):
    if "callback_query" in update:
        query = update["callback_query"]
        user_id = str(query["from"]["id"])
        chat_id = query["message"]["chat"]["id"]
        data = query["data"]

        requests.post(f"{URL}/deleteMessage", json={
            "chat_id": chat_id,
            "message_id": query["message"]["message_id"]
        })

        process_callback(data, chat_id, user_id, user_state)

    elif "message" in update:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        user_id = str(msg["from"]["id"])
        text = msg.get("text", "")

        if text == "/start":            
            user_state.pop(user_id, None)
            # Отправляем приветственное сообщение с двумя inline-кнопками
            send_start_inline_buttons(chat_id)
            return

        # Все остальные команды теперь работают через inline-кнопки
