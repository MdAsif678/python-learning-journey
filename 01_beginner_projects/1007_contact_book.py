contact = {
        'Asif': {
        'phone': '9876543210',
        'email': 'asif@gmail.com'
    }
}

while True:
    print("WELCOME TO PROFESSIONAL CONTACT BOOK")
    print("1. Add Contact\n2. Search Contact\n3. View All Contacts\n4. Update Contact\n5. Delete Contact\n6. Count Contacts\n7. Exit\n")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Please enter the name of the person: ")
            phone = input("Enter the number of the person: ")
            email = input("Enter the email of the person: ")

            contact[name] = {
                "phone" : phone,
                "email" : email
            }
            print("Contact added Successfully\n")
        
        elif choice == 2:
            name = input("Please enter the name of the person: ")
            if name in contact:
                print("="*50,"\n")
                print(contact[name],"\n")
                print("="*50,"\n")
            else:
                print("No such contact exists")
        
        elif choice == 3:
            print("="*50,"\n")
            for name, info in contact.items():
                print(f"Name : {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}\n")
            
            print("="*50,"\n")

        elif choice == 4:
            print("1. Update Name \n2. Update Number \n3. Update Email")
            try:
                choice2 = int(input("Enter your choice: "))
                name = input("Please enter the name of the contact you want to update: ")
                if name in contact:
                    if choice2 == 1:
                        name2 = input("Please enter new name: ")
                        contact[name2] = contact[name]
                        contact.pop(name)
                        print("Updated name successfully\n")
                    
                    elif choice2 == 2:
                        number = input("Please Enter new number: ")
                        contact[name]["phone"] = number
                        print("Updated number successfully\n")
                    
                    elif choice2 == 3:
                        email = input("Please Enter new email: ")
                        contact[name]["email"] = email
                        print("Updated email successfully\n")
                    else:
                        print("Invalid Choice")
                else:
                    print("No such Contact exists\n")
            
            except ValueError:
                print("Not a valid choice\n")
        
        elif choice == 5:
            name = input("Please enter the name of the contact you want to delete: ")
            if name in contact:
                contact.pop(name)
                print("Contact deleted successfully\n")
            else:
                print("No such contact found\n")
        
        elif choice == 6:
            print(f"The number of contacts you have is: {len(contact)}\n")
        
        elif choice == 7:
            print("Thanks for using our contact book")
            break
        
        else:
            print("Thats an invalid Choice")
            print("="*50,"\n")
    except ValueError:
        print("That is not a number")
    
    except KeyboardInterrupt:
        print("\nProgram closing")
        print("="*50)
        break


