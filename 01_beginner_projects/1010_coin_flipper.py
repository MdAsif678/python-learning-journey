# Coin flip simulator (flip n times, show heads/tails percentage)
import random

def coin_flipper():
    return random.randint(0,1)

while True:
    print("WELCOME TO PROFESSIONAL COIN FLIPPER")
    print("1. Flip coin \n2. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter the number of coins you want to flip: "))
            if n <= 0:
                print("Number of flips must be greater than 0.\n")
                continue
            head = 0
            tail = 0
            for i in range(n):
                value = coin_flipper()
                if value == 0:
                    print(f"Coin {i+1}: Head")
                    head += 1
                elif value == 1:
                    print(f"Coin {i+1}: Tail")
                    tail += 1
            
            print(f"\nHead: {head}")
            print(f"Tail: {tail}")
            print(f"\nHeads appeared {(head/n)*100:.2f}% of the times")
            print(f"Tails appeared {(tail/n)*100:.2f}% of the times\n")
            print("="*100)

        elif choice == 2:
            print("Thanks for using coin flipper")
            break
        
        else:
            print("Invalid Choice\n")
    
    except ValueError:
        print("Not a valid number")
    
    except KeyboardInterrupt:
        print("\nClosing Program\n")
        break