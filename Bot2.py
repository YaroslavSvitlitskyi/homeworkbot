import telebot
import config1

from telebot import types 

bot = telebot.TeleBot(config1.TOKEN)


@bot.message_handler(commands=["start"])

def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	thing3 = types.KeyboardButton("/write_absent_people")
	
	markup.add(thing3)

	bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nДля того щоб записати відсутніх\n натисніть кнопку\n/write_absent_people".format(message.from_user, bot.get_me()),	
		parse_mode="html", reply_markup=markup)
	bot.send_message(message.chat.id, "✅Правила синтаксису запису відсутніх:\n1️⃣Записувати треба тільки прізвища(з великої літери)\n2️⃣Записувати прізвища треба так:прізвище,прізвище,прізвище і т.д\nУдачного запису😊 ".format(message.from_user, bot.get_me()),parse_mode="html")



@bot.message_handler(commands=['write_absent_people'])
def mess(message):

		bot.send_message(message.chat.id, "{0.first_name},можеш писати".format(message.from_user, bot.get_me()),parse_mode = "html")


@bot.message_handler(content_types=['text'])
def mass(message):
	with open("Log.txt", "w") as file:
			file.write("\n" + message.text)
	with open("Log.txt", "r") as file:
			x = file.read()
	if message.text in x:
		bot.send_message(message.chat.id, "Дякую,прізвища записані")



bot.polling(none_stop = True)

