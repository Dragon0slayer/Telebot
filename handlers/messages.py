from telebot.types import Message

from bot import bot
from config import HELP_TEXT, RULES_TEXT
from keyboards.reply import get_main_menu_keyboard
from keyboards.inline import get_game_keyboard
from states.user_states import state_manager


@bot.message_handler(commands=['help'])
def handle_help(message: Message):
    bot.send_message(
        message.chat.id,
        HELP_TEXT,
        reply_markup=get_main_menu_keyboard()
    )


@bot.message_handler(commands=['rules'])
def handle_rules(message: Message):
    bot.send_message(
        message.chat.id,
        RULES_TEXT,
        reply_markup=get_main_menu_keyboard()
    )


@bot.message_handler(commands=['play'])
def handle_play(message: Message):
    """Початок нової гри"""
    user_id = message.from_user.id
    state_manager.set_state(user_id, 'playing')

    bot.send_message(
        message.chat.id,
        "🎮 Оберіть свій варіант:",
        reply_markup=get_game_keyboard()
    )


@bot.message_handler(commands=['stats'])
def handle_stats(message: Message):
    """Показати статистику користувача"""
    user_id = message.from_user.id
    stats = state_manager.get_stats(user_id)

    total = stats['wins'] + stats['losses'] + stats['draws']
    win_rate = (stats['wins'] / total * 100) if total > 0 else 0

    stats_text = f"""
📊 Твоя статистика:

🏆 Перемоги: {stats['wins']}
😢 Поразки: {stats['losses']}
🤝 Нічиї: {stats['draws']}
📈 Всього ігор: {total}
💯 Відсоток перемог: {win_rate:.1f}%

Продовжуй грати! /play
"""
    bot.send_message(message.chat.id, stats_text)


@bot.message_handler(commands=['reset'])
def handle_reset(message: Message):
    """Скинути статистику"""
    user_id = message.from_user.id
    state_manager.reset_stats(user_id)
    bot.send_message(
        message.chat.id,
        "🔄 Статистику скинуто! Почніть нову гру /play"
    )


# --------- Обробники текстових кнопок ---------


@bot.message_handler(func=lambda message: message.text == '🎮 Грати')
def handle_play_button(message: Message):
    handle_play(message)


@bot.message_handler(func=lambda message: message.text == '📊 Статистика')
def handle_stats_button(message: Message):
    handle_stats(message)


@bot.message_handler(func=lambda message: message.text == '📜 Правила')
def handle_rules_button(message: Message):
    handle_rules(message)


@bot.message_handler(func=lambda message: message.text == 'ℹ️ Допомога')
def handle_help_button(message: Message):
    handle_help(message)


@bot.message_handler(func=lambda message: True)
def handle_text(message: Message):
    """Обробка невідомих текстових повідомлень"""
    bot.send_message(
        message.chat.id,
        "❓ Не розумію цю команду. Використовуйте /help для допомоги"
    )