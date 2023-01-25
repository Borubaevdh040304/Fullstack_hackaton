import telebot
from telebot import types
from decouple import config


token = config('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇰🇬 Кыргыз Тили')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇰🇬 Тилди тандаңыз", reply_markup=markup)

@bot.message_handler(func=lambda x:True)
def reply_to_button(message):

    if message.text == '🇷🇺 Русский':
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton(text='Наш сайт', url='http://35.185.69.40/')
        markup.add(btn4)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт Online Restaurant", reply_markup = markup)
        markup = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text="website1", url='http://35.185.69.40/docs/')
        btn6 = types.InlineKeyboardButton(text='website2', url='http://34.123.240.158/admin/')
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, "Выберите сайт, которая вас интересует", reply_markup=markup)

    elif message.text == '🇰🇬 Кыргыз Тили':
        markup = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton(text='Биздин сайт', url='http://35.185.69.40/')
        markup.add(btn3)
        bot.send_message(message.from_user.id, "Сайтка өтүү үчүн төмөнкү баскычты басыңыз Online Restaurant", reply_markup = markup)
        markup = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text="биринчи веб сайт", url='http://35.185.69.40/docs/')
        btn6 = types.InlineKeyboardButton(text='экинчи веб сайт', url='http://35.185.69.40/admin/')
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, "Сизди кызыктырган сайтты тандаңыз", reply_markup=markup)
    else:
        bot.send_message(message.id,'Click on the button')
        bot.register_next_step_handler(message,reply_to_button)

    
 
bot.polling(none_stop=True, interval=0)



