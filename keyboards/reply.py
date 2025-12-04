from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Створює головне меню з Reply клавіатурою
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_play = KeyboardButton('🎮 Грати')
    btn_stats = KeyboardButton('📊 Статистика')
    btn_rules = KeyboardButton('📜 Правила')
    btn_help = KeyboardButton('ℹ️ Допомога')

    keyboard.add(btn_play, btn_stats)
    keyboard.add(btn_rules, btn_help)

    return keyboard