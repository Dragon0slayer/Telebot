from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_game_keyboard() -> InlineKeyboardMarkup:
    """
    Створює inline клавіатуру для вибору в грі
    """
    keyboard = InlineKeyboardMarkup(row_width=3)

    btn_rock = InlineKeyboardButton('🪨 Камінь', callback_data='rock')
    btn_scissors = InlineKeyboardButton('✂️ Ножиці', callback_data='scissors')
    btn_paper = InlineKeyboardButton('📄 Папір', callback_data='paper')

    keyboard.add(btn_rock, btn_scissors, btn_paper)
    return keyboard


def get_play_again_keyboard() -> InlineKeyboardMarkup:
    """
    Створює inline клавіатуру для повторної гри
    """
    keyboard = InlineKeyboardMarkup(row_width=2)

    btn_play = InlineKeyboardButton('🔄 Грати ще', callback_data='play_again')
    btn_stats = InlineKeyboardButton('📊 Статистика', callback_data='view_stats')

    keyboard.add(btn_play, btn_stats)
    return keyboard