import logging
from telethon import connection
from telethon.sync import TelegramClient
from app.config_parser import load_config

logging.basicConfig(level=logging.INFO)

config = load_config('config/bot.ini')
api_id = config.tg_bot.api_id
api_hash = config.tg_bot.api_hash
username = config.tg_bot.username

url = 'https://t.me/+o8ZMXyl1jrljMzMy'

client = TelegramClient(username, api_id, api_hash)
client.start()


def save_users(group):
    participants = client.iter_participants(group)
    for participant in participants:
        print(participant.first_name, participant.id)


if __name__ == '__main__':
    save_users(url)
    # client.send_message('purple_indifferent_bot', 'hi')
    # print(client.get_me().stringify())
    # for dialog in client.iter_dialogs():
    #     print(dialog.name, dialog.id)
