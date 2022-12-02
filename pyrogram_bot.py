import asyncio
import logging
from pyrogram import Client
from app.config_parser import load_config

logging.basicConfig(level=logging.INFO)

config = load_config('config/bot.ini')
api_id = config.tg_bot.api_id
api_hash = config.tg_bot.api_hash
bot_token = config.tg_bot.bot_token

receiver_id = '1533275740'  # it's me


async def main():
    async with Client(bot_token, api_id, api_hash) as app:
        await app.send_message(receiver_id, 'Hiiiii')


if __name__ == '__main__':
    asyncio.run(main())
