import logging
import os
import pyrogram
from pyrogram import Client, filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


if os.path.exists('me.session'):
    bot = Client('me')
    print('есть')
else:
    from app.config_parser import load_config
    config = load_config('config/bot.ini')
    api_id = config.tg_bot.api_id
    api_hash = config.tg_bot.api_hash
    bot = Client('me', api_id, api_hash)


async def get_members(group_id) -> set:
    members = set()
    async for member in bot.get_chat_members(group_id):
        members.add(member.user.id)
    return members


async def get_messages(group_id) -> list:
    messages = []
    async for message in bot.get_chat_history(group_id):
        if message.from_user:
            messages.append({
                'id': message.id,
                'user_id': message.from_user.id
            })
    return messages


@bot.on_message(filters.command('clean'))
async def delete_message(client, message):
    members = await get_members(message.chat.id)
    messages = await get_messages(message.chat.id)
    for mess in messages:
        if mess['user_id'] not in members:
            await client.delete_messages(message.chat.id, mess['id'])
            logger.warning(f'Сообщение № {mess["id"]} удалено')


if __name__ == '__main__':
    bot.run()
