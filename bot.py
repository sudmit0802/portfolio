import telebot
import confs
from telebot import types

bot = telebot.TeleBot(confs.TOKEN)

#markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#item1 = types.KeyboardButton("А Давай!😜")
#item2 = types.KeyboardButton("Не, ты скучный.")
#markup0.add(item1,item2)
#
#markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#item1 = types.KeyboardButton("Россия🇷🇺")
#item2 = types.KeyboardButton("Европа🇪🇺")
#item3 = types.KeyboardButton("США🇺🇸")
#item4 = types.KeyboardButton("Китай🇨🇳")
#markup1.row(item1, item2)
#markup1.row(item3, item4)
#
#markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#item5 = types.KeyboardButton("Москва")
#item6 = types.KeyboardButton("Санкт-Петербург")
#item7 = types.KeyboardButton("Омск")
#item8 = types.KeyboardButton("Вологда")
#markup2.row(item5, item6)
#markup2.row(item7, item8)
#
#
#
#@bot.message_handler(commands =['start'])
#
#def welcome(message):
#    sti = open('static/sticker.webp', 'rb')
#    bot.send_sticker(message.chat.id, sti)
#    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - бот <b>{1.first_name}</b>, меня написал Дима.\nДавай дружить!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup0)
#
#@bot.message_handler(content_types =['text'])
#
#def conversation(message):    
#    if message.text == "А Давай!😜":
#        bot.send_message(message.chat.id, "Итак, давай начнем, расскажи мне откуда ты?", reply_markup=markup1)
#    elif message.text == "Не, ты скучный.":
#        bot.send_message(message.chat.id, "Ну извините, меня слепили за вечер на коленке, странно, что вы ожидали большего. 🫤 Так давай дружить?", reply_markup=markup0)
#    elif(message.text == "Россия🇷🇺"):
#
#        bot.send_message(message.chat.id, "АБАЛДЕТЬ, я тоже из России! А из какого ты города?", reply_markup=markup2)
#    elif(message.text == "Европа🇪🇺" or message.text == "США🇺🇸" or message.text == "Китай🇨🇳"):
#        bot.send_message(message.chat.id, "Ой-ой, не хочу я с тобой общаться, меня так инагентом признают и удалят. Если хочешь со мной дружить, то хотя бы сделай вид, что ты из России. Ну так что, будем дружить?", reply_markup=markup0)
#    elif(message.text == "Омск"):
#        pic = open('static/picture.jpg', 'rb')
#        bot.send_photo(message.chat.id, pic)
#        omsklink = "Крутяк!\nВот кстати, что я нашел в инетернете об этом чудесном городе:\nОмск — один из крупнейших городов России, расположенный на слиянии рек Иртыша и Оми, крупный научный, культурный , спортивный и промышленный центр. Город трудовой славы.\n" + '[Читать далее](https://clck.ru/whgBR)'
#        bot.send_message(message.chat.id, omsklink, parse_mode = 'Markdown', reply_markup=types.ReplyKeyboardRemove())
#        bot.send_message(message.chat.id, "Хочешь узнать о других городах? Выбирай!", reply_markup=markup2)
#    elif(message.text == "Вологда"):
#        pic = open('static/picture1.jpg', 'rb')
#        bot.send_photo(message.chat.id, pic)
#        vologdalink = "Супер!\nВот кстати, что я нашел в инетернете об этом чудесном городе:\nВологда — город в России, административный, культурный, транспортный и научный центр Вологодской области, центр Вологодского района, в который не входит, обладая статусом города областного значения и образуя городской округ город Вологда.\n" + '[Читать далее](https://clck.ru/whq3t)'
#        bot.send_message(message.chat.id, vologdalink, parse_mode = 'Markdown', reply_markup=types.ReplyKeyboardRemove())
#        bot.send_message(message.chat.id, "Хочешь узнать о других городах? Выбирай!", reply_markup=markup2)
#    elif(message.text == "Санкт-Петербург"):
#        pic = open('static/picture2.jpg', 'rb')
#        bot.send_photo(message.chat.id, pic)
#        vologdalink = "Ничего себе!\nВот кстати, что я нашел в инетернете об этом чудесном городе:\nВторой по численности населения город РФ. Город федерального значения. Административный центр Северо-Западного федерального округа. Основан 27 мая 1703 года царём Петром I. В 1714-1728 и 1732-1918 годах - столица Российского государства.\n" + '[Читать далее](https://clck.ru/whyV4)'
#        bot.send_message(message.chat.id, vologdalink, parse_mode = 'Markdown', reply_markup=types.ReplyKeyboardRemove())
#        bot.send_message(message.chat.id, "Хочешь узнать о других городах? Выбирай!", reply_markup=markup2)
#    elif(message.text == "Москва"):
#        pic = open('static/picture3.jpg', 'rb')
#        bot.send_photo(message.chat.id, pic)
#        vologdalink = "Вот это да!\nВот кстати, что я нашел в инетернете об этом чудесном городе:\nМосква — столица России, город федерального значения, административный центр Центрального федерального округа и центр Московской области, в состав которой не входит.\n" + '[Читать далее](https://clck.ru/whxWs)'
#        bot.send_message(message.chat.id, vologdalink, parse_mode = 'Markdown', reply_markup=types.ReplyKeyboardRemove())
#        bot.send_message(message.chat.id, "Хочешь узнать о других городах? Выбирай!", reply_markup=markup2)
#    else:
#        bot.send_message(message.chat.id, "Не понимаю, о чем речь. Дружить то будем?", reply_markup=markup0)
#
#
## RUN
#

bot.polling(none_stop=True)