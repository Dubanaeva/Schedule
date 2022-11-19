# import config
# import telebot

# bot = telebot.TeleBot(config.token)

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)

# if __name__ == '__main__':
#      bot.infinity_polling()

import telebot
from telebot import types # для указание типов
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋Say hello")
    btn2 = types.KeyboardButton("❓Schedule")
    btn3 = types.KeyboardButton("...")
    btn4 = types.KeyboardButton("💻Games")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! I am interesting & useful bot for Ala-Too International students".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋Say hello"):
        bot.send_message(message.chat.id, text="Hello dear student, welcome!")
    elif(message.text == "❓Schedule"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Computer Science")
        btn2 = types.KeyboardButton("Applied Math & Informatics")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)



        #Math
    elif(message.text == "Math"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 course API")
        btn2 = types.KeyboardButton("2 course API")
        btn3 = types.KeyboardButton("3 course API")
        btn4 = types.KeyboardButton("4 course API")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "1 course API"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Mon")
        btn2 = types.KeyboardButton("Tue")
        btn3 = types.KeyboardButton("Wed")
        btn4 = types.KeyboardButton("Thu")
        btn5 = types.KeyboardButton("Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
        math1()



        #Computer Science
    elif(message.text == "Computer Science"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 course CS")
        btn2 = types.KeyboardButton("2 course CS")
        btn3 = types.KeyboardButton("3 course CS")
        btn4 = types.KeyboardButton("4 course CS")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "1 course CS"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пн")
        btn2 = types.KeyboardButton("Вт")
        btn3 = types.KeyboardButton("Ср")
        btn4 = types.KeyboardButton("Чт")
        btn5 = types.KeyboardButton("Пт")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "Пн"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="ггг")
        back = types.KeyboardButton("Back")

        #Back
    elif (message.text == "Back"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋Say hello")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
def math1():
    if(message.text == "Mon"):
        bot.send_message(message.chat.id, text="ураа")

bot.polling(none_stop=True)