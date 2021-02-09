from handlers.config import Config as configHandler
from interface import text_format
from handlers import menu


def edit_menu(config: configHandler):
    menu_options = config.retrieve_config_list()
    response = menu.create_int_menu("CONFIG MENU", menu_options, True)
    if not response: return

    selected_choice = menu_options[response-1]

    response = menu.create_string_menu("INNER CONFIG MENU", config.retrieve_config_options(selected_choice), True)
    if not response: return

    config.update_config(selected_choice, response)
    return


def send(config: configHandler):
    menu_options = config.retrieve_config_list()
    text_format.send_separator_message("CURRENT CONFIG")
    for i in range(len(menu_options)):
        print(menu_options[i] + " > " + str(config.retrieve_config(menu_options[i])))
    return
