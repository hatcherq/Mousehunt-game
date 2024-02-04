import Title
import name
import retrain
import random
import shop
import time

def print_slowly(text, delay=0.08):
    """Prints the given text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def bob():
    hunter_name=input("\nWhat's ye name, Hunter?\n")
    if name.is_valid_name(hunter_name):
        print_slowly(f"Welcome to the Kingdom, Hunter {hunter_name}!")
        return hunter_name
    else:
        print_slowly("Welcome to the Kingdom, Hunter Bob!")
        return "Bob"


def train_or_not():
    trap = "Cardboard and Hook Trap"
    print_slowly("Before we begin, let's train you up!")
    choice=input(f'Press "Enter" to start training or "skip" to Start Game: ')
    if choice == "":
        print("")
        trap=retrain.main()
    elif choice == "skip":
        None
        


    return trap



def join_hunt(gold,cheese_bought,point):
    
    i=0
    
    while i<5:
        print_slowly("Sound the horn to call for the mouse...")
        time.sleep(2)
        answer=input(f'Sound the horn by typing "yes", Stop hunt by typing "stop" : ').strip()

        if answer=="yes" and int(cheese_bought)>0:
            if random.random() <= 0.4:
                print_slowly("Caught a Brown mouse!")
                gold+=125
                point+=115
                cheese_bought-=1
                i=0
                print(f"My gold: {gold}, My points: {point}\n")
            else:
                print_slowly('Nothing happens.')
                print(f"My gold: {gold}, My points: {point}\n")
                i+=1
                cheese_bought-=1

        elif answer=="yes" and int(cheese_bought) == 0:
            print_slowly("Nothing happens. You are out of cheese!")
            print(f"My gold: {gold}, My points: {point}\n")
            i+=1

        elif answer=="stop":
            i=5
            break
        
        else:
            print_slowly("Try again!")
            print(f"My gold: {gold}, My points: {point}\n")
            i+=1
        
        if i==5:
                continue_the_hunt=input("Do you want to continue to hunt? ").lower()
                if continue_the_hunt == "no":
                    pass
                else:
                    i=0

    return gold,cheese_bought,point




def main():
    gold = 125
    cheese_bought = 0
    cost = 0
    point=0
    trap = "Cardboard and Hook Trap"
    hunter_name = bob()
    trap = train_or_not()

    while True:
        try:
            user_pick = int(input(f"\nWhat do ye want to do now, Hunter {hunter_name}?\n1. Exit game\n2. Join the Hunt\n3. The Cheese Shop\n"))
            if user_pick not in [1, 2, 3]:
                raise ValueError  # Manually raise a ValueError if the input is not 1, 2, or 3
        except ValueError:
            print_slowly("Invalid choice! Please enter a valid number (1, 2, or 3).")
            continue
        if user_pick==1:
            return None
        elif user_pick==2:
            gold,cheese_bought,point= join_hunt(gold,cheese_bought,point)
        elif user_pick==3:
            print_slowly("Welcome to The Cheese Shop!\nCheddar - 10 gold")
            choice=shop.greet()
            while choice == "1" or choice == "2" :
                if choice=="1":
                    gold_spent, cheese_bought = shop.buy_cheese(gold, cheese_bought)
                    gold = gold - gold_spent
                elif choice =="2":
                    shop.display_inventory(gold, cheese_bought, trap)
                choice=shop.greet()
        else:
            print_slowly("Invalid choice! Please enter a valid number (1, 2, or 3).")

if __name__ == "__main__" :
    main()






