print ("Larry: What's ye name, Hunter?")
name = input()
print(f"Larry: Is '{name}' a name I can pronounce?")


def length(string):
    if 1 <= len(string) <= 9:
        return True
    else:
        return False

is_valid_length = length(name)
print(f"It has a length of {len(name)} which is between 1 to 9 characters? {is_valid_length}!")


def alphabet(string):
    if string[0].isalpha():
        return True
    else:
        return False
is_valid_start = alphabet(name)
print (f"It starts with an alphabet? {is_valid_start}")

def single(string):
    if ' ' not in string:
        return True
    else:
        return False
is_one_word = single(name)
print (f"It is a single word? {is_one_word}")


def pronounce(name):
    if is_valid_length and is_valid_start and is_one_word:
        return True
    else:
        return False
is_valid_name = pronounce(name)


print (f"Larry: I can pronounce this name --- {is_valid_name}")

