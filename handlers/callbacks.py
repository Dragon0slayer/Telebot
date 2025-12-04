from telebot.types import CallbackQuery

from bot import bot
from keyboards.inline import get_game_keyboard, get_play_again_keyboard
from states.user_states import state_manager, game_logic


@bot.callback_query_handler(func=lambda call: call.data in ['rock', 'scissors', 'paper'])
def handle_game_choice(call: CallbackQuery):
    """Обробка вибору гравця"""
    user_id = call.from_user.id

    user_choice = game_logic.map_callback_to_choice(call.data)
    bot_choice = game_logic.get_bot_choice()

    result = game_logic.determine_winner(user_choice, bot_choice)

    if result == 'win':
        state_manager.increment_wins(user_id)
        result_emoji = '🎉'
        result_text = 'Ти переміг!'
    elif result == 'lose':
        state_manager.increment_losses(user_id)
        result_emoji = '😢'
        result_text = 'Ти програв!'
    else:
        state_manager.increment_draws(user_id)
        result_emoji = '🤝'
        result_text = 'Нічия!'

    message_text = f"""
{result_emoji} {result_text}

Твій вибір: {user_choice}
Вибір бота: {bot_choice}

Зіграємо ще раз?
"""

    bot.edit_message_text(
        message_text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=get_play_again_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'play_again')
def handle_play_again(call: CallbackQuery):
    bot.edit_message_text(
        "🎮 Оберіть свій варіант:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=get_game_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'view_stats')
def handle_view_stats(call: CallbackQuery):
    user_id = call.from_user.id
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
"""

    bot.answer_callback_query(call.id, "Статистика оновлена!")
    bot.edit_message_text(
        stats_text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=get_play_again_keyboard()
    )