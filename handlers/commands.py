from telebot.types import Message

# обработчки команды старт
def handle_start(bot, message:Message):
    user_first_name = message.from_user.first_name or 'Гость'
    bot.send_message(message.chat.id, f'Привет,{user_first_name}. Я на связи')

# регистрация обработчика
def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_handler(message: Message):
        handle_start(bot, message)