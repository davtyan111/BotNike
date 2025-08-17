# bot/logic_inline.py
import requests
from config import URL
from database.db import (
    find_photo_by_filters, save_order, get_user_orders,
    get_all_tariffs, get_all_subcodes, get_all_locations,
    # если нет этих точечных функций, не страшно — ниже я делаю мапы из списков
)
from bot.utils import send_support_link


def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": text})


def _inline_keyboard(rows):
    return {"inline_keyboard": rows}


def _row(*buttons):
    return [{"text": t, "callback_data": d} for t, d in buttons]


def _rows_by(buttons, per_row=3):
    return [buttons[i:i+per_row] for i in range(0, len(buttons), per_row)]


# === 1) Тарифы ===
def send_tariff_buttons(chat_id, per_row=3):
    tariffs = get_all_tariffs()  # [{"id":1,"name":"0.5","emoji":"📦"}] или без emoji
    if not tariffs:
        send_message(chat_id, "Пока нет доступных тарифов.")
        return

    btns = []
    for t in tariffs:
        emoji = t.get("emoji", "📦")
        label = f"{emoji} {t['name']}".strip()
        # используем id в callback
        btns.append((label, f"tariff:{t['id']}"))

    rows = [_row(*chunk) for chunk in _rows_by(btns, per_row=per_row)]
    rows.append(_row(("🧾 История заказов", "history"), ("👤 Мой аккаунт", "my_account")))

    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": "👋 Привет! Выбери тариф:",
        "reply_markup": _inline_keyboard(rows)
    })


# === 2) Тип ===
def send_type_buttons(chat_id, per_row=3):
    types_ = get_all_subcodes()  # [{"id":10,"name":"glo","emoji":"🔥"}]
    if not types_:
        send_message(chat_id, "Типы пока не настроены в админке.")
        return

    btns = []
    for s in types_:
        emoji = s.get("emoji", "")
        label = f"{emoji} {s['name']}".strip()
        btns.append((label, f"type:{s['id']}"))

    rows = [_row(*chunk) for chunk in _rows_by(btns, per_row=per_row)]
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": "Теперь выбери тип:",
        "reply_markup": _inline_keyboard(rows)
    })


# === 3) Локация ===
def send_location_buttons(chat_id, per_row=3):
    locs = get_all_locations()  # [{"id":100,"name":"kentron","emoji":"📍"}]
    if not locs:
        send_message(chat_id, "Локации пока не настроены в админке.")
        return

    btns = []
    for l in locs:
        emoji = l.get("emoji", "📍")
        label = f"{emoji} {l['name']}".strip()
        btns.append((label, f"loc:{l['id']}"))

    rows = [_row(*chunk) for chunk in _rows_by(btns, per_row=per_row)]
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": "📍 Выбери локацию:",
        "reply_markup": _inline_keyboard(rows)
    })


# === обработка шагов ===
def process_callback(data, chat_id, user_id, user_state):
    if data == "history":
        orders = get_user_orders(user_id)
        if not orders:
            send_message(chat_id, "❗ История пуста.")
            return
        msg = "🕓 Последние заказы:\n"
        for o in orders:
            msg += (f"📦 {o['tariff']} | 🧩 {o['subcode']} | "
                    f"📍 {o['location']} | 🗓 {o['created_at'].strftime('%d.%m %H:%M')}\n")
        send_message(chat_id, msg)
        return

    # выбор тарифа -> показываем типы
    if data.startswith("tariff:"):
        tariff_id = data.split(":", 1)[1]

        # сохраним ИД; имя достанем позже при сохранении/подписи
        user_state[user_id] = {"tariff_id": tariff_id}
        send_type_buttons(chat_id)
        return

    # выбор типа -> показываем локации
    if data.startswith("type:"):
        type_id = data.split(":", 1)[1]
        user_state.setdefault(user_id, {})["type_id"] = type_id
        send_location_buttons(chat_id)
        return

    # выбор локации -> ищем фото, сохраняем заказ
    if data.startswith("loc:"):
        loc_id = data.split(":", 1)[1]
        st = user_state.get(user_id, {})
        tariff_id = st.get("tariff_id")
        type_id = st.get("type_id")

        if not (tariff_id and type_id):
            send_message(chat_id, "⚠️ Начните сначала: /start")
            return

        # сделаем быстрые мапы id->name (и emoji при желании)
        tariffs = {str(t["id"]): t for t in get_all_tariffs()}
        subcodes = {str(s["id"]): s for s in get_all_subcodes()}
        locations = {str(l["id"]): l for l in get_all_locations()}

        tariff = tariffs.get(str(tariff_id), {})
        subcode = subcodes.get(str(type_id), {})
        location = locations.get(str(loc_id), {})

        tariff_name = tariff.get("name", "")
        subcode_name = subcode.get("name", "")
        location_name = location.get("name", "")

        # поиск фото по именам (как было у тебя)
        result = find_photo_by_filters(tariff_name, subcode_name, location_name)
        if result:
            photo_url = f"https://drive.google.com/uc?id={result['drive_file_id']}"
            requests.post(f"{URL}/sendPhoto", json={
                "chat_id": chat_id,
                "photo": photo_url,
                "caption": f"🏙 {location_name.title()} / тариф {tariff_name}-{subcode_name}"
            })
        else:
            send_message(chat_id, "❌ Фото не найдено. Попробуйте другой набор.")

        save_order(user_id, tariff_name, subcode_name, location_name)
        send_support_link(chat_id)
        user_state.pop(user_id, None)
