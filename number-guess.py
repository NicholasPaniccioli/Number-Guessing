#Welcome player to the game
print("Welcome to the Number Guessing Game!" \
"\nA random number between 1 and 100 will be chosen." \
"\nTry to guess the number within a few guesses. Goodluck!")

#Showcase the difficulty levels & take user selection
print("\nSelect the difficulty level:" \
"\n1. Easy (10 chances)" \
"\n2. Medium (5 chances)" \
"\n3. Hard (3 chances)")

user_input = input("\nEnter your choice: ")

#Start the game/loop till guesses hit 0 
#or correct guess is given.
if user_input == "1":
    print("\nGreat! You selected Easy. You have 10 chances!")
elif user_input == "2":
    print("\nGreat! You selected Medium. You have 5 chances!")
elif user_input == "3":
    print("\nGreat! You selected Hard. You have 3 chances!")
else:
    print("You did not select a valid difficulty.")
