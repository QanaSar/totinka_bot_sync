# основной файл, который запускает бота и регистрирует обработчики
from telebot import TeleBot
from config import API_TOKEN
from handlers.commands import register_handlers as register_command_handlers
from handlers.moderation import register_handlers as register_moderation_handlers

# создаем обьект бота
bot = TeleBot(API_TOKEN, parse_mode='HTML')

# регистрируем обработчики
register_command_handlers(bot)
register_moderation_handlers(bot)

# Запуск бота
if __name__ == '__main__':
    print('Бот запущен....')
    bot.infinity_polling()