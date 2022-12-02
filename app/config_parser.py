import configparser
from dataclasses import dataclass


@dataclass
class TgBot:
    api_id: int
    api_hash: str
    username: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str) -> Config:
    config = configparser.ConfigParser()
    config.read(path)
    tg_bot = config['tg_bot']
    return Config(
        tg_bot=TgBot(
            api_id=int(tg_bot['api_id']),
            api_hash=tg_bot['api_hash'],
            username=tg_bot['username']
        )
    )
