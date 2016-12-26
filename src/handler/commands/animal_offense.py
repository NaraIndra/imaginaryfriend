from .base import Base
import vk
from src.config import redis


class AnimalOffense(Base):
    name = 'ao'
    domain = 'animal_offense'
    key = 'animal_offense:{}'
    quality_order = ['src_xxbig', 'src_xbig', 'src_big', 'src', 'src_small']
    session = vk.Session()
    api = vk.API(session)

    @staticmethod
    def execute(bot, command):
        read_count = AnimalOffense.get(command.chat_id)
        total_count = AnimalOffense.get_total() - 1
        post = AnimalOffense.api.wall.get(domain=AnimalOffense.domain, offset=total_count - read_count, count=1)

        try:
            data = post[1]
            photo = list(filter(lambda a: a['type'] == 'photo', data['attachments']))[0]['photo']
            photo_link = [photo[q] for q in AnimalOffense.quality_order if q in photo][0]
            text = data['text']

            AnimalOffense.increment(command.chat_id)

            bot.send_photo(chat_id=command.chat_id, caption=text, photo=photo_link)
        except IndexError:
            bot.send_message(chat_id=command.chat_id, text='No new photos')

    @staticmethod
    def get_total():
        return int(AnimalOffense.api.wall.get(domain=AnimalOffense.domain, offset=0, count=1)[0])

    @staticmethod
    def get(chat_id):
        result = redis.instance().get(AnimalOffense.key.format(chat_id))

        return int(result.decode("utf-8")) if result is not None else 0

    @staticmethod
    def increment(chat_id):
        redis.instance().incr(AnimalOffense.key.format(chat_id))
