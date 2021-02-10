from handlers.config import Config as configHandler
from interface.game import game
from interface import instructions
from interface import config as config_menu
from interface import scores
from handlers import menu

OPTIONS = ["Play the game", "Read instructions", "View all scores", "Edit Configuration", "View Configuration"]


def activate_menu(config: configHandler):
    response = menu.create_int_menu("MAIN MENU", OPTIONS, False)

    # Detects response and activates functions dependant on the outcome.
    if response == 1:
        game.play(config)
    elif response == 2:
        instructions.send()
    elif response == 3:
        scores.send()
    elif response == 4:
        config_menu.edit_menu(config)
    elif response == 5:
        config_menu.send(config)

    # Reactivates menu at the end of session.
    activate_menu(config)



