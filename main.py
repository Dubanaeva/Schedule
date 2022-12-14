import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot("5788489755:AAGzRBtcg1zDAPXK4SiBFHOZhsSP4i1NDq8")

r = requests.get("https://sinoptik.ua/погода-бишкек")
html = BS(r.content, "html.parser")
for el in html.select('#content'):

    day1 = el.select("#bd1 .date")[0].text
    month1 = el.select("#bd1 .month")[0].texts
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
    btn1 = types.KeyboardButton("☰Schedule")
    btn2 = types.KeyboardButton("❆Weather")
    btn3 = types.KeyboardButton("💻Final exams")
    btn4 = types.KeyboardButton("🍴Dining prices")
    btn5 = types.KeyboardButton("🤾Sports mugs")
    btn6 = types.KeyboardButton("Namaz time")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! I am interesting & useful bot for Ala-Too International students".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Namaz time"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('JAN')
        item2 = types.KeyboardButton('FEB')
        item3 = types.KeyboardButton('MAR')
        item4 = types.KeyboardButton('APR')
        item5 = types.KeyboardButton('MAY')
        item6 = types.KeyboardButton('JUN')
        item7 = types.KeyboardButton('JUL')
        item8 = types.KeyboardButton('AUG')
        item9 = types.KeyboardButton('SEP')
        item10 = types.KeyboardButton('OCT')
        item11 = types.KeyboardButton('NOV')
        item12 = types.KeyboardButton('DEC')
        markup.add(item, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    if message.text == 'JAN':
        bot.send_message(message.chat.id, text = 'JANUARY:\nFadjr: 6:38, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:07, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 16:15, 4 rakats Fardh\nMaghrib: 18:06,3 rakats Fardh,2 rakats Sunnah\nIsha: 19:48, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'FEB':
        bot.send_message(message.chat.id, text = 'FEBRUARY:\nFadjr: 6:21, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:17, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 16:35, 4 rakats Fardh\nMaghrib: 18:33, 3 rakats Fardh,2 rakats Sunnah\nIsha: 20:10, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'MAR':
        bot.send_message(message.chat.id, text = 'MARCH:\nFadjr: 6:00, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:16, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 17:07, 4 rakats Fardh\nMaghrib: 19:10, 3 rakats Fardh,2 rakats Sunnah\nIsha: 21:00, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'APR':
        bot.send_message(message.chat.id, text = 'APRIL:\nFadjr: 5:05, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:08, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 17:36, 4 rakats Fardh\nMaghrib: 19:29, 3 rakats Fardh,2 rakats Sunnah\nIsha: 21:29, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'MAY':
        bot.send_message(message.chat.id, text = 'MAY:\nFadjr: 4:04, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:07, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 17:58, 4 rakats Fardh\nMaghrib: 20:04, 3 rakats Fardh,2 rakats Sunnah\nIsha: 22:11, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'JUN':
        bot.send_message(message.chat.id, text = 'JUNE:\nFadjr: 3:13, 2 rakats Sunnah,2 rakats Fardh\nZuhr: 13:07, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 18:17, 4 rakats Fardh\nMaghrib: 20:35, 3 rakats Fardh,2 rakats Sunnah\nIsha: 22:37, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'JUL':
        bot.send_message(message.chat.id, text = 'JULY:\nFadjr: 3:08, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:07, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 18:25, 4 rakats Fardh\nMaghrib: 20:46, 3 rakats Fardh,2 rakats Sunnah\nIsha: 22:52, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'AUG':
        bot.send_message(message.chat.id, text = 'AUGUST:\nFadjr: 3:53, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:10, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 18:15, 4 rakats Fardh\nMaghrib: 20:05, 3 rakats Fardh,2 rakats Sunnah\nIsha: 22:06, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'SEP':
        bot.send_message(message.chat.id, text = 'SEPTEMBER:\nFadjr: 5:06, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 13:04, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 17:17, 4 rakats Fardh\nMagrib: 19:16, 3 rakats Fardh,2 rakats Sunnah\nIsha: 21:11, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'OCT':
        bot.send_message(message.chat.id, text = 'OCTOBER:\nFadjr: 5:22, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 12:53, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 16:59, 4 rakats Fardh\nMaghrib: 18:45, 3 rakats Fardh,2 rakats Sunnah\nIsha: 20:14, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'NOV':
        bot.send_message(message.chat.id, text = 'NOVEMBER:\nFadjr: 6:17, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 12:47, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 16:14, 4 rakats Fardh\nMaghrib: 17:54, 3 rakats Fardh,2 rakats Sunnah\nIsha: 19:27, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')
    elif message.text == 'DEC':
        bot.send_message(message.chat.id, text = 'DECEMBER:\nFadjr: 6:29, 2 rakats Sunnah,2 rakats Fardh\nDhuhr: 12:53, 4 rakats Sunnah,4 rakats Fardh,2 rakats Sunnah\nAsr: 15:47, 4 rakats Fardh\nMaghrib: 17:29, 3 rakats Fardh,2 rakats Sunnah\nIsha: 19:06, 4 rakats Fardh,2 rakats Sunnah, 3 rakats Witr')

    elif(message.text == "❆Weather"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today = types.KeyboardButton("☘Today")
        days4 = types.KeyboardButton("𝕬next4days")
        back = types.KeyboardButton("Back")
        markup.add(back, today, days4)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "☘Today"):
        bot.send_message(message.chat.id, text=("🌥Бишкек " + str(day1) + " " + str(month1) + " " + str(wday1) + "\n" + "💨Температура: " + t_min1 + " " + t_max1 + "\n" + "❁Описание:" + descr))
    elif(message.text == "𝕬next4days"):
        bot.send_message(message.chat.id, text=("🌥Бишкек " + day2 + " " + month2 + " " + wday2 + "\n" + "💨Температура: " + t_min2 + " " + t_max2 + "\n" + "\n" + "🌥Бишкек " + day3 + " " + month3 + " " + wday3 + "\n" + "💨Температура: " + t_min3 + " " + t_max3 + "\n" + "\n" + "🌥Бишкек " + day4 + " " + month4 + " " + wday4 + "\n" + "💨Температура: " + t_min4 + " " + t_max4 + "\n" + "\n" + "🌥Бишкек " + day5 + " " + month5 + " " + wday5 + "\n" + "💨Температура: " + t_min5 + " " + t_max5 ))
    elif(message.text == "💻Final exams"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        math = types.KeyboardButton("📚‍💻math")
        cs = types.KeyboardButton("👨🏻🖥️cs")
        back = types.KeyboardButton("Back")
        markup.add(math, cs, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    #Math Buttons
    elif (message.text == "📚‍💻math"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        math1 = types.KeyboardButton("math1_F_1s")
        math2 = types.KeyboardButton("math2_F_1s")
        math3 = types.KeyboardButton("math3_F_1s")
        math4 = types.KeyboardButton("math4_F_1s")
        back = types.KeyboardButton("Back")
        markup.add(math1, math2, math3, math4, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    #Computer Science Buttons
    elif (message.text == "👨🏻🖥️cs"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        math1 = types.KeyboardButton("cs1_F_1s")
        math2 = types.KeyboardButton("cs2_F_1s")
        math3 = types.KeyboardButton("cs3_F_1s")
        math4 = types.KeyboardButton("cs4_F_1s")
        back = types.KeyboardButton("Back")
        markup.add(math1, math2, math3, math4, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    #Math Final Schedule
    elif (message.text == "math1_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n 12.12.2022 (Monday) \n Philosophy 11:30-12:30 B 205 M.Edilova \n \n 13.12.2022 (Tuesday) \n Russian Language 10:30-11:30 Big Lab/Lab 3/Lab 4 Alymbekova S/Chokusheva.G \n Calculus-1 14:00-16:00 B 202 Mr.Husein/Remudin  \n \n 15.12.2022 (Thursday) \n Algebra and Geometry 14:00-16:00 Lab 5 R.Mekuria \n \n 16.12.2022 (Friday) \n Physical Training 9:00-10:00 I.Chalova \n Physics-1 10:30-11:30 B 203 Ms.Asia \n \n 19.12.2022 (Monday) \n Programming Language 1 9:00-10:00 Big Lab Zhumaniiaz Mamataliev \n \n 20.12.2022 (Tuesday) \n Discrete Math 14:00-15:30 Lab 5 Dr.Remudin \n \n 21.12.2022 (Wednesday) \n English 10:30-11:30 B 205 Mr.Murray")
    elif (message.text == "math2_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n 12.12.2022 (Monday) \n Kyrgyz Language 13:00-14:00 B 201 D.Orozalieva\n \n 13.12.2022 (Tuesday) \n Applied Math. Software 11:45-12:45 Lab 3 Zh.Mamataliev \n Иностр.студ. (кыргыз.яз) 13:00-14:00 Big lab A. Saidalieva \n \n 14.12.2022(Wednesday) \n Манастануу 13:00-14:00 403С Zhuzupekova K \n \n 16.12.2022 (Friday) \n Physical training 13:00-14:00 Z. Kamchibekova/ Z. Chynybekov \n \n 19.12.2022 (Monday) \n Calculus III 14:00-15:30 B 203 Mr. Hussien 20.12.2022 (Tuesday) \n English III 14:30-15:30 B 201 Mr. Murray 21.12.2022 (Wednesday) \n Web Technologies 13:00-14:00 Lab 3 Zh.Hamidov \n \n 23.12.2022 (Friday) \n Differential Equations 14:00-15:00 B 204 Diana Zhumantaeva")
    elif (message.text == "math3_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n 12.12.2022 (Monday) \n Equations of the Mathematical Physics I 9:00-10:00 B 201 Dr. Tauheed \n \n 13.12.2022 (Tuesday) \n Probability Theory and Statistics I 14:30-16:00 Lab3 Dr Nurbek \n \n 14.12.2022 (Wednesday) \n Languages&Methods of Prog. I(Java) 10:30-11:30 B 201 A. Kibekbaev \n \n 15.12.2022 (Thursday) \n Scientific Programming 9:00-10:00 Lab 3 Zhumaniiaz Mamataliev \n \n 16.12.2022 (Friday) \n Comp. Networks 9:00-10:00 Lab 4 Mr. Imtiyaz \n \n 19.12.2022 (Monday) \n Numerical Methods 10:30-11:30 online Omer Gurbuz")
    elif (message.text == "math4_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Number Theory 14:00-15:30 B 202 Mr. Hussien \n \n 13.12.2022 (Tuesday) \n Information Security 13:00-14:00 Project Mr. Imtiyaz \n \n 14.12.2022 (Wednesday) \n Data Science 13:00-14:00 B 202 Dr Arslan \n \n 15.12.2022 (Thursday) \n Optimization Methods 10:30-11:30 Lab3 Zh. Mamataliev \n \n 19.12.2022 (Monday) \n Computer Architecture 14:30-15:30 B 202 Mr Arslan \n \n 20.12.2022 (Tuesday) \n Operating Systems 14:30-15:30 B 202 Dr Arslan \n \n 21.12.2022 (Wednesday) \n Research Methods 14:30-15:30 B 201 Dr. Remudin \n \n 22.12.2022 (Thursday) \n Computer Graphics 12:00-13:00 Lab 4 Mr.Andrey")

        #Computer Science Final

        # CS 1 course F schedule
    elif (message.text == "cs1_F_1s"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("cs1A_F_1s")
        btn2 = types.KeyboardButton("cs1B_F_1s")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "cs1A_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Elective: Infromation Security, Graphic Design, Data Science  13:00-14:00 COM-22 (AB) Project/ Lab 4/ Lab 3 I. Gulbarga/ A. Ermakov/ A. Khan \n Physical training 15:00-16:00 COM-22 (AB) Z. Kamchibekova/ Z. Chynybekov \n \n 13.12.2022 (Tuesday) \n Russian language + foreigners 10:30-11:30 COM-22 (AB) Lab 3/ Lab 4/ Big Lab/ S. Alymbekova/G. Chokusheva/ A. Orozova \n Calculus-I 14:00-16:00 COM-22 (AB) B 205/ B203 H. Chebsi/ T. Khan \n \n 14.12.22 (Wednesday) Kyrgyz language for foreigners 14:00-15:00 B 111 A. Saidalieva \n Introduction to Eng.&CS 10:00-11:30 COM-22 (AB) Online B. Shambetova \n \n 15.12.2022 (Thursday) Elective - English 13:00-14:00 COM-22 (A) B204 E. Murray \n Algebra and Geometry 14:00-15:30 COM-22 (AB) Big Lab/Lab3/Lab5 for MAT R. Mekuria/ I. Gulbarga/ Mekia Shigute Gaso \n \n 16.12.2022 (Friday) Elective - Languages: English for B group, French, German, Chinese 09:00-10:00 COM-22 B203/B204/В201/В202 E. Murray/ I. Abdimitalieva/ A. Zhumalieva 19.12.2022 (Monday) Programming Languages - I 10:30-12:00 COM-22 (AB) Big Lab/ Lab 3 Mekia Shigute Gaso \n \n 20.12.2022 (Tuesday) \n Elective: Engineering Computer Graphics, Physics 11:00-12:00 COM-22 (AB) Lab 3/ Online A. Ermakov/ R. Isaev ")
    elif (message.text == "cs1B_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Elective: Infromation Security, Graphic Design, Data Science  13:00-14:00 COM-22 (AB) Project/ Lab 4/ Lab 3 I. Gulbarga/ A. Ermakov/ A. Khan \n Physical training 15:00-16:00 COM-22 (AB) Z. Kamchibekova/ Z. Chynybekov \n \n 13.12.2022 (Tuesday) \n Russian language + foreigners 10:30-11:30 COM-22 (AB) Lab 3/ Lab 4/ Big Lab/ S. Alymbekova/G. Chokusheva/ A. Orozova \n Calculus-I 14:00-16:00 COM-22 (AB) B 205/ B203 H. Chebsi/ T. Khan \n \n 14.12.22 (Wednesday) Kyrgyz language for foreigners 14:00-15:00 B 111 A. Saidalieva \n Introduction to Eng.&CS 10:00-11:30 COM-22 (AB) Online B. Shambetova \n \n 15.12.2022 (Thursday) Elective - English 13:00-14:00 COM-22 (A) B204 E. Murray \n Algebra and Geometry 14:00-15:30 COM-22 (AB) Big Lab/Lab3/Lab5 for MAT R. Mekuria/ I. Gulbarga/ Mekia Shigute Gaso \n \n 16.12.2022 (Friday) Elective - Languages: English for B group, French, German, Chinese 09:00-10:00 COM-22 B203/B204/В201/В202 E. Murray/ I. Abdimitalieva/ A. Zhumalieva 19.12.2022 (Monday) Programming Languages - I 10:30-12:00 COM-22 (AB) Big Lab/ Lab 3 Mekia Shigute Gaso \n \n 20.12.2022 (Tuesday) \n Elective: Engineering Computer Graphics, Physics 11:00-12:00 COM-22 (AB) Lab 3/ Online A. Ermakov/ R. Isaev ")

    # CS 2 course F schedule

    elif (message.text == "cs2_F_1s"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("cs2A_F_1s")
        btn2 = types.KeyboardButton("cs2B_F_1s")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "cs2A_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Electrotechnics & Electronics 13:00-14:00 COM-21 (B) Big Lab T. Khan \n Electrotechnics & Electronics 14:30-15:30 COM-21 (A) Big Lab T. Khan \n \n 13.12.2022 (Tuesday) \n Kyrgyz language 13:00-14:00 COM-21 (AB) Lab3/ Lab4/ Big Lab/ ? A. Saidalieva/G. Samatova/N. Kazakova/ K. Zhuzupekova \n Physical training 14:00-15:00 COM-21 (AB) Z. Kamchibekova/ I. Chalova \n \n 14.12.22 (Wednesday) \n Object Oriented Programming 13:00-14:00 COM-21 (A) B205 A. Kibekbaev \n Object Oriented Programming 14:30-15:30  COM-21(B) B205 A. Kibekbaev \n \n 15.12.2022 (Thursday) \n Database Systems 12:00-13:00 COM-21 (AB) В205 N. Abdullaev \n \n 16.12.2022 (Friday) \n Turkish Languages - ll 10:30-11:30 COM-21 (AB) B 201/ B202/ ?// Lab 4 E. Usupova/ Zulfizar/ M. Mujde/ A. Beysheeva \n \n 19.12.2022 (Monday) \n Web Technologies 13:00-14:00 COM-21(B) B 205 R.Isaev \n Web Technologies 14:30-15:30 COM-21 (A) B 205 R.Isaev \n \n 20.12.2022 (Tuesday) \n Discrete Mathematics 14:00-15:30 COM-21 (AB) Big Lab/Lab3/Lab5 for MAT R. Mekuria/ H. Chebsi/ T. Khan")
    elif (message.text == "cs2B_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Electrotechnics & Electronics 13:00-14:00 COM-21 (B) Big Lab T. Khan \n Electrotechnics & Electronics 14:30-15:30 COM-21 (A) Big Lab T. Khan \n \n 13.12.2022 (Tuesday) \n Kyrgyz language 13:00-14:00 COM-21 (AB) Lab3/ Lab4/ Big Lab/ ? A. Saidalieva/G. Samatova/N. Kazakova/ K. Zhuzupekova \n Physical training 14:00-15:00 COM-21 (AB) Z. Kamchibekova/ I. Chalova \n \n 14.12.22 (Wednesday) \n Object Oriented Programming 13:00-14:00 COM-21 (A) B205 A. Kibekbaev \n Object Oriented Programming 14:30-15:30  COM-21(B) B205 A. Kibekbaev \n \n 15.12.2022 (Thursday) \n Database Systems 12:00-13:00 COM-21 (AB) В205 N. Abdullaev \n \n 16.12.2022 (Friday) \n Turkish Languages - ll 10:30-11:30 COM-21 (AB) B 201/ B202/ ?// Lab 4 E. Usupova/ Zulfizar/ M. Mujde/ A. Beysheeva \n \n 19.12.2022 (Monday) \n Web Technologies 13:00-14:00 COM-21(B) B 205 R.Isaev \n Web Technologies 14:30-15:30 COM-21 (A) B 205 R.Isaev \n \n 20.12.2022 (Tuesday) \n Discrete Mathematics 14:00-15:30 COM-21 (AB) Big Lab/Lab3/Lab5 for MAT R. Mekuria/ H. Chebsi/ T. Khan")

        # CS 3 course F schedule

    elif (message.text == "cs3_F_1s"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("cs3A_F_1s")
        btn2 = types.KeyboardButton("cs3B_F_1s")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "cs3A_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Software Engineering - I 10:30-11:30 COM-20 Lab 4 Ch. Esenbekov \n \n 13.12.2022 (Tuesday) \n Comp. Networks&Telecommunication 14:30-15:30 COM-20 Big Lab I. Gulbarga \n \n 14.12.22 (Wednesday) \n Introduction to Enterpreunership 14:30-15:30 COM-20 B 203 A. Khan \n \n 15.12.2022 (Thursday) \n Mobile App Development 09:00-12:00 COM-20 (A) Big Lab N. Abdullaev \n Mobile App Development 14:00-17:00 COM-20 (B) Lab 4 N. Abdullaev \n \n 16.12.2022 (Friday) \n Design & Analysis of Algorithms 09:00-11:00 COM-20 (AB) Big Lab/ Lab 3 Mekia Shigute Gaso \n \n 19.12.2022 (Monday) \n Probability and Statistics 12:00-13:00 COM-20 (AB) B 205 O. Gurbuz")
    elif (message.text == "cs3B_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Software Engineering - I 10:30-11:30 COM-20 Lab 4 Ch. Esenbekov \n \n 13.12.2022 (Tuesday) \n Comp. Networks&Telecommunication 14:30-15:30 COM-20 Big Lab I. Gulbarga \n \n 14.12.22 (Wednesday) \n Introduction to Enterpreunership 14:30-15:30 COM-20 B 203 A. Khan \n \n 15.12.2022 (Thursday) \n Mobile App Development 09:00-12:00 COM-20 (A) Big Lab N. Abdullaev \n Mobile App Development 14:00-17:00 COM-20 (B) Lab 4 N. Abdullaev \n \n 16.12.2022 (Friday) \n Design & Analysis of Algorithms 09:00-11:00 COM-20 (AB) Big Lab/ Lab 3 Mekia Shigute Gaso \n \n 19.12.2022 (Monday) \n Probability and Statistics 12:00-13:00 COM-20 (AB) B 205 O. Gurbuz")

    # CS 4 course F schedule
    elif(message.text == "cs4_F_1s"):
        bot.send_message(message.chat.id, text="📅🗓📆-> \n  12.12.2022 (Monday) \n Designing in C# 10:30-11:30 Big Lab G. Esenalieva \n \n 13.12.2022 (Tuesday) \n Front-end 10:30-11:30 Online R. Isaev \n \n 14.12.22 (Wednesday) \n Information Security 10:30-11:30 Project I. Gulbarga \n Elective: Introduction to Data Mining, Software Architecture & Design patterns 12:00-13:00 B205/ Online A. Kibekbaev/ R. Isaev \n \n 15.12.2022 (Thursday) \n Machine Learning 09:00-10:00 Lab 4 A. Khan \n \n 16.12.2022 (Friday) \n HCI 10:30-11:30 Online B. Shambetova \n \n 19.12.2022 (Monday) \n Elective: Image Processing, Robotics 10:30-11:30 Lab 4/ Online T. Khan/ R. Isaev \n \n 20.12.2022 (Tuesday) \n Enterprise Resource Planning 13:00-14:00 Lab 4 A. Khan")



    elif(message.text == "☰Schedule"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Computer Science")
        btn2 = types.KeyboardButton("Applied Math & Informatics")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
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
        bot.send_message(message.chat.id, text="4 course API Monday \n 09.00 - 09.40: Computer Architecture B 203 \n 09.50 - 10.30: Computer Architecture B 203 \n 10.40 - 11.20: Computer Architecture B 203 \n 11.30 - 12.10: Break time \n 12.20 - 13.00: Information Security  Lab 3 \n 13.00 - 14.00: Information Security  Lab 3 \n 14.00 - 14.40: Number Theory B 201 \n 14.50 - 15.30: Number Theory B 201 \n 15.40 - 16.20: Number Theory B 201 \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time ")
    elif(message.text == "4c_m_Tue"):
        bot.send_message(message.chat.id, text="4 course API Tuesday \n 09.00 - 09.40: Operating systems B 110 \n 09.50 - 10.30: Operating systems B 110 \n 10.40 - 11.20:  Break time  \n 11.30 - 12.10: Information Security Lab 4 \n 12.20 - 13.00: Information Security Lab 4 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Data Science B 201 \n 14.50 - 15.30: Data Science B 201 \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif(message.text == "4c_m_Wed"):
        bot.send_message(message.chat.id, text="4 course API Wednesday \n 09.00 - 09.40: Number Theory B 204 \n 09.50 - 10.30: Number Theory B 204  \n 10.40 - 11.20: Operating Systems B 203 \n 11.30 - 12.10: Operating Systems B 203 \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🍉Lunch \n 14.00 - 14.40: Data Science B 202 \n 14.50 - 15.30: Data Science B 202 \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time ")
    elif(message.text == "4c_m_Thu"):
        bot.send_message(message.chat.id, text="4 course API Thursday \n 09.00 - 09.40: Optimization Methods Lab 3 \n 09.50 - 10.30: Optimization Methods Lab 3 \n 10.40 - 11.20: Break time \n 11.30 - 12.10: Break time \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🍏Lunch \n 14.00 - 14.40: Computer Graphics Lab 4 \n 14.50 - 15.30: Computer Graphics Lab 4 \n 15.40 - 16.20: Computer Graphics Lab 4 \n 16.30 - 17.10: Break time  \n 17.20 - 18.00: Break time ")
    elif(message.text == "4c_m_Fri"):
        bot.send_message(message.chat.id, text="4 course API Friday \n 09.00 - 09.40: Optimization Methods  Big Lab \n 09.50 - 10.30: Optimization Methods  Big Lab \n 10.40 - 11.20: Research Methods B 204 \n 11.30 - 12.10: Research Methods B 204 \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🍓Lunch \n 14.00 - 14.40: Break time \n 14.50 - 15.30: Break time \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time B 203 \n 17.20 - 18.00: Break time")

    #Computer Science

    elif (message.text == "Computer Science"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 course CS")
        btn2 = types.KeyboardButton("2 course CS")
        btn3 = types.KeyboardButton("3 course CS")
        btn4 = types.KeyboardButton("4 course CS")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)

        # 1 course API
    elif (message.text == "1 course CS"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1c_csA")
        btn2 = types.KeyboardButton("1c_csB")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif(message.text == "1c_csA"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1c_csA_Mon")
        btn2 = types.KeyboardButton("1c_csA_Tue")
        btn3 = types.KeyboardButton("1c_csA_Wed")
        btn4 = types.KeyboardButton("1c_csA_Thu")
        btn5 = types.KeyboardButton("1c_csA_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "1c_csB"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1c_csB_Mon")
        btn2 = types.KeyboardButton("1c_csB_Tue")
        btn3 = types.KeyboardButton("1c_csB_Wed")
        btn4 = types.KeyboardButton("1c_csB_Thu")
        btn5 = types.KeyboardButton("1c_csB_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)

        #A

    elif (message.text == "1c_csA_Mon"):
        bot.send_message(message.chat.id, text="1 course CS-A Monday \n 09.00 - 09.40: Physical Training \n 09.50 - 10.30: Physical Training \n 10.40 - 11.20: Elective English B 202 \n 11.30 - 12.10: Elective English B 202 \n 12.20 - 13.00: [Elective] Information Security B  210 \n 13.00 - 14.00: [Elective] Information Security B  210 \n 14.00 - 14.40: [Elective] Graphics Design Lab 3 - B 210 \n 14.50 - 15.30: Elective] Graphics Design Lab 3 - B 210 \n 15.40 - 16.20: Elective] Graphics Design Lab 3 - B 210 \n 16.30 - 17.10: Elective] Graphics Design Lab 3 - B 210 \n 17.20 - 18.00: Break time")
    elif (message.text == "1c_csA_Tue"):
        bot.send_message(message.chat.id, text="1 course CS-A Tuesday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Algebra and Geometry B 102 \n 10.40 - 11.20:  Algebra and Geometry B 102 \n 11.30 - 12.10: Russian language B 202/203 \n 12.20 - 13.00: Russian language B 202/203 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Calculus B 205 \n 14.50 - 15.30: Calculus B 205 \n 15.40 - 16.20: Calculus B 205 \n 16.30 - 17.10: Russian Language (for foreigners) B 109 \n 17.20 - 18.00: Russian Language (for foreigners) B 109")
    elif (message.text == "1c_csA_Wed"):
        bot.send_message(message.chat.id, text="1 course CS-A Wednesday \n 09.00 - 09.40: Introduction to Eng.&Cs B 205 \n 09.50 - 10.30: Introduction to Eng.&Cs B 205 \n 10.40 - 11.20: Programming Languages B 204 \n 11.30 - 12.10: Programming Languages B 204 \n 12.20 - 13.00: Programming Languages B 204 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: [Elective] Data Science B 202 \n 14.50 - 15.30: [Elective] Engineering Computer Graphics Lab 4 & B 211/ Physics B 200 \n 15.40 - 16.20: [Elective] Engineering Computer Graphics Lab 4 & B 211/ Physics B 200 \n 16.30 - 17.10: Russian Language Practic course B 109 \n 17.20 - 18.00: Russian Language Practic course B 109 ")
    elif (message.text == "1c_csA_Thu"):
        bot.send_message(message.chat.id, text="1 course CS-A Thursday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Introduction to Eng.&Cs Big Lab \n 10.40 - 11.20: Introduction to Eng.&Cs Big Lab \n 11.30 - 12.10: Algebra and Geometry B 201 \n 12.20 - 13.00: Algebra and Geometry B 201 \n 13.00 - 14.00: 🍛Lunch \n 14.00 - 14.40: Programming Languages B 208 \n 14.50 - 15.30: Programming Languages B 208 \n 15.40 - 16.20: Programming Languages B 208 \n 16.30 - 17.10: [Elective] Data Science B 202 \n 17.20 - 18.00: [Elective] Data Science B 202 ")
    elif (message.text == "1c_csA_Fri"):
        bot.send_message(message.chat.id, text="1 course CS-A Friday \n 09.00 - 09.40: Elective English B 201 \n 09.50 - 10.30: Elective English B 201 \n 10.40 - 11.20: Elective French B 205\n 11.30 - 12.10: Elective French B 205 \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🥦Lunch \n 14.00 - 14.40: Calculus B 204 \n 14.50 - 15.30: Calculus B 204 \n 15.40 - 16.20: Calculus B 204 16.30 - 17.10: Physical training special group \n 17.20 - 18.00: Physical training special group")

    #B

    elif (message.text == "1c_csB_Mon"):
        bot.send_message(message.chat.id, text="1 course CS-B Monday \n 09.00 - 09.40: Elective English B 202 \n 09.50 - 10.30: Elective English B 202 \n 10.40 - 11.20: Programming Languages B 104 \n 11.30 - 12.10: Programming Languages B 104 \ n 12.20 - 13.00: Programming Languages B 104 \n 13.00 - 14.00: 🍓 Lunch \n 14.00 - 14.40: [Elective] Graphics Design Lab 3 - B 210 \n 14.50 - 15.30: Elective] Graphics Design Lab 3 - B 210 \n 15.40 - 16.20: Elective] Graphics Design Lab 3 - B 210 \n 16.30 - 17.10: Elective] Graphics Design Lab 3 - B 210 \n 17.20 - 18.00: Break time ")
    elif (message.text == "1c_csB_Tue"):
        bot.send_message(message.chat.id, text="1 course CS-B Tuesday \n 09.00 - 09.40: Physical Training \n 09.50 - 10.30: Physical Training \n 10.40 - 11.20:  Calculus B 205 \n 11.30 - 12.10: Calculus B 205 \n 12.20 - 13.00: Calculus B 205 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Russian language B 202/203 \n 14.50 - 15.30: Russian language B 202/203 \n 15.40 - 16.20: Algebra and Geometry B 201 \n 16.30 - 17.10: Algebra and Geometry B 201 \n 17.20 - 18.00: Russian Language (for foreigners)")
    elif (message.text == "1c_csB_Wed"):
        bot.send_message(message.chat.id, text="1 course CS-B Wednesday \n 09.00 - 09.40: Elective English B 203 \n 09.50 - 10.30:Elective English B 203 \n 10.40 - 11.20: Introduction to Eng.&Cs B 205 \n 11.30 - 12.10: Introduction to Eng.&Cs B 205 \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: [Elective] Data Science B 202 \n 14.50 - 15.30: [Elective] Engineering Computer Graphics Lab 4 & B 211/ Physics B 200 \n 15.40 - 16.20: [Elective] Engineering Computer Graphics Lab 4 & B 211/ Physics B 200 \n 16.30 - 17.10: Russian Language Practic course B 109 \n 17.20 - 18.00: Russian Language Practic course B 109")
    elif (message.text == "1c_csB_Thu"):
        bot.send_message(message.chat.id, text="1 course CS-B Thursday \n 09.00 - 09.40: Calculus B 204 \n 09.50 - 10.30: Calculus B 204 \n 10.40 - 11.20: Introduction to Eng.&Cs Big Lab \n 11.30 - 12.10: Introduction to Eng.&Cs Big Lab \n 12.20 - 13.00: Introduction to Eng.&Cs Big Lab \n 13.00 - 14.00: 🍛Lunch \n 14.00 - 14.40: Algebra and Geometry B 201 \n 14.50 - 15.30: Algebra and Geometry B 201 \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break Time \n 17.20 - 18.00: [Break Time ")
    elif (message.text == "1c_csB_Fri"):
        bot.send_message(message.chat.id, text="1 course CS-B Friday \n 09.00 - 09.40: Elective English B 201 \n 09.50 - 10.30: Elective English B 201 \n 10.40 - 11.20: Elective French B 205\n 11.30 - 12.10: Elective French B 205 \n 12.20 - 13.00: Break time \n 13.00 - 14.00: 🥦Lunch \n 14.00 - 14.40: Programming Languages Big Lab & B208 \n 14.50 - 15.30: Programming Languages Big Lab & B208 \n 15.40 - 16.20: Programming Languages Big Lab & B 208 \n 16.30 - 17.10: Physical training special group \n 17.20 - 18.00: Physical training special group")

        # 2 course CS
    elif (message.text == "2 course CS"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("2c_csA")
        btn2 = types.KeyboardButton("2c_csB")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "2c_csA"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("2c_csA_Mon")
        btn2 = types.KeyboardButton("2c_csA_Tue")
        btn3 = types.KeyboardButton("2c_csA_Wed")
        btn4 = types.KeyboardButton("2c_csA_Thu")
        btn5 = types.KeyboardButton("2c_csA_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "2c_csB"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("2c_csB_Mon")
        btn2 = types.KeyboardButton("2c_csB_Tue")
        btn3 = types.KeyboardButton("2c_csB_Wed")
        btn4 = types.KeyboardButton("2c_csB_Thu")
        btn5 = types.KeyboardButton("2c_csB_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
        # A
    elif (message.text == "2c_csB_Mon"):
        bot.send_message(message.chat.id, text="2 course CS-B Monday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Object Oriented Programming Big Lab \n 10.40 - 11.20: Object Oriented Programming Big Lab \n 11.30 - 12.10: Object Oriented Programming Big Lab \n 12.20 - 13.00: Object Oriented Programming Big Lab \n 13.00 - 14.00: 🥑Lunch \n 14.00 - 14.40: Web Technologies B 211 \n 14.50 - 15.30: Web Technologies  B 211 \n 15.40 - 16.20: Web Technologies  B 211 \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif (message.text == "2c_csB_Tue"):
        bot.send_message(message.chat.id, text="2 course CS-B Tuesday \n 09.00 - 09.40: Electrotechnics & Electronics Lab4- B211 \n 09.50 - 10.30: Electrotechnics & Electronics Lab4- B211 \n 10.40 - 11.20:  Electrotechnics & Electronics Lab4- B211 \n 11.30 - 12.10: Kyrgyz Languages B204/B103/C408/B101 \n 12.20 - 13.00: Kyrgyz Languages B204/B103/C408/B101 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Discrete Mathematics B 204 \n 14.50 - 15.30: Discrete Mathematics B 204 \n 15.40 - 16.20: Kyrgyz language (for foreigners) C 403 \n 16.30 - 17.10: Kyrgyz language (for foreigners) C 403 \n 17.20 - 18.00: Break time ")
    elif (message.text == "2c_csB_Wed"):
        bot.send_message(message.chat.id, text="2 course CS-B Wednesday \n 09.00 - 09.40: Turkish Languages B 101 \n 09.50 - 10.30: Turkish Languages B 101 \n 10.40 - 11.20: Break Time \n 11.30 - 12.10: Physical Training \n 12.20 - 13.00: Physical Training \n 13.00 - 14.00: 🍇Lunch \n 14.00 - 14.40: Kyrgyz language (for foreigners) C 403 \n 14.50 - 15.30: Kyrgyz Languages C 403 \n 15.40 - 16.20: Break time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time  ")
    elif (message.text == "2c_csB_Thu"):
        bot.send_message(message.chat.id, text="2 course CS-B Thursday \n 09.00 - 09.40: Discrete Mathematics B 202 \n 09.50 - 10.30: Discrete Mathematics B 202 \n 10.40 - 11.20: Break Time \n 11.30 - 12.10: Kyrgyz Language C403/B103/B104 \n 12.20 - 13.00: Kyrgyz Language C403/B103/B104 \n 13.00 - 14.00: 🥐Lunch \n 14.00 - 14.40: Electrotechnics & Electronics B 205 \n 14.50 - 15.30: Electrotechnics & Electronics B 205 \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time  \n 17.20 - 18.00: Break time ")
    elif (message.text == "2c_csB_Fri"):
        bot.send_message(message.chat.id, text="2 course CS-B Friday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Database Systems Big Lab \n 11.30 - 12.10: Database Systems Big Lab \n 12.20 - 13.00: Database Systems Big Lab \n 13.00 - 14.00: 🫓Lunch \n 14.00 - 14.40: Web Technologies B 205 \n 14.50 - 15.30: Web Technologies B 205 \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time B 203 \n 17.20 - 18.00: Break time")
        # B
    elif (message.text == "2c_csA_Mon"):
        bot.send_message(message.chat.id, text="2 course CS-A Monday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Break Time \n 11.30 - 12.10: Discrete Mathematics B 201 \ n 12.20 - 13.00: Discrete Mathematics B 201 \n 13.00 - 14.00: 🍓 Lunch \n 14.00 - 14.40: Object Oriented Programming Big Lab \n 14.50 - 15.30: Object Oriented Programming Big Lab \n 15.40 - 16.20: Object Oriented Programming Big Lab \n 16.30 - 17.10: Object Oriented Programming Big Lab \n 17.20 - 18.00: Break time")
    elif (message.text == "2c_csA_Tue"):
        bot.send_message(message.chat.id, text="2 course CS-A Tuesday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20:  Break Time \n 11.30 - 12.10: Kyrgyz language B204/B103/B408 \n 12.20 - 13.00: Kyrgyz language B204/B103/B408  \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Physical Training \n 14.50 - 15.30: Physical Training \n 15.40 - 16.20: Kyrgyz language (for foreigners) C 403 \n 16.30 - 17.10: Kyrgyz language (for foreigners) C 403 \n 17.20 - 18.00: Break Time")
    elif (message.text == "2c_csA_Wed"):
        bot.send_message(message.chat.id, text="2 course CS-A Wednesday \n 09.00 - 09.40: Turkish languages B 101 \n 09.50 - 10.30:Turkish languages B 101 \n 10.40 - 11.20: Electrotechnics & Electronics Lab 3/ B 210 \n 11.30 - 12.10: Electrotechnics & Electronics Lab 3/ B 210 \n 12.20 - 13.00: Electrotechnics & Electronics Lab 3/ B 210 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Kyrgyz Languages (for foreigners) C 403 \n 14.50 - 15.30: Kyrgyz Languages (for foreigners) C 403 \n 15.40 - 16.20:Break Time \n 16.30 - 17.10: Break Time \n 17.20 - 18.00: Break Time")
    elif (message.text == "2c_csA_Thu"):
        bot.send_message(message.chat.id, text="2 course CS-A Thursday \n 09.00 - 09.40: Web Technologies Lab 4 \n 09.50 - 10.30: Web Technologies Lab 4 \n 10.40 - 11.20: Web Technologies Lab 4 \n 11.30 - 12.10: Kyrgyz Languages c403/B103/B104 \n 12.20 - 13.00: Kyrgyz Languages c403/B103/B104 \n 13.00 - 14.00: 🍛Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break Time \n 17.20 - 18.00: Break Time ")
    elif (message.text == "2c_csA_Fri"):
        bot.send_message(message.chat.id, text="2 course CS-A Friday \n 09.00 - 09.40: Discrete Mathematics B 202 \n 09.50 - 10.30: Discrete Mathematics B 202 \n 10.40 - 11.20: Database Systems Big Lab \n 11.30 - 12.10: Database Systems Big Lab \n 12.20 - 13.00: Database Systems Big Lab \n 13.00 - 14.00: 🥦Lunch \n 14.00 - 14.40: Web Technologies B 205 \n 14.50 - 15.30: Web Technologies B 205 \n 15.40 - 16.20: Electrotechnics & Electronics B 205 \n 16.30 - 17.10: Electrotechnics & Electronics B 205 \n 17.20 - 18.00: Physical training special group")


        # 3 course

    elif(message.text == "3 course CS"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("3c_csA")
        btn2 = types.KeyboardButton("3c_csB")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "3c_csA"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("3c_csA_Mon")
        btn2 = types.KeyboardButton("3c_csA_Tue")
        btn3 = types.KeyboardButton("3c_csA_Wed")
        btn4 = types.KeyboardButton("3c_csA_Thu")
        btn5 = types.KeyboardButton("3c_csA_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
    elif (message.text == "3c_csB"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("3c_csB_Mon")
        btn2 = types.KeyboardButton("3c_csB_Tue")
        btn3 = types.KeyboardButton("3c_csB_Wed")
        btn4 = types.KeyboardButton("3c_csB_Thu")
        btn5 = types.KeyboardButton("3c_csB_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)

    elif (message.text == "3c_csA_Mon"):
        bot.send_message(message.chat.id, text="3 course CS-A Monday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Software Engineering Lab4/ B211 \n 11.30 - 12.10: Software Engineering Lab4/ B211\n 12.20 - 13.00: Software Engineering Lab4/ B211 \n 13.00 - 14.00: 🥑Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time ")
    elif (message.text == "3c_csA_Tue"):
        bot.send_message(message.chat.id, text="3 course CS-A Tuesday \n 09.00 - 09.40: Probability and Statistics B 211 \n 09.50 - 10.30: Probability and Statistics B 211 \n 10.40 - 11.20:  Mobile App Development Big Lab \n 11.30 - 12.10: Mobile App Development Big Lab \n 12.20 - 13.00: Mobile App Development Big Lab \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: BreakTime \n 17.20 - 18.00: Break time ")
    elif (message.text == "3c_csA_Wed"):
        bot.send_message(message.chat.id, text="3 course CS-A Wednesday \n 09.00 - 09.40: Comp.Networks & Telecommunication Big Lab \n 09.50 - 10.30: Comp.Networks & Telecommunication Big Lab \n 10.40 - 11.20: Comp.Networks & Telecommunication Big Lab \n 11.30 - 12.10: Mobile App Development Big Lab 12.20 - 13.00: Mobile App Development Big Lab \n 13.00 - 14.00: 🍇Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time ")
    elif (message.text == "3c_csA_Thu"):
        bot.send_message(message.chat.id, text="3 course CS-A Thursday \n 09.00 - 09.40: Probability and Statistics B 205 \n 09.50 - 10.30: Probability and Statistics B 205 \n 10.40 - 11.20: Design & Analysis of Algorithms B 203 \n 11.30 - 12.10: Design & Analysis of Algorithms B 203 \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🥐Lunch \n 14.00 - 14.40: Comp.Networks & Telecommunication Lab3/B210 \n 14.50 - 15.30: Comp.Networks & Telecommunication Lab3/B210 \n 15.40 - 16.20: Comp.Networks & Telecommunication Lab3/B210 \n 16.30 - 17.10: Comp.Networks & Telecommunication Lab3/B210 \n 17.20 - 18.00: Break time  ")
    elif (message.text == "3c_csA_Fri"):
        bot.send_message(message.chat.id, text="3 course CS-A Friday \n 09.00 - 09.40: Design & Analysis of Algorithms Lab3/B210 \n 09.50 - 10.30: Design & Analysis of Algorithms Lab3/B210 \n 10.40 - 11.20: Introduction to Enterpreunership B 201 \n 11.30 - 12.10: Introduction to Enterpreunership B 201 \n 12.20 - 13.00: Introduction to Enterpreunership B 201 \n 13.00 - 14.00: 🫓Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time B 203 \n 17.20 - 18.00: Break time")

    elif (message.text == "3c_csB_Mon"):
        bot.send_message(message.chat.id, text="3 course CS-B Monday \n 09.00 - 09.40: Design & Analysis of Algorithms B 204 \n 09.50 - 10.30: Design Analysis of Algorithms B 204 \n 10.40 - 11.20: Software Engineering Lab4/ B211 \n 11.30 - 12.10: Software Engineering Lab4/ B211\n 12.20 - 13.00: Software Engineering Lab4/ B211 \n 13.00 - 14.00: 🥑Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time ")
    elif (message.text == "3c_csB_Tue"):
        bot.send_message(message.chat.id, text="3 course CS-B Tuesday \n 09.00 - 09.40: Probability and Statistics B 211 \n 09.50 - 10.30: Probability and Statistics B 211 \n 10.40 - 11.20:  Mobile App Development Big Lab \n 11.30 - 12.10: Mobile App Development Big Lab \n 12.20 - 13.00: Mobile App Development Big Lab \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: BreakTime \n 17.20 - 18.00: Break time ")
    elif (message.text == "3c_csB_Wed"):
        bot.send_message(message.chat.id, text="3 course CS-B Wednesday \n 09.00 - 09.40: Comp.Networks & Telecommunication Big Lab \n 09.50 - 10.30: Comp.Networks & Telecommunication Big Lab \n 10.40 - 11.20: Comp.Networks & Telecommunication Big Lab \n 11.30 - 12.10: Mobile App Development Big Lab 12.20 - 13.00: Mobile App Development Big Lab \n 13.00 - 14.00: 🍇Lunch \n 14.00 - 14.40: Design & Analysis of Algorithms \n 14.50 - 15.30: Design & Analysis of Algorithms Big Lab \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time \n 17.20 - 18.00: Break time")
    elif (message.text == "3c_csB_Thu"):
        bot.send_message(message.chat.id, text="3 course CS-B Thursday \n 09.00 - 09.40: Probability and Statistics B 205 \n 09.50 - 10.30: Probability and Statistics B 205 \n 10.40 - 11.20: Introduction to Enterpreunership B 205 \n 11.30 - 12.10: Introduction to Enterpreunership B 205 \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🥐Lunch \n 14.00 - 14.40: Comp.Networks & Telecommunication Lab3/B210 \n 14.50 - 15.30: Comp.Networks & Telecommunication Lab3/B210 \n 15.40 - 16.20: Comp.Networks & Telecommunication Lab3/B210 \n 16.30 - 17.10: Comp.Networks & Telecommunication Lab3/B210 \n 17.20 - 18.00: Break time   ")
    elif (message.text == "3c_csB_Fri"):
        bot.send_message(message.chat.id, text="3 course CS-B Friday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Break Time \n 11.30 - 12.10: Break Time \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🫓Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break time B 203 \n 17.20 - 18.00: Break time")

        # 4 course
    elif (message.text == "4 course CS"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("4c_cs_Mon")
        btn2 = types.KeyboardButton("4c_cs_Tue")
        btn3 = types.KeyboardButton("4c_cs_Wed")
        btn4 = types.KeyboardButton("4c_cs_Thu")
        btn5 = types.KeyboardButton("4c_cs_Fri")
        back = types.KeyboardButton("Back")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="->", reply_markup=markup)
        # A
    elif (message.text == "4c_cs_Mon"):
        bot.send_message(message.chat.id, text="4 course CS-A Monday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Designing in C# B210/B200 \n 11.30 - 12.10: Designing in C# B210-B200 \n 12.20 - 13.00: Information Security Lab3/B210 \n 13.00 - 14.00: Information Security Lab3/B210 \n 14.00 - 14.40: Enterprise Resource Planning A202 \n 14.50 - 15.30: Enterprise Resource Planning A202 \n 15.40 - 16.20: Enterprise Resource Planning A202 \n 16.30 - 17.10: Enterprise Resource Planning A202")
    elif (message.text == "4c_cs_Tue"):
        bot.send_message(message.chat.id, text="4 course CS-A Tuesday \n 09.00 - 09.40: Introduction to Data Mining B204/ Software Architecture & Design patterns B200 \n 09.50 - 10.30: Introduction to Data Mining B204/ Software Architecture & Design patterns B200 \n 10.40 - 11.20:  Introduction to Data Mining B204/ Software Architecture & Design patterns B200 \n 11.30 - 12.10: Information Security Lab4-B211 \n 12.20 - 13.00: Information Security Lab4-B211 \n 13.00 - 14.00: 🥙Lunch \n 14.00 - 14.40: Break Time \n 14.50 - 15.30: Break Time \n 15.40 - 16.20: Machine Learning B202/ Introduction to Data Science B202 \n 16.30 - 17.10: Machine Learning B202/ Introduction to Data Science B202")
    elif (message.text == "4c_cs_Wed"):
        bot.send_message(message.chat.id, text="4 course CS-A Wednesday \n 09.00 - 09.40:Introduction to Data Mining Lab4- B211/ Software Architecture & Design patterns B200 \n 09.50 - 10.30: Introduction to Data Mining Lab4- B211/ Software Architecture & Design patterns B200 \n 10.40 - 11.20: Introduction to Data Mining Lab4- B211/ Software Architecture & Design patterns B200 \n 11.30 - 12.10: Break Time \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🍇Lunch \n 14.00 - 14.40: HCI B 204 \n 14.50 - 15.30: HCI B 204 \n 15.40 - 16.20: Designing in C# Lab3-B 210 / Robotics B 200 \n 16.30 - 17.10: Designing in C# Lab3-B 210 / Robotics B 200 \n 17.20 - 18.00: Break time  ")
    elif (message.text == "4c_cs_Thu"):
        bot.send_message(message.chat.id, text="4 course CS-A Thursday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Designing in C# Lab3-B 210 / Robotics B 200 \n 11.30 - 12.10: Introduction to Enterpreunership B 205 \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🥐Lunch \n 14.00 - 14.40: HCI B 204 \n 14.50 - 15.30: HCI B 204 \n 15.40 - 16.20: Break Time \n 16.30 - 17.10: Break Time  \n 17.20 - 18.00: Break time")
    elif (message.text == "4c_cs_Fri"):
        bot.send_message(message.chat.id, text="4 course CS-A Friday \n 09.00 - 09.40: Break Time \n 09.50 - 10.30: Break Time \n 10.40 - 11.20: Image Processing B211/ Lab4 \n 11.30 - 12.10: Image Processing B211/ Lab4 \n 12.20 - 13.00: Break Time \n 13.00 - 14.00: 🫓Lunch \n 14.00 - 14.40: Machine Learning Lab4 \n 14.50 - 15.30: Machine Learning Lab4 \n 15.40 - 16.20: Machine Learning lab4 \n 16.30 - 17.10: Machine Learning 4 \n 17.20 - 18.00: Break time")
     #Sport mugs

    elif (message.text == "🤾Sports mugs"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        f = types.KeyboardButton("⚽football")
        v = types.KeyboardButton("🏐volleyball")
        b = types.KeyboardButton("🏀basketball")
        k = types.KeyboardButton("🎱9-korgool")
        t = types.KeyboardButton("🏓tennis")
        c = types.KeyboardButton("♟chess")
        back = types.KeyboardButton("Back")
        markup.add(b, k, t, v, c, f, back)
        bot.send_message(message.chat.id, text="Choose -->", reply_markup=markup)
    elif(message.text == "⚽football"):
        bot.send_message(message.chat.id, text="⚽Футбол \n Чыныбеков Замирбек Бактыбекович \n 17:00-19:30 (Среда, Пятница) \n Футбольное поле")
    elif (message.text == "🏐volleyball"):
        bot.send_message(message.chat.id, text="🏐Волейбол(муж) \n Азат.у.Шайымбек \n 16:30-18:00 Среда спортзал \n 18:30-19:00 Пятница спортзал \n \n 🏐Волейбол(жен) \n Азат.у.Шайымбек \n 16:30-18:00 (Понедельник, Пятница) спортзал")
    elif (message.text == "🏀basketball"):
        bot.send_message(message.chat.id, text="🏀Баскетбол(муж) \n Ирина Чалова Викторовна \n 16:30-18:00 (Вторник, Четверг) \n спортзал \n \n 🏀Баскетбол(жен) \n Ирина Чалова Викторовна \n 18:00-19:30 (Вторник, Четверг) спортзал")
    elif (message.text == "🎱9-korgool"):
        bot.send_message(message.chat.id, text="🎱Тогуз кооргол \n Камчибекова Замира Каликеевна \n 14:00-16:00 Понедельник \n 16:00-18:00 Вторник \n 16:30-18:00 Четверг \n С блок подвал 006")
    elif (message.text == "🏓tennis"):
        bot.send_message(message.chat.id, text="🏓Теннис \n Чыныбеков Замирбек Бактыбекович \n 17:00-18:30 (Вторник, Четверг) \n Теннисный зал")
    elif (message.text == "♟chess"):
        bot.send_message(message.chat.id, text="♟Шахматы \n Исакжанов Кельсинбек Бекбаевич \n 16:40-18:00 (Вторник, Четверг) \n ")

        #Back
    elif(message.text == "Back"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button6 = types.KeyboardButton("Namaz time")
        button1 = types.KeyboardButton("☰Schedule")
        button3 = types.KeyboardButton("❆Weather")
        button4 = types.KeyboardButton("💻Final exams")
        button5 = types.KeyboardButton("🍴Dining prices")
        button2 = types.KeyboardButton("🤾Sports mugs")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, text="You are on the main menu 🥰", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="I did not program for such a command ☹️")

bot.polling(none_stop=True)
