from interface import  textFormat
from handlers import validation
from interface import menu

# Creates a new menu to be used throughout the code
def create_menu(title, description, options, back_menu):
    # Print menu
    textFormat.send_separator_message(title)
    print(description)
    for i in range(len(options)):
        print(str(i+1) + ") " + options[i])

    # The ability to go back to menu (optional)
    back_index = 0
    if back_menu:
        back_index = len(options)+1
        print(str(len(options)+1) + ") Go back to main menu")
    print()

    # Validate input
    validated = False
    choice = 0

    while not validated:
        choice = input("Choose your option: ")
        valid = validation.validate_integer(choice, 1, len(options)+1)
        if not valid:
            validation.validation_err()
        else:
            choice = int(choice)
            validated = True
            if back_index != 0 and choice == back_index:
                menu.send_menu()
                return

    return choice


# Custom menu that accepts word reply's - for configuration editing mainly.
def create_word_menu(title, description, options, back_menu):
    # Print menu
    textFormat.send_separator_message(title)
    print(description)

    if not options == []:
        for i in range(len(options)):
            print("- " +  options[i])
    else:
        print("- Reply with a number (0-100)")

    if back_menu:
        print("- Menu")
    print()

    # Validate input
    validated = False
    choice = ""

    while not validated:
        choice = input("Choose your option: ").lower()

        if choice.lower() == "menu":
            validated = True
            choice = "menu"
            menu.send_menu()
            return
        else:
            if options == []:
                valid = validation.validate_integer(choice, 1, 100)
                if not valid:
                    validation.validation_err()
                else:
                    choice = choice.lower()
                    validated = True
            else:
                if choice.lower() in options:
                    choice = choice.lower()
                    validated = True
                else:
                    validation.validation_err()

    return choice
