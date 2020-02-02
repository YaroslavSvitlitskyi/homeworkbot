import telebot
import config

from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])



def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	thing1 = types.KeyboardButton("/Авторизуватись")
	
	markup.add(thing1)

	bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nХочеш отримати Д/З за минулий день?\nТоді натисніть кнопку\n/Авторизуватись".format(message.from_user, bot.get_me()),	
		parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["Авторизуватись"])


	
def Bot(message):
	
	bot.send_message(message.chat.id, "{0.first_name}, Введи своє прізвище".format(message.from_user, bot.get_me()),parse_mode= "html")



@bot.message_handler(content_types=["text"])


def Bot1(message):			 	
	f = open("Log.txt", "r")
	l = f.read()			 	
	if message.text in l:
		bot.send_message(message.chat.id, "Вітаю ти можеш забрати свою домашку!".format(message.from_user,bot.get_me()),parse_mode= "html")
		with open("work.txt", 'r') as file:
			    w = file.read()
		bot.send_message(message.chat.id,w, parse_mode = "html")
	else:
		bot.send_message(message.chat.id,"Ти не був відсутній")



bot.polling(none_stop = True)