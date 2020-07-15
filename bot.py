import telebot;
import requests;
bot = telebot.TeleBot('token');

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, "Привет, я показываю текущую погоду в городе Ульяновске. Напиши мне: Погода")
def request_current_weather():
	appid = "8426bf0c72628b9b053f215cb6dd14c4"
	s_city = "Ulyanovsk,RU"
	res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	result=data['main']['temp']
	return result

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'погода':
		bot.send_message(message.from_user.id, "Сейчас")
		bot.send_message(message.from_user.id,request_current_weather())
		bot.send_message(message.from_user.id, "градусов по Цельсию")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Напиши: Погода")
	else:
		bot.send_message(message.from_user.id, "Такой команды нет")
bot.polling(none_stop=True, interval=0)
