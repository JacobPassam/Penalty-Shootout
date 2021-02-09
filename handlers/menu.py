from handlers import validation
from interface import text_format


def create_string_menu(title, display_options, back_menu):
    text_format.send_separator_message(title)
    # Detect integer range type
    success, output = validation.validate_to_int(display_options[0])
    if success:
        print("- Reply with an integer between " + str(display_options[0] + " & " + str(display_options[1])))
    else:
        for i in range(len(display_options)):
            print("- " + display_options[i])

    if back_menu:
        print("- Menu")

    validated = False
    while not validated:
        response = input("Enter your response: ").lower()
        if not response == "menu":
            if response in display_options:
                index = display_options.index(response)
                return display_options[index]
            elif success:
                success, output = validation.validate_to_int(response)
                if success:
                    if display_options[0] <= output <= display_options[1]:
                        return output
        else:
            return

        validation.validation_err()


def create_int_menu(title, display_options, back_menu):
    text_format.send_separator_message(title)
    for i in range(len(display_options)):
        print(str(i+1) + ") " + display_options[i])

    if back_menu:
        print(str(len(display_options)+1) + ") Back to menu")

    validated = False
    while not validated:
        response = input("Enter your response: ").lower()
        success, output = validation.validate_to_int(response)
        if success:
            if back_menu:
                if 1 <= output <= len(display_options)+1:
                    return output
            else:
                if 1 <= output <= len(display_options):
                    return output

        validation.validation_err()
