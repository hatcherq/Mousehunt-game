import train

def main():
    train.intro()
    train.travel_to_camp()
    trap = train.setup_trap()
    train.sound_horn(trap)
    while True:
            retraining = input('\nPress Enter to continue training and "no" to stop training: ')
            if retraining == "no" :
                break
            elif retraining == "":
                trap = train.setup_trap()
                train.sound_horn(trap)

            else:
                print("Try again!")
    return trap
                
if __name__ == '__main__':
    main()
