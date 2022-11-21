import telebot
from telebot import types # для указание типов
import config

# from games import games
# from weather import weather
hours = ["09.00 - 09.40", "09.50 - 10.30", "10.40 - 11.20", "11.30 - 12.10", "12.20 - 13.00", "13.00 - 14.00", "14.00 - 14.40", "14.50 - 15.30", "15.40 - 16.20", "16.30 - 17.10", "17.20 - 18.00"]
mon_1c_m = ["Programming Language B 205","Philosophy B 205", "Lunch", "Algebra and geometry B 205", "Discrete Math B 205"]
tue_1c_m = ["Russian Language B 203/202", "Break time", "English language B 201", "Lunch", "Programming Language B Big Lab", "Break Time"]
wed_1c_m = ["Break time", "Calculus B 202", "Lunch", "Algebra and geometry B 205", "Discrete Math B 205"]
thu_1c_m = ["Break time", "Physics B 202", "Break time", "Lunch", "Calculus B 202", "Break time"]
fri_1c_m = ["Break time", "Physics B 202", "Break time", "Lunch", "Physical education"]
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎓About AIU")
    btn2 = types.KeyboardButton("☰Schedule")
    btn3 = types.KeyboardButton("❆Weather")
    btn4 = types.KeyboardButton("💻Games")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! I am interesting & useful bot for Ala-Too International students".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🎓About AIU"):
        bot.send_message(message.chat.id, text="The state governing body of the university is the Ministry of Education and Science of the Kyrgyz Republic.The founder of Ala-Too International University is Sapat International Educational Institutions. Ala-Too International University (AIU) was established in 1996 and it is located in Bishkek, the Kyrgyz Republic.")
    elif(message.text == "❆Weather"):
        # weather()
        pass
    elif(message.text == "💻Games"):
        # games()
        pass
    elif(message.text == "☰Schedule"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Computer Science")
        btn2 = types.KeyboardButton("Applied Math & Informatics")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)

    elif(message.text == "Applied Math & Informatics"):
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
        btn1 = types.KeyboardButton("1c_m_Mon")
        btn2 = types.KeyboardButton("1c_m_Tue")
        btn3 = types.KeyboardButton("1c_m_Wed")
        btn4 = types.KeyboardButton("1c_m_Thu")
        btn5 = types.KeyboardButton("1c_m_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "1c_m_Mon"):
        bot.send_message(message.chat.id, text="\n 1 course API Monday \n 09.00 - 09.40: Programming Language B 205 \n 09.50 - 10.30: Programming Language B 205 \n 10.40 - 11.20: Programming Language B 205 \n 11.30 - 12.10: Philosophy B 205 \n 12.20 - 13.00: Philosophy B 205 \n 13.00 - 14.00: Lunch \n 14.00 - 14.40: Algebra and geometry B 205 \n 14.50 - 15.30: Algebra and geometry B 205 \n 15.40 - 16.20: Discrete Math B 205 \n 16.30 - 17.10: Discrete Math B 205 \n 17.20 - 18.00: Break time")
    elif(message.text == "1c_m_Tue"):
        bot.send_message(message.chat.id, text="\n 1 course API Tuesday \n 09.00 - 09.40: Russian Language B 203/202 \n 09.50 - 10.30: Russian Language B 203/202 \n 10.40 - 11.20: Break time \n 11.30 - 12.10: English language B 201 \n 12.20 - 13.00: English language B 201 \n 13.00 - 14.00: Lunch \n 14.00 - 14.40: Programming Language B Big Lab \n 14.50 - 15.30: Programming Language B Big Lab \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time B 205 \n 17.20 - 18.00: Break time")
    elif(message.text == "1c_m_Wed"):
        pass
    elif(message.text == "1c_m_Thu"):
        pass
    elif(message.text == "1c_m_Fri"):
        pass


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

        #Back
    elif (message.text == "Back"):
        pass
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)