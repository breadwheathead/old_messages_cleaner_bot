from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from app.config_parser import load_config

config = load_config('config/bot.ini')
bot = Bot(config.tg_bot.bot_token)
dp = Dispatcher(bot)
