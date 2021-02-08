from handlers import menu
from handlers import config as configHandler
from interface import menu as menu_interface
from interface import textFormat
from handlers import config


# Sends the configuration menu as well as displaying the inner menus, making use of handlers/menu.py
def send_menu(config_obj: configHandler):
    menu_options = config_obj.get_config("options")

    menu_choice = menu.create_menu("CONFIG MENU", "Chose an option below.", menu_options, True, config_obj)
    if menu_choice <= len(menu_options):
        inner_option_name = menu_options[menu_choice-1]
        inner_options = config_obj.get_config(menu_options[menu_choice-1])[1]
        menu_inner_choice = menu.create_word_menu("CONFIG INNER MENU", "Chose an option below.", inner_options, True, config_obj)
        if menu_inner_choice != "menu" or menu_inner_choice != None:
            config_obj.update_config(inner_option_name, menu_inner_choice)
            menu_interface.send_menu(config_obj)


# Shows the current configuration settings.
def show_current(config_obj: configHandler):
    config_obj = config.Config()

    menu_options = config_obj.get_config("options")
    textFormat.send_separator_message("CURRENT CONFIG")
    for i in range(len(menu_options)):
        print(menu_options[i] + " > " + str(config_obj.get_config(menu_options[i])[0]))
    menu_interface.send_menu(config_obj)