import time

def print_slowly(text, delay=0.08):
    """Prints the given text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


title = "MOUSEHUNT"
logo = '''
       ____()()
      /      @@
`~~~~~\_;m__m._>o
'''
author = "creator - hatcherqiu"
credits = f'''Inspired by Mousehunt© Hitgrab
{author}
Mice art - Joan Stark'''

print(title)
print_slowly(logo)
print_slowly(credits)
