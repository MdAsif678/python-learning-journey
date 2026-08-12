# Simple ATM simulator (deposit/withdraw/balance, saved to JSON)
import json

class ATM:
    def __init__(self,balance):
        self.balance = balance
    
    def deposit(self,amount):
        if amount <= 0:
            print("Please enter non negative number\n")
            return
        self.balance += amount
        print(f"{amount} Deposited.\n")
        return self.balance
    
    def withdraw(self,amount):
        if amount <= 0:
            print("Please enter non negative number\n")
            return
        if amount > self.balance:
            print("Your account doesnt have enough credits.\n")
            return
        self.balance -= amount
        print(f"{amount} withdrawn.\n")
        return self.balance

    def show_bal(self):
        print(f"Current Balance: ${self.balance:.2f}\n")
        return self.balance

    
accounts = {
    "Asif" : 4000,
    "John" : 55000,
    "Xinping" : 350000
}

while True:
    print("WELCOME TO OUR ATM")
    print("1. Log in to your account \n2. Create new account \n3. Show all acounts \n4. Save Accounts \n5. Load Accounts \n6. Exit")
    
    try:
        choice0 = int(input("Enter your choice: "))
        if choice0 == 1:
            username = input("Please enter your name: ")
            if username in accounts:
                atm = ATM(accounts[username])
                while True:
                    print(f"\nHello {username},\nWhat would you like to do today \n1. Deposit Cash \n2. Withdraw Cash \n3. Show Balance \n4. Exit")
                    try:
                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            amount = float(input("Enter the amount you want to deposit: "))
                            total = atm.deposit(amount)
                            if total is not None:
                                accounts[username] = total
                        
                        elif choice == 2:
                            amount = float(input("Enter the amount you want to withdraw: "))
                            total = atm.withdraw(amount)
                            if total is not None:
                                accounts[username] = total
                        
                        elif choice == 3: 
                            atm.show_bal()
                        
                        elif choice == 4:
                            print("Thank you for using our ATM")
                            print("="*50)
                            break

                        else:
                            print("Not a valid choice\n")

                    except ValueError:
                        print("Thats not a valid number\n")
                    
                    except KeyboardInterrupt:
                        print("\nClosing Program")
                        print("="*100)
                        break
            else:
                print("No such account exists\n")
        elif choice0 == 2:
            name = input("Please enter the name of new account holder: ")
            amount = float(input("Please enter the amount you want to initially store: "))
            if amount <= 0:
                print("Not a valid amount to deposit\n")
                continue
            if name in accounts:
                print("Account already exists\n")
                continue
            accounts[name] = amount
            print("Account created successfully\n")

        
        elif choice0 == 3:
            print()
            for name, bal in accounts.items():
                print(f"{name} : {bal}")
            print()
        
        elif choice0 == 4:
            with open("1011_accounts.json","w") as f:
                json.dump(accounts, f, indent = 4)
            
            print("Accounts saved successfully\n")

        
        elif choice0 == 5:
            try:
                with open("1011_accounts.json","r") as f:
                    accounts = json.load(f)
                
                print("Accounts loaded successfully\n")
            except FileNotFoundError:
                print("No such file exists\n")
                continue
        
        elif choice0 == 6:
            print("Farewell\n")
            print("="*100)
            break

        else:
            print("That choice doesnt exist\n")    
        
    except ValueError:
        print("Not a valid number\n")
    
    except KeyboardInterrupt:
        print("\nClosing Program\n")
        print("="*100)
        break