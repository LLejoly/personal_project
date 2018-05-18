def is_valid_number(s):
    if isinstance(s, int):
        if s >= 0:
            return True
        return False
    if isinstance(s, str):
        if s.isdigit():
            return True
        return False

    return False
