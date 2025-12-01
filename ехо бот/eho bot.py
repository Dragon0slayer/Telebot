import telebot
import os
from dotenv import load_dotenv


load_dotenv()
Token = os.getenv("Token")


bot = telebot.TeleBot(Token)


@bot.message_handler(func=lambda msg: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

print("Бот запущений…")
bot.infinity_polling()