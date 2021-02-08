from handlers import menu
from interface import instructions
from interface import config
from handlers import config as configHandler
from interface import viewScores
from interface.game import game

MENU_OPTIONS = ["Play the game", "Read instructions", "View all scores", "Edit Configuration", "View Configuration"]


# Sends the default menu
def activate_menu(config_obj: configHandler):
    menu_choice = menu.create_menu("MAIN MENU", "Chose an option below.", MENU_OPTIONS, False)

    if menu_choice == 1:
        game.play(config_obj)
    elif menu_choice == 2:
        instructions.send()
    elif menu_choice == 3:
        viewScores.send()
    elif menu_choice == 4:
        config.send_menu(config_obj)
    elif menu_choice == 5:
        config.show_current(config_obj)

    activate_menu(config_obj)
