import time

def print_slowly(text, delay=0.08):
    """Prints the given text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def greet():
    while True:  # Keep asking until a valid input is provided
        choice = input("\nHow can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop\n")
        if choice in ["1", "2", "3"]:  # Check if the choice is one of the valid options
            return choice
        else:
            print_slowly("Invalid choice! Please select 1, 2, or 3.")  # Error message for invalid input

def buy_cheese(gold: int, cheese_bought: int = 0) -> tuple:
    gold_spend = 0
    print_slowly(f"You have {gold} gold to spend.")
    amount_str = input("State [cheese quantity]: ").strip().lower()
    if amount_str == "back":
        return gold_spend, cheese_bought
    elif amount_str.startswith('cheddar') :
            cheese_type, amount = amount_str.split()
            amount = int(amount)
            gold_spend = int(amount) * 10
            if amount <= 0:
                gold_spend = 0
                print_slowly("Must purchase a positive amount of cheese!")
                
            
            elif gold_spend > gold:
                gold_spend = 0
                print_slowly("Insufficient gold!")
                
            else:
                print_slowly(f"Successfully purchase {amount} cheddar!")
                cheese_bought+=int(amount)
                
    else:
        print_slowly("Sorry, did not understand.Please enter in the format 'cheddar [quantity]'.")
    return gold_spend , cheese_bought

def display_inventory(gold: int, cheese_bought: int, trap: str) -> None:
    
    print_slowly(f"Gold - {gold}\nCheddar - {cheese_bought}\nTrap - {trap}")


def main():
    gold = 125
    cheese_bought = 0
    trap = "Cardboard and Hook Trap"
    print("Welcome to The Cheese Shop!\nCheddar - 10 gold")
    while True:
        choice=greet()
        if choice == "1":
            gold_spent, cheese_bought = buy_cheese(gold, cheese_bought)
            gold = gold - gold_spent

        elif choice == "2":
            display_inventory(gold, cheese_bought, trap)

        elif choice == "3":
            break
        
        

if __name__ == "__main__":
    main()
