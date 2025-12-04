from bot.types import messages

import bot
from config import WELCOME_TEXT
from keyboards.reply import get_main_menu_keyboard


@bot.message_handler(commands=['start'])
def handle_start(message: messages):
    """Обробка команди /start"""
    user_name = message.from_user.first_name

    bot.send_message(
        message.chat.id,
        f"👋 Привіт, {user_name}!\n\n{WELCOME_TEXT}",
        reply_markup=get_main_menu_keyboard()
    )