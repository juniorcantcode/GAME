import random

# loop
while True:

    choise = input("Roll The Dice? (y/n): ")

    if choise == "y" or choise == "Y":

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print(f'({die1}, {die2})')

    elif choise == "n" or choise == "N":

        print("Maa Chuda Bsdk")
        break

    else:

        print("invalid Hai lawde")
        
        # my first project ig lol