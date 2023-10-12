from config import weatherBotTelegramToken , weatherApiToken
import telebot
from main import getWeather

# Создаем экземпляр бота
bot = telebot.TeleBot(weatherBotTelegramToken)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'привет! напиши свой город и я пришлю тебе погоду')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    city = message.text
    bot.send_message(message.chat.id, getWeather(city ,weatherApiToken ) )


# Запускаем бота
bot.polling(none_stop=True, interval=0)
