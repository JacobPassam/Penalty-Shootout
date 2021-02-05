# Validates an integer from a string, checking its minimum and maximum value allowed.
def validate_integer(integer, minimum, maximum):
    try:
        number = int(integer)
        if minimum <= number <= maximum:
            return True
        else:
            return False
    except ValueError:
        return False


# Used to print out one line of text to ensure everything is the same throughout the code.
def validation_err():
    print("[VALIDATION] Error")