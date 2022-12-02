import logging
import json
from datetime import date, datetime
from pprint import pprint
from telethon import connection
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from app.config_parser import load_config

logging.basicConfig(level=logging.INFO)

config = load_config('config/bot.ini')
api_id = config.tg_bot.api_id
api_hash = config.tg_bot.api_hash
username = config.tg_bot.username

client = TelegramClient(username, api_id, api_hash)
client.start()


async def get_all_participants(group):
    offset_user = 0
    limit_user = 100
    all_participants = []

    participants = await client.get_participants(group)

    for participant in participants:
        print(participant.first_name, participant.id)


async def get_all_messages(group):
    offset_msg = 0
    limit_msg = 10
    all_messages = []
    total_messages = 0
    total_count_limit = 100  # лимит по сообщениям

    class DateTimeEncoder(json.JSONEncoder):
        """ Класс для сериализации записи дат в JSON """

        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)

    while True:
        history = await client(GetHistoryRequest(
            peer=group,
            offset_id=offset_msg,
            offset_date=None,
            add_offset=0,
            limit=limit_msg,
            max_id=0,
            min_id=0,
            hash=0
        )
        )
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
            # all_messages.append(
            #     {
            #         'id': message.id,
            #         'group_id': message.peer_id.channel_id,
            #         'user_id': message.from_id
            #     }
            # )
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    print(total_messages)
    with open('messages.json', 'w', encoding='utf-8') as file:
        json.dump(all_messages, file, ensure_ascii=False, indent=2, cls=DateTimeEncoder)

    # return all_messages


async def main():
    url = 'https://t.me/+o8ZMXyl1jrljMzMy'
    await get_all_messages(url)
    # await get_all_participants(url)


if __name__ == '__main__':
    client.loop.run_until_complete(main())
    # client.send_message('purple_indifferent_bot', 'hi')
    # print(client.get_me().stringify())
    # for dialog in client.iter_dialogs():
    #     print(dialog.name, dialog.id)
