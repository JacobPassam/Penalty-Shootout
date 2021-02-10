from handlers import validation
from interface import text_format


# Lowers everything it can in an array
def lower_all_arr(arr):
    for i in range(len(arr)):
        try:
            arr[i] = str(arr[i]).lower()
        except:
            arr[i] = arr[i]
    return arr


def create_string_menu(title, display_options, back_menu):
    # Sends default separator message
    text_format.send_separator_message(title)
    normal_display = False

    # Detect integer range type
    if not isinstance(display_options[1], str):
        # Not a bool, TRUE = 1, False = 0
        if display_options[1] >= 2:
            # Asks additional input for a number in a certain range
            print("- Reply with an integer between " + str(display_options[0]) + " & " + str(display_options[1]))
        else:
            normal_display = True
    else:
        normal_display = True

    # Prints out all options if it is a selection menu without numbers
    if normal_display:
        display_options = lower_all_arr(display_options)
        for i in range(len(display_options)):
            print("- " + str(display_options[i]))

    # Prints out menu option if enabled.
    if back_menu:
        print("- menu")

    validated = False
    while not validated:
        # Validates response
        response = input("Enter your response: ").lower()
        if not response == "menu":
            # Checks to see if response is in valid options/responses
            if response in display_options:
                # Retrieves the index and returns the option they chose.
                index = display_options.index(response)
                return display_options[index]
            else:
                # Attempts to compare value of display_options if integer.
                try:
                    if display_options[1] >= 2:
                        # Validates to integer from string.
                        success, output = validation.validate_to_int(response)
                        if success:
                            # Compares <=> integer for validity.
                            if display_options[0] <= output <= display_options[1]:
                                return output
                except:
                    validated = False
        else:
            # Returns to go back to menu
            return None
        # Outputs error
        validation.validation_err()


def create_int_menu(title, display_options, back_menu):
    # Sends default seperator messaged
    text_format.send_separator_message(title)
    # Loops through all options and prints out.
    for i in range(len(display_options)):
        print(str(i+1) + ") " + display_options[i])

    # If back menu is enabled, it adds that option.
    if back_menu:
        print(str(len(display_options)+1) + ") Back to menu")

    validated = False
    while not validated:
        # Validates response
        response = input("Enter your response: ").lower()

        # Attempts to change responsei into integer
        success, output = validation.validate_to_int(response)
        if success:
            if back_menu:
                # Back menu enabled, checks if number is the added value of the list (+1)
                if 1 <= output <= len(display_options)+1:
                    if output == len(display_options)+1:
                        return None
                    else:
                        return output
            else:
                # Checks if number is in default range without menu added.
                if 1 <= output <= len(display_options):
                    return output
        validation.validation_err()
