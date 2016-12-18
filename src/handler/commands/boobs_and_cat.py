from .base import Base
import json
from src.utils import random_element
from urllib.request import urlopen


class BoobsAndCat(Base):
    name = 'bc'
    images = None

    @staticmethod
    def execute(bot, command):
        if BoobsAndCat.images is None:
            BoobsAndCat.images = BoobsAndCat.__preload()

        bot.send_photo(chat_id=command.chat_id, photo=random_element(BoobsAndCat.images))

    @staticmethod
    def __preload():
        response = urlopen('https://api.cognitive.microsoft.com/bing/v5.0/images/search?q=boobs%20and%20cat&mkt=en-us&safe-search=strict&image-type=photo&subscription-key=dd95294bc02748a1ab5152d36fdbbdac')
        data = json.loads(response.read().decode('utf-8'))

        return list(map(lambda e: e['contentUrl'], data['value']))