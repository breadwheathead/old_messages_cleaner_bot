from aiogram import types
from aiogram.dispatcher import Dispatcher


async def start(message: types.Message):
    await message.answer('Вас приветствует Бот для удаления сообщений пользователей, покинувших этот чат')


async def echo(message: types.Message):
    await message.reply(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(echo, content_types=['text'])
