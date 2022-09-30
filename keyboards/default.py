from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def confirmation():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    confirm = KeyboardButton("Xa")
    no_confirm = KeyboardButton("Yo'q")
    markup.add(confirm, no_confirm)
    return markup