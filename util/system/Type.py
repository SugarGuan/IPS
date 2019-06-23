def is_str(var):
    if isinstance(var, str):
        return True
    else:
        return False


def is_string(var):
    return is_str(var)


def is_int(var):
    if isinstance(var, int):
        return True
    else:
        return False


def is_integer(var):
    return is_int(var)


def is_byte(var):
    if isinstance(var, bytes):
        return True
    else:
        return False


def is_list(var):
    if isinstance(var, list):
        return True
    else:
        return False


def is_null(var):
    if var is None:
        return True
    else:
        return False


def isnot_null(var):
    if var is None:
        return False
    else:
        return True


def is_empty_str(var):
    if not is_str(var):
        return False
    if var != '':
        return False
    return True