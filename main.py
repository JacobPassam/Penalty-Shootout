from handlers import config
from interface import main_menu

configHandler = config.Config()
configHandler.startup()

main_menu.activate_menu(configHandler)
