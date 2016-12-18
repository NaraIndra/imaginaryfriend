from .base import Base
import json
from src.utils import random_element
from urllib.request import urlopen


class Pizza(Base):
    name = 'pizza'
    images = None

    @staticmethod
    def execute(bot, command):
        if Pizza.images is None:
            Pizza.images = Pizza.__preload()

        bot.send_photo(chat_id=command.chat_id, photo=random_element(Pizza.images))

    @staticmethod
    def __preload():
        response = urlopen('https://api.cognitive.microsoft.com/bing/v5.0/images/search?q=pizza&mkt=en-us&safe-search=strict&image-type=photo&subscription-key=dd95294bc02748a1ab5152d36fdbbdac')
        data = json.loads(response.read().decode('utf-8'))

        return list(map(lambda e: e['contentUrl'], data['value']))