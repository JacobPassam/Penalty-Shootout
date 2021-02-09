from handlers import validation
from interface import text_format


def lower_all_arr(arr):
    for i in range(len(arr)):
        try:
            arr[i] = str(arr[i]).lower()
        except:
            arr[i] = arr[i]
    return arr


def create_string_menu(title, display_options, back_menu):
    text_format.send_separator_message(title)
    # Detect integer range type

    if not isinstance(display_options[1], str):
        if display_options[1] >= 2:
            print("- Reply with an integer between " + str(display_options[0]) + " & " + str(display_options[1]))
        else:
            display_options = lower_all_arr(display_options)
            for i in range(len(display_options)):
                print("- " + str(display_options[i]))
    else:
        display_options = lower_all_arr(display_options)
        for i in range(len(display_options)):
            print("- " + str(display_options[i]))


    if back_menu:
        print("- menu")

    validated = False
    while not validated:
        response = input("Enter your response: ").lower()
        if not response == "menu":
            if response in display_options:
                index = display_options.index(response)
                return display_options[index]
            else:
                try:
                    if display_options[1] >= 2:
                        success, output = validation.validate_to_int(response)
                        if success:
                            if display_options[0] <= output <= display_options[1]:
                                return output
                except:
                    validated = False
        else:
            return None
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
                    if output == len(display_options)+1:
                        return None
                    else:
                        return output
            else:
                if 1 <= output <= len(display_options):
                    return output
        else:
            return None
        validation.validation_err()
