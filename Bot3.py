import telebot
import config2

from telebot import types 

bot = telebot.TeleBot(config2.TOKEN)

@bot.message_handler(commands=["start"])


def welcome(message):	
	bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nМожеш скидувати д/з".format(message.from_user, bot.get_me()),	
		parse_mode="html") 

@bot.message_handler(content_types=["text"])


def mess(message):
	with open("work.txt", "w") as file:
		 	file.write(message.text)
	with open("work.txt", "r") as file:
			l = file.read()
	if message.text in l:
		bot.send_message(message.chat.id, "Дякую,домашнє завдання записане")

bot.polling(none_stop = True)

