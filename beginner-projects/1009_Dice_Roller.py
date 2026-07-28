# Dice roller simulator (roll any number of any-sided dice)
import random

def dice_roller(sides):
    return random.randint(1,sides)

while True:
    print("WELCOME TO PROFESSIONAL DICE ROLLER")
    print("What do you want to do? \n1. Roll Die \n2. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            die = int(input("Enter the number of die you want to roll: "))
            sides = int(input("Enter the number of sides of dice you want to roll: "))
            if sides < 2:
                print("A die must have at least 2 sides.\n")
                continue
            for i in range(die):
                print(f"Die {i+1}: {dice_roller(sides)}","\n")
        elif choice == 2:
            print("Thnaks for using our dice roller.\n")
            break
        else:
            print("Invalid Choice\n")
    except ValueError:
        print("Please enter a valid number")
    
    except KeyboardInterrupt:
        print("\nClosing Program\n","="*50)
        break