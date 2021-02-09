from handlers import config
from interface import main_menu

configHandler = config.Config()
configHandler.load_config()

main_menu.activate_menu(config)
