import re
from telebot.types import Message

# Проверка и удаление ссылок
def handle_links(bot, message: Message):
    # Проверяем что сообщение из группы
    if message.chat.type in ['group', 'supergroup']:
        url_pattern = re.compile(r"https?://\S+|t\.me/\S+")
        # Если в сообщений найдена ссылка
        if url_pattern.search(message.text):
            bot.delete_message(message.chat.id, message.id)
            bot.send_message(message.chat.id, 'Ссылки запрещены')

# Регистрация обработчиков
def register_handlers(bot):
    @bot.message_handler(content_types=['text'])
    def moderation_handler(message: Message):
        handle_links(bot, message)