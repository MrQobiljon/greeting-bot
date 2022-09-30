from telebot.types import Message

from data.loader import bot, db
import admins

db.create_group_table()

@bot.message_handler(commands=['start'], func=lambda message: message.chat.type in ['private'])
def start(message: Message):
    bot.send_message(message.chat.id, f"Assalomu alaykum hurlamtli {message.from_user.first_name}!\n"
                                      f"Bu <b>Salom beruvchi</b> bot.\n"
                                      f"Bot guruhga tashrif buyurgan foydalanuvchilar bilan salomlashadi.\n"
                                      f"Botdan foydlanish uchun botni guruhga qo'shing.")


@bot.message_handler(content_types=['new_chat_members'])
def new_member(message: Message):
    chat_id = message.chat.id
    if message.json['new_chat_members'][0]['is_bot']:
        db.insert_group_id(chat_id)
    bot.send_message(chat_id, f"{message.chat.title} guruhiga xush kelibsiz @{message.json['new_chat_members'][0]['username']}")


bot.polling(none_stop=True)