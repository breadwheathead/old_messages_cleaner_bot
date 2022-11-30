import logging
from aiogram.utils import executor
from bot_init import dp
from app.handlers import register_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    register_handlers(dp)

    logger.info('Бот запущен')
    executor.start_polling(dp, skip_updates=True)
