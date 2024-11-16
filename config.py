# код для загрузки токена из .env
from dotenv import load_dotenv
import os

# загружаем переменное окружение
load_dotenv()

# получаем токен бота
API_TOKEN = os.getenv('API_TOKEN')

# проверяем наличие токена
if not API_TOKEN:
    raise ValueError('Токе не найден. Проверьте файл .env')