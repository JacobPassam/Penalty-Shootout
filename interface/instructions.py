from interface import textFormat
from interface import menu
from handlers import config as configHandler

# Sends the instructions to the interface and returns to menu.
def send(config_obj: configHandler):
    textFormat.send_separator_message("INSTRUCTIONS")
    print("1 - Choose your option (left, centre, right)")
    print("2 - If the keeper chooses the same option, they win a point.")
    print("3 - If you choose a different option compared to the keeper, you get a point.")
    print("4 - If you get more scores than the keeper, you win, if not, you loose.")
    menu.send_menu(config_obj)


