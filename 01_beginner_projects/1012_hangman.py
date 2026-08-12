import random

words = ["apple", "banana", "watermelon", "mango", "strawberry"]
lives = 5
word = random.choice(words)
holder = ["_"]*len(word)
print("Welcome to professional Hangman GAME!!")
guessed = set()
while lives > 0:
    print(f"Lives: {lives}")
    g_word = input(f"\n{" ".join(holder)}\n\nGuess the Letter: ").lower()

    if g_word in guessed:
        print("You already guessed that letter!")
        continue

    
    if len(g_word) != 1 or not g_word.isalpha():
        print("Please enter a single letter,no digits allowed")
        continue
    guessed.add(g_word)
    if g_word not in word:
        print("Wrong Guess")
        lives -= 1
    
    else:
        for i in range(len(word)):
            if word[i] == g_word:
                holder[i] = g_word
        
        print("Correct Guess!")

    if "_" not in holder:
        print("YOu guessed the word, CONGRATS!")
        break

if lives == 0:
    print(f"\nYou lost! The word was: {word}")