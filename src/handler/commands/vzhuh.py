from .base import Base
from PIL import Image, ImageFont, ImageDraw


class Vzhuh(Base):
    name = 'vzhuh'
    images = None

    @staticmethod
    def execute(bot, command):
        text = Vzhuh.format_text('вжух ' + ' '.join(command.args))
        Vzhuh.create_image(text)

        bot.send_photo(chat_id=command.chat_id, photo=open('sample-out.png', 'rb'))

    @staticmethod
    def format_text(text):
        result = []
        current_part = ''
        if len(text) > 8:
            parts = text.upper().split(' ')
            for part in parts:
                if len(current_part) + len(part) <= 10:
                    current_part += part + ' '
                else:
                    result.append(current_part)
                    result.append(part)
                    current_part = ''
            result.append(current_part)
        else:
            result.append(text)

        return '\r\n'.join(result)

    @staticmethod
    def create_image(text):
        img = Image.open("vzush_sample.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/Library/Fonts/Futura.ttc", 40, index=2)
        draw.text((222, 280), text, (0, 0, 0), font=font)
        img.save('sample-out.png')
