from telebot import TeleBot

from config import TOKEN
from database.database import DataBase

bot = TeleBot(TOKEN, parse_mode='html')
db = DataBase()