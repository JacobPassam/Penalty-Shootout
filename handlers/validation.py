# Format return: success, output (int)
def validate_to_int(string):
    try:
        integer = int(string)
        return True, integer
    except ValueError:
        return False, False


# Format return: success, output
def validate_to_bool(string):
    try:
        if string.lower() == "false":
            return True, False
        elif string.lower() == "true":
            return True, True
        else:
            return False, False
    except ValueError:
        return False, False


def bool_to_string(bool):
    try:
        if bool:
            return True, "True"
        elif not bool:
            return True, "False"
        else:
            return False, False
    except:
        return False


def int_to_string(int):
    return True, str(int)


def validation_err():
    print("[VALIDATION] Error")
