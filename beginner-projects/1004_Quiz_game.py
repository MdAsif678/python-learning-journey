# Simple quiz game (questions stored in a dictionary, tracks score)

quiz = {
    "What color is the sun: ":"white",
    "What color is grass ":"green",
    "What color is sky":"blue",
    "What color is tree branch":"brown",
    "What is 82+652":"734",
    "Who won the most FIFA world cup": "brazil"
}



print("WELCOME TO PROFESSIONAL QUIZ GAME")
while True:
    try:
        choice = int(input("WHAT DO YOU WANT TO DO TODAY \n1. Play Game \n2. Exit \nEnter your choice: "))
        if choice == 1:
                score = 0
                for ques,ans in quiz.items():
                    print(ques)
                    answer = input("\nEnter your answer:")
                    if answer.lower().strip() == ans:
                        score += 1
                        print("Correct Answer!")
                    
                    else:
                        print(f"WRONG ANSWER BOOOOOOOOO,correct answer: {ans}\n")
            
                print(f"Your Score is: {score}/{len(quiz)}","\n","="*100)

        elif choice == 2:
            print("Thanks for PLAYING THE GAME")
            break

        else:
            print("INVALID CHOICE\n")
    
    except ValueError:
        print("!!!Thats not a valid Choice!!!\n")
    except KeyboardInterrupt:
        print("="*50,"Program closed","="*50)
        break


print("\a")