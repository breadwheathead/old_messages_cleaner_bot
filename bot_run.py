import logging
from aiogram.utils import executor
from bot_init import bot, dp
from app.handlers import register_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def on_startup(_):
    await bot.delete_my_commands()


if __name__ == '__main__':
    register_handlers(dp)

    logger.info('Бот запущен')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
