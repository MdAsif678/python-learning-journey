import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
punc = string.punctuation

print("WELCOME TO PROFESSIONAL PASSWORD GENERATOR V2")
while True:
    print("What would you like to do \n1. Generate a password \n2. Check Complexity Score of your password \n3. Exit\n")
    try:
        choice = int(input("Enter Your choice: "))
        password = ""
        if choice == 1:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Not a valid length\n")
                continue
            isupper = input("Incluce upper case letters(y/n): ")
            islower = input("Incluce lower case letters(y/n): ")
            isdig = input("Include digits(y/n): ")
            ispunc = input("Incluce punctuations(y/n): ")
            pool = ""

            if isupper.lower() == "y":
                pool += upper
            if islower.lower() == "y":
                pool += lower
            if isdig.lower() == "y":
                pool += digits
            if ispunc.lower() == "y":
                pool += punc
            
            if len(pool) == 0:
                print("No valid characters available to generate a password you desire")
                continue

            while len(password)< length:
                password += random.choice(pool)
            
            print(f"The generated password is: {password}","\n")

        elif choice == 2:
            score = 0
            passw = input("Enter your password: ")
            if any(letter.isupper() for letter in passw):
                score += 1
            if any(letter.islower() for letter in passw):
                score += 1
            if any(letter.isdigit() for letter in passw):
                score += 1
            if any(letter in punc for letter in passw):
                score += 1
            
            if len(passw) >= 8:
                score += 1
            if len(passw) >= 12:
                score += 1
                
            if score == 6:
                print(f"Score = {score}\nVery Strong password\n")
            elif 4 <= score <= 5:
                print(f"Score = {score}\nStrong password\n")
            elif score == 3:
                print(f"Score = {score}\nModerate password\n")
            elif score <3:
                print(f"Score = {score}\nWeak Password\n")

            if len(passw) > 100 and score ==6:
                print("NOTE: YOU HAVE AN ULTRA SUPER PRO MAX STRONG PASSWORD\n")

        elif choice == 3:
            print("Thanks for using our password generator\n")
            break
        else:
            print("No such choice available")
    except ValueError:
        print("Thats not a valid choice\n")
    except KeyboardInterrupt:
        print("\nProgram Closing\n") 
        break