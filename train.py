import time

def print_slowly(text, delay=0.08):
    """Prints the given text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print_slowly("I'm Hatcher. Welcome to training centre, I'll be your hunting instructor.")

def travel_to_camp():
    print_slowly("Let's go to the Meadow to begin your training!")
    input("Press Enter to travel to the Meadow...")
    print_slowly("Travelling to the Meadow....")
    time.sleep(5)
    print_slowly("Hatcher: This is your camp. Here you'll set up your mouse trap.")


def setup_trap():
    print_slowly("Hatcher: Let's get your first trap...")
    input("Press Enter to view traps that Hatcher is holding...")
    print_slowly("Hatcher is holding...")
    time.sleep(2)
    print_slowly("Left: High Strain Steel Trap")
    print_slowly("Right: Hot Tub Trap")
    trap = input("Select a trap by typing \"left\" or \"right\": ").strip()
    if trap == "right":
        print_slowly('''Hatcher: Excellent choice.
Your "Hot Tub Trap" is now set!
Hatcher: You need cheese to attract a mouse.''')
        print('Hatcher places one cheddar on the trap!')
        trap = "Hot Tub Trap"

    elif trap == "left":
        print_slowly('''Hatcher: Excellent choice.
Your "High Strain Steel Trap" is now set!
Hatcher: You need cheese to attract a mouse.''')
        print('Hatcher places one cheddar on the trap!')
        trap = "High Strain Steel Trap"
    else:
        print_slowly('''No trap selected.
Hatcher: Odds are slim with no trap!''')
        trap = "Cardboard and Hook Trap"
    return trap

def sound_horn(trap):
    print_slowly("Sound the horn to call for the mouse...")
    sound = input("Sound the horn by typing \"yes\": ").strip()
    if sound =="yes":
        has_sound_horn=True
    else:
        has_sound_horn=False
    
    if has_sound_horn==True and (trap=="Hot Tub Trap" or trap=="High Strain Steel Trap"):
        print_slowly("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
    elif has_sound_horn==False and trap=="Cardboard and Hook Trap":
        print_slowly("Nothing happens.")
    else:
        print_slowly("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
        
def main():
    trap="Cardboard and Hook Trap"
    intro()
    travel_to_camp()
    trap=setup_trap()
    sound_horn(trap)

if __name__ == "__main__" :
    main()


