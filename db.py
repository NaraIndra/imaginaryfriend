import configparser


config = configparser.ConfigParser()
config.read('./main.cfg', encoding='utf-8')

DATABASES = {'db': config['db']}
