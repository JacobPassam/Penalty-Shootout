from handlers import menu
from interface import instructions
from interface import config
from interface import viewScores
from interface.game import game

MENU_OPTIONS = ["Play the game", "Read instructions", "View all scores", "Edit Configuration", "View Configuration"]


# Sends the default menu
def send_menu():
    menu_choice = menu.create_menu("MAIN MENU", "Chose an option below.", MENU_OPTIONS, False)

    if menu_choice == 1:
        game.play()
    elif menu_choice == 2:
        instructions.send()
    elif menu_choice == 3:
        viewScores.send()
    elif menu_choice == 4:
        config.send_menu()
    elif menu_choice == 5:
        config.show_current()
    else:
        send_menu()
