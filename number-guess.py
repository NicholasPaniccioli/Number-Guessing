import random

#Helper methods
def start_game(chances):
    global user_chances
    global rand_num
    global attempts
    user_chances = chances
    rand_num = random.randrange(1,100)
    attempts = 0
    print("\nGame has started! Good luck!")


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

#Set Players chances and start game
if user_input == "1":
    print("\nGreat! You selected Easy. You have 10 chances!")
    start_game(10)
elif user_input == "2":
    print("\nGreat! You selected Medium. You have 5 chances!")
    start_game(5)
elif user_input == "3":
    print("\nGreat! You selected Hard. You have 3 chances!")
    start_game(3)
    print(rand_num)
else:
    print("You did not select a valid difficulty.")

#loops until game is over
while user_chances > 0:
    user_guess = input("Enter your guess: ")
    if user_guess != str(rand_num) and int(user_guess) > rand_num:
        print("Incorrect! The number is less than " + user_guess)
        user_chances -= 1
        attempts += 1
        if user_chances == 0:
            print("Nice try, unfortunately you did not guess the number.")
    elif user_guess != str(rand_num) and int(user_guess) < rand_num:
        print("Incorrect! The number is greater than " + user_guess)
        user_chances -= 1
        attempts += 1

        if user_chances == 0:
            print("Nice try, unfortunately you did not guess the number.")
    else:
        attempts += 1
        print("Congrats! You guessed the correct number in " + str(attempts) + " attempts." )
        break
