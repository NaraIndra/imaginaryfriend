from src.handler.commands.base import Base
from src.handler.commands.start import Start
from src.handler.commands.help import Help
from src.handler.commands.ping import Ping
from src.handler.commands.get_stats import GetStats
from src.handler.commands.moderate import Moderate
from src.handler.commands.chance import Chance

from src.handler.commands.butts import Butts
from src.handler.commands.boobs import Boobs
from src.handler.commands.boobs_and_cat import BoobsAndCat
from src.handler.commands.meow import Meow
from src.handler.commands.woof import Woof
from src.handler.commands.borscht import Borscht
from src.handler.commands.pizza import Pizza
from src.handler.commands.shaverma import Shaverma
from src.handler.commands.xkcd import XKCD
from src.handler.commands.vzhuh import Vzhuh
from src.handler.commands.animal_offense import AnimalOffense

commands = {}
for clazz in Base.__subclasses__():
    command_name = getattr(clazz, 'name')
    command_aliases = getattr(clazz, 'aliases')
    execute_method = getattr(clazz, 'execute')

    if command_name is not None:
        commands[command_name] = execute_method
    for command_alias in command_aliases:
        commands[command_alias] = execute_method
