from interface import menu
from handlers import config

configHandler = config.Config()
configHandler.load_config()

menu.send_menu(configHandler)
