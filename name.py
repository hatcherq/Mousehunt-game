def is_valid_length (string):
    if 1 <= len(string) <= 9:
        return True
    else:
        return False


def is_valid_start(string):
    if string[0].isalpha():
        return True
    else:
        return False

def is_one_word(string):
    if ' ' not in string:
        return True
    else:
        return False

def is_valid_name(string):
    if is_valid_length(string) and is_valid_start(string) and is_one_word(string):
        return True
    else:
        return False






