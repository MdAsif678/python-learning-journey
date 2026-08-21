# Palindrome checker for sentences (ignores spaces and punctuation)
sentence = input("Enter a sentence: ")
sent2 = ""
for letter in sentence:
    if letter.isalnum():
        sent2 += letter.lower()


if sent2 == sent2[::-1]:
    print("The sentence is palidrome.")
else:
    print("The sentence is not palindrome.")