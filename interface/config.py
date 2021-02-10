from handlers.config import Config as configHandler
from interface import text_format
from handlers import menu


# Sends editing menu to change configuration.
def edit_menu(config: configHandler):
    menu_options = config.retrieve_config_list()
    response = menu.create_int_menu("CONFIG MENU", menu_options, True)
    # Awaits response from menu
    if not response: return

    # Retrieves the selected choice in the menu via their option. 1 = 0, 2 = 1. (lists start from 0)
    selected_choice = menu_options[response-1]

    # Retrieves response in inner config menu from the config options available for the configuration setting.
    response = menu.create_string_menu("INNER CONFIG MENU", config.retrieve_config_options(selected_choice), True)
    if not response: return

    # Updates the configuration and goes through validity checks.
    config.update_config(selected_choice, response)
    return


def send(config: configHandler):
    # Retrieves the current configuration list
    menu_options = config.retrieve_config_list()
    text_format.send_separator_message("CURRENT CONFIG")
    # Prints out each configuration setting.
    for i in range(len(menu_options)):
        print(menu_options[i] + " > " + str(config.retrieve_config(menu_options[i])))
    return
