import requests
from config import URL
from database.db import get_user_orders
from bot.logic_inline import process_callback, send_message, send_tariff_buttons

user_state = {}  # Храним состояние пользователя

def handle_update(update):
    if "message" in update:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        user_id = str(msg["from"]["id"])
        text = msg.get("text", "")

        if text == "/start":
            user_state.pop(user_id, None)
            send_tariff_buttons(chat_id)
            return

        # Всё остальное — игнор
        send_message(chat_id, "❗ Пожалуйста, используйте только кнопки.")
        return

    elif "callback_query" in update:
        query = update["callback_query"]
        user_id = str(query["from"]["id"])
        chat_id = query["message"]["chat"]["id"]
        data = query["data"]

        # Удаляем inline-кнопки (визуально)
        requests.post(f"{URL}/editMessageReplyMarkup", json={
            "chat_id": chat_id,
            "message_id": query["message"]["message_id"],
            "reply_markup": {"inline_keyboard": []}
        })

        # Обработка callback-кнопок
        process_callback(data, chat_id, user_id, user_state)
