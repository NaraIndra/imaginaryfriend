from .base import Base
import json
from src.utils import random_element
from urllib.request import urlopen


class Borscht(Base):
    name = 'borscht'
    images = None

    @staticmethod
    def execute(bot, command):
        if Borscht.images is None:
            Borscht.images = Borscht.__preload()

        bot.send_photo(chat_id=command.chat_id, photo=random_element(Borscht.images))

    @staticmethod
    def __preload():
        response = urlopen('https://api.cognitive.microsoft.com/bing/v5.0/images/search?q=%D0%B1%D0%BE%D1%80%D1%89&mkt=en-us&safe-search=strict&image-type=photo&subscription-key=dd95294bc02748a1ab5152d36fdbbdac')
        data = json.loads(response.read().decode('utf-8'))

        return list(map(lambda e: e['contentUrl'], data['value']))