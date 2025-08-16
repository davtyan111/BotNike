# bot/handlers_inline.py
import requests
from config import URL
from database.db import get_user_orders
from bot.logic_inline import process_callback, send_message, send_tariff_buttons

user_state = {}

def handle_update(update):
    if "callback_query" in update:
        query = update["callback_query"]
        user_id = str(query["from"]["id"])
        chat_id = query["message"]["chat"]["id"]
        data = query["data"]

        requests.post(f"{URL}/editMessageReplyMarkup", json={
            "chat_id": chat_id,
            "message_id": query["message"]["message_id"],
            "reply_markup": {"inline_keyboard": []}
        })

        process_callback(data, chat_id, user_id, user_state)

    elif "message" in update:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        user_id = str(msg["from"]["id"])
        text = msg.get("text", "")

        if text == "/start":
            user_state.pop(user_id, None)
            send_tariff_buttons(chat_id)  # динамически из БД
            return

        if text == "/history":
            orders = get_user_orders(user_id)
            if not orders:
                send_message(chat_id, "❗ История пуста.")
                return
            out = "🕓 Последние заказы:\n"
            for o in orders:
                out += (f"📦 {o['tariff']} | 🧩 {o['subcode']} | "
                        f"📍 {o['location']} | 🗓 {o['created_at'].strftime('%d.%m %H:%M')}\n")
            send_message(chat_id, out)
