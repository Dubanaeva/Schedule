import telebot
from telebot import types
import config
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.token)

# Namaz time

#WEATHER
r = requests.get('https://sinoptik.ua/погода-бишкек')
html = BS(r.content, "html.parser")
for el in html.select('#content'):
    #today 1nd
    day1 = el.select("#bd1 .date")[0].text
    month1 = el.select("#bd1 .month")[0].text
    wday1 = el.select("#bd1 .day-link")[0].text
    t_min1 = el.select(".temperature .min")[0].text
    t_max1 = el.select(".temperature .max")[0].text
    descr = el.select(".wDescription .description")[0].text
    #2nd
    day2 = el.select("#bd2 .date")[0].text
    month2 = el.select("#bd2 .month")[0].text
    wday2 = el.select("#bd2 .day-link")[0].text
    t_min2 = el.select(".temperature .min")[1].text
    t_max2 = el.select(".temperature .max")[1].text
    #3nd
    day3 = el.select("#bd3 .date")[0].text
    month3 = el.select("#bd3 .month")[0].text
    wday3 = el.select("#bd3 .day-link")[0].text
    t_min3 = el.select(".temperature .min")[2].text
    t_max3 = el.select(".temperature .max")[2].text
    #4nd
    day4 = el.select("#bd4 .date")[0].text
    month4 = el.select("#bd4 .month")[0].text
    wday4 = el.select("#bd4 .day-link")[0].text
    t_min4 = el.select(".temperature .min")[3].text
    t_max4 = el.select(".temperature .max")[3].text
    #5nd
    day5 = el.select("#bd5 .date")[0].text
    month5 = el.select("#bd5 .month")[0].text
    wday5 = el.select("#bd5 .day-link")[0].text
    t_min5 = el.select(".temperature .min")[4].text
    t_max5 = el.select(".temperature .max")[4].text

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎓About AIU")
    btn2 = types.KeyboardButton("☰Schedule")
    btn3 = types.KeyboardButton("❆Weather")
    btn4 = types.KeyboardButton("💻Final exams")
    btn5 = types.KeyboardButton("🍴Dining prices")
    btn6 = types.KeyboardButton("🤾Sports mugs")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! I am interesting & useful bot for Ala-Too International students".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🎓About AIU"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Back")
        markup.add(back)

        bot.send_message(message.chat.id, text="->", reply_markup=markup)
        bot.send_message(message.chat.id, text="The state governing body of the university is the Ministry of Education and Science of the Kyrgyz Republic.The founder of Ala-Too International University is Sapat International Educational Institutions. Ala-Too International University (AIU) was established in 1996 and it is located in Bishkek, the Kyrgyz Republic.")
    elif(message.text == "❆Weather"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today = types.KeyboardButton("☘Today")
        days4 = types.KeyboardButton("𝕬next4days")
        back = types.KeyboardButton("Back")
        markup.add(back, today, days4)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "☘Today"):
        bot.send_message(message.chat.id, text=("🌥Бишкек " + day1 + " " + month1 + " " + wday1 + "\n" + "💨Температура: " + t_min1 + " " + t_max1 + "\n" + "❁Описание:" + descr))
    elif(message.text == "𝕬next4days"):
        bot.send_message(message.chat.id, text=("🌥Бишкек " + day2 + " " + month2 + " " + wday2 + "\n" + "💨Температура: " + t_min2 + " " + t_max2 + "\n" + "\n" + "🌥Бишкек " + day3 + " " + month3 + " " + wday3 + "\n" + "💨Температура: " + t_min3 + " " + t_max3 + "\n" + "\n" + "🌥Бишкек " + day4 + " " + month4 + " " + wday4 + "\n" + "💨Температура: " + t_min4 + " " + t_max4 + "\n" + "\n" + "🌥Бишкек " + day5 + " " + month5 + " " + wday5 + "\n" + "💨Температура: " + t_min5 + " " + t_max5 ))
    elif(message.text == "💻Final exams"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Back")
        markup.add(back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
        # games()
        pass
    elif(message.text == "☰Schedule"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Applied Math & Informatics")
        back = types.KeyboardButton("Back")
        markup.add(btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "🍴Dining prices"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍰Sweets")
        btn2 = types.KeyboardButton("🍲Dishes")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "🍰Sweets"):
        bot.send_message(message.chat.id, text="🍰Сладости \n Медовик-60сом \n Брауни-60сом \n Чизкейк-75сом \n Печенье с ябл начин-40сом")
    elif(message.text == "🍲Dishes"):
        bot.send_message(message.chat.id, text="🥘Блюда 🍜\n Комплексный обед-130сом \n Плов-130сом \n Рис-55сом \n Пюре-55сом \n Сосиски-40сом \n Котлеты-70сом \n Куриные ножки-75сом \n Нагетсы-20сом \n Мясной подлив-65сом \n Макароны-55сом \n Вареные яйца-15сом \n Чечевичный суп-75сом \n Салаты-60сом \n Морковный салат-40сом \n Оромо-50сом \n Манты-35сом")
    elif(message.text == "Applied Math & Informatics"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 course API")
        btn2 = types.KeyboardButton("2 course API")
        btn3 = types.KeyboardButton("3 course API")
        btn4 = types.KeyboardButton("4 course API")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)

    #1 course API
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
        bot.send_message(message.chat.id, text=" 1 course API Monday \n 09.00 - 09.40: Programming Language B 205 \n 09.50 - 10.30: Programming Language B 205 \n 10.40 - 11.20: Programming Language B 205 \n 11.30 - 12.10: Philosophy B 205 \n 12.20 - 13.00: Philosophy B 205 \n 13.00 - 14.00: 🍝Lunch \n 14.00 - 14.40: Algebra and geometry B 205 \n 14.50 - 15.30: Algebra and geometry B 205 \n 15.40 - 16.20: Discrete Math B 205 \n 16.30 - 17.10: Discrete Math B 205 \n 17.20 - 18.00: Break time")
    elif(message.text == "1c_m_Tue"):
        bot.send_message(message.chat.id, text=" 1 course API Tuesday \n 09.00 - 09.40: Russian Language B 203/202 \n 09.50 - 10.30: Russian Language B 203/202 \n 10.40 - 11.20: Break time \n 11.30 - 12.10: English language B 201 \n 12.20 - 13.00: English language B 201 \n 13.00 - 14.00: 🍔Lunch \n 14.00 - 14.40: Programming Language B Big Lab \n 14.50 - 15.30: Programming Language B Big Lab \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif(message.text == "1c_m_Wed"):
        bot.send_message(message.chat.id, text="1 course API Wednesday \n 09.00 - 09.40: Break time \n 09.50 - 10.30: Break time \n 10.40 - 11.20: Calculus B 202 \n 11.30 - 12.10: Calculus B 202 \n 12.20 - 13.00: Calculus B 202 \n 13.00 - 14.00: 🍜Lunch \n 14.00 - 14.40: Algebra and geometry B 205 \n 14.50 - 15.30: Algebra and geometry B 205 \n 15.40 - 16.20: Discrete Math B 205 \n 16.30 - 17.10: Discrete Math B 205 \n 17.20 - 18.00: Break time")
    elif(message.text == "1c_m_Thu"):
        bot.send_message(message.chat.id, text="1 course API Thursday \n 09.00 - 09.40: Break time \n 09.50 - 10.30: Break time \n 10.40 - 11.20: Physics B 202 \n 11.30 - 12.10: Physics B 202 \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🍣Lunch \n 14.00 - 14.40: Calculus B 202 \n 14.50 - 15.30: Calculus B 202 \n 15.40 - 16.20: Calculus B 202 \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif(message.text == "1c_m_Fri"):
        bot.send_message(message.chat.id, text="1 course API Friday \n 09.00 - 09.40: Break time \n 09.50 - 10.30: Break time \n 10.40 - 11.20: Physics B 202 \n 11.30 - 12.10: Physics B 202 \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🌮Lunch \n 14.00 - 14.40: Physical education \n 14.50 - 15.30: Physical education \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")

    #2 course API
    elif(message.text == "2 course API"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("2c_m_Mon")
        btn2 = types.KeyboardButton("2c_m_Tue")
        btn3 = types.KeyboardButton("2c_m_Wed")
        btn4 = types.KeyboardButton("2c_m_Thu")
        btn5 = types.KeyboardButton("2c_m_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "2c_m_Mon"):
        bot.send_message(message.chat.id, text="2 course API Monday \n 09.00 - 09.40: Differetial Equations C 005 \n 09.50 - 10.30: Differetial Equations C 005 \n 10.40 - 11.20: Differetial Equations C 005 \n 11.30 - 12.10: Applied Math. Software Practice B 204 \n 12.20 - 13.00: Applied Math. Software Practice B 204 \n 13.00 - 14.00: 🧆Lunch \n 14.00 - 14.40: English language B 203 \n 14.50 - 15.30: English language B 203 \n 15.40 - 16.20: Кыргыз тили жана адабияты B 102 \n 16.30 - 17.10: Кыргыз тили жана адабияты B 102 \n 17.20 - 18.00: Спец физ-ра")
    elif(message.text == "2c_m_Tue"):
        bot.send_message(message.chat.id, text="2 course API Tuesday \n 09.00 - 09.40: Break time \n 09.50 - 10.30: Break time \n 10.40 - 11.20: Break time \n 11.30 - 12.10: Applied Math. Software Practice Lab 3 \n 12.20 - 13.00: Applied Math. Software Practice Lab 3 \n 13.00 - 14.00: 🍗Lunch \n 14.00 - 14.40: Break time  \n 14.50 - 15.30: Break time  \n 15.40 - 16.20: Кыргыз тили жана адабияты С 403 \n 16.30 - 17.10: Кыргыз тили жана адабияты С 403 \n 17.20 - 18.00: Break time")
    elif(message.text == "2c_m_Wed"):
        bot.send_message(message.chat.id, text="2 course API Wednesday \n 09.00 - 09.40: Web technologies Lab 3 \n 09.50 - 10.30: Web technologies Lab 3 \n 10.40 - 11.20: Web technologies B 201 \n 11.30 - 12.10: Web technologies B 201 \n 12.20 - 13.00: Манастануу А 309 \n 13.00 - 14.00: Манастануу А 309 \n 14.00 - 14.40: Кыргыз тили жана адабияты С 403(inter stud) \n 14.50 - 15.30: Кыргыз тили жана адабияты С 403(inter stud) \n 15.40 - 16.20: Calculus B 203 \n 16.30 - 17.10: Calculus B 203 \n 17.20 - 18.00: Calculus B 203")
    elif(message.text == "2c_m_Thu"):
        bot.send_message(message.chat.id, text="2 course API Thursday \n 09.00 - 09.40:  Break time \n 09.50 - 10.30: Break time \n 10.40 - 11.20: Break time \n 11.30 - 12.10: Break time \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🍖Lunch \n 14.00 - 14.40: Differetial Equations B 202 \n 14.50 - 15.30: Differetial Equations B 202 \n 15.40 - 16.20: Differetial Equations B 202 \n 16.30 - 17.10: Break time B 205 \n 17.20 - 18.00: Break time ")
    elif(message.text == "2c_m_Fri"):
        bot.send_message(message.chat.id, text="2 course API Friday \n 09.00 - 09.40: Calculus B 203 \n 09.50 - 10.30: Calculus B 203 \n 10.40 - 11.20: Calculus B 203 \n 11.30 - 12.10: Physical education \n 12.20 - 13.00: Physical education \n 13.00 - 14.00: 🥘Lunch \n 14.00 - 14.40: Кыргыз тили жана адабияты B 202 \n 14.50 - 15.30: Кыргыз тили жана адабияты B 202 \n 15.40 - 16.20: Web technologies B 203 \n 16.30 - 17.10: Web technologies B 203 \n 17.20 - 18.00: Break time")

    #3 course
    elif(message.text == "3 course API"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("3c_m_Mon")
        btn2 = types.KeyboardButton("3c_m_Tue")
        btn3 = types.KeyboardButton("3c_m_Wed")
        btn4 = types.KeyboardButton("3c_m_Thu")
        btn5 = types.KeyboardButton("3c_m_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "3c_m_Mon"):
        bot.send_message(message.chat.id, text="3 course API Monday \n 09.00 - 09.40: Equations of the Mathematical Physics B 201 \n 09.50 - 10.30: Equations of the Mathematical Physics B 201 \n 10.40 - 11.20: Break time \n 11.30 - 12.10: Numerical Methods (online) \n 12.20 - 13.00: Numerical Methods (online) \n 13.00 - 14.00: Numerical Methods (online) \n 14.00 - 14.40: Break time \n 14.50 - 15.30: Break time \n 15.40 - 16.20: Algorithms and Data Structures B 204 \n 16.30 - 17.10: Algorithms and Data Structures B 204 \n 17.20 - 18.00: Algorithms and Data Structures B 204")
    elif(message.text == "3c_m_Tue"):
        bot.send_message(message.chat.id, text="3 course API Tuesday \n 09.00 - 09.40: Break time \n 09.50 - 10.30: Probability Theory and Statistics Lab 3 \n 10.40 - 11.20: Probability Theory and Statistics Lab 3 \n 11.30 - 12.10: Probability Theory and Statistics B 204 \n 12.20 - 13.00: Probability Theory and Statistics B 204 \n 13.00 - 14.00: Lunch \n 14.00 - 14.40: Languages&Methods of Prog(Java) Lab3 \n 14.50 - 15.30: Languages&Methods of Prog(Java) Lab3  \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif(message.text == "3c_m_Wed"):
        bot.send_message(message.chat.id, text="3 course API Wednesday \n 09.00 - 09.40: Break time \n 09.50 - 10.30: Break time \n 10.40 - 11.20: Break time \n 11.30 - 12.10: Break time \n 12.20 - 13.00: Break time \n 13.00 - 14.00: Lunch \n 14.00 - 14.40: Languages&Methods of Prog(Java) Lab3 \n 14.50 - 15.30: Languages&Methods of Prog(Java) Lab3 \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif(message.text == "3c_m_Thu"):
        bot.send_message(message.chat.id, text="3 course API Thursday \n 09.00 - 09.40: Equations of the Mathematical Physics B 201 \n 09.50 - 10.30: Equations of the Mathematical Physics B 201 \n 10.40 - 11.20: Equations of the Mathematical Physics B 201 \n 11.30 - 12.10: Scientific Programming B 204 \n 12.20 - 13.00: Scientific Programming B 204 \n 13.00 - 14.00: Lunch \n 14.00 - 14.40: Break \n 14.50 - 15.30: Break \n 15.40 - 16.20: Numerical Methods & Analysis (online) \n 16.30 - 17.10: Numerical Methods & Analysis (online) \n 17.20 - 18.00: Break time ")
    elif(message.text == "3c_m_Fri"):
        bot.send_message(message.chat.id, text="3 course API Friday \n 09.00 - 09.40: Comp.Networks Lab 4 \n 09.50 - 10.30: Comp.Networks Lab 4 \n 10.40 - 11.20: Scientific Programming Lab 3 \n 11.30 - 12.10: Scientific Programming Lab 3 \n 12.20 - 13.00: Break \n 13.00 - 14.00: Lunch \n 14.00 - 14.40: Comp.Networks \n 14.50 - 15.30: Comp.Networks \n 15.40 - 16.20: Comp.Networks \n 16.30 - 17.10: Comp.Networks B 203 \n 17.20 - 18.00: Break time")

    #4 course
    elif(message.text == "4 course API"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("4c_m_Mon")
        btn2 = types.KeyboardButton("4c_m_Tue")
        btn3 = types.KeyboardButton("4c_m_Wed")
        btn4 = types.KeyboardButton("4c_m_Thu")
        btn5 = types.KeyboardButton("4c_m_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "4c_m_Mon"):
        bot.send_message(message.chat.id, text="4 course API Monday \n ")
    elif(message.text == "4c_m_Tue"):
        bot.send_message(message.chat.id, text="4 course API Tuesday \n ")
    elif(message.text == "4c_m_Wed"):
        bot.send_message(message.chat.id, text="4 course API Wednesday \n ")
    elif(message.text == "4c_m_Thu"):
        bot.send_message(message.chat.id, text="4 course API Thursday \n ")
    elif(message.text == "4c_m_Fri"):
        bot.send_message(message.chat.id, text="4 course API Friday \n ")

        #Back
    elif(message.text == "Back"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🎓About AIU")
        button2 = types.KeyboardButton("☰Schedule")
        button3 = types.KeyboardButton("❆Weather")
        button4 = types.KeyboardButton("💻Final exams")
        button5 = types.KeyboardButton("🍴Dining prices")
        button6 = types.KeyboardButton("🤾Sports mugs")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, text="You are on the main menu 🥰", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="I did not program for such a command ☹️")

bot.polling(none_stop=True)
