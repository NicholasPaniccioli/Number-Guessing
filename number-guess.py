import random

#Fields
user_chances = 0
rand_num = 0
attempts = 0
quit_game = False

#Helper methods
def start_game(chances):
    x = chances
    y = random.randrange(1,100)
    z = 0
    print("\nGame has started! Good luck!")
    return x,y,z #user chances, rand num, attempts respectively

#Welcome player to the game
print("Welcome to the Number Guessing Game!" \
"\nA random number between 1 and 100 will be chosen." \
"\nTry to guess the number within a few guesses. Goodluck!")

#loops program until user quits the game
while not quit_game:
    #Showcase the difficulty levels & take user selection
    print("\nSelect the difficulty level:" \
    "\n1. Easy (10 chances)" \
    "\n2. Medium (5 chances)" \
    "\n3. Hard (3 chances)" \
    "\n4. Quit the game")

    user_input = input("\nEnter your choice: ").strip()

    #Set Players chances and start game
    if user_input == "1":
        print("\nGreat! You selected Easy. You have 10 chances!")
        user_chances, rand_num, attempts = start_game(10)
    elif user_input == "2":
        print("\nGreat! You selected Medium. You have 5 chances!")
        user_chances, rand_num, attempts = start_game(5)
    elif user_input == "3":
        print("\nGreat! You selected Hard. You have 3 chances!")
        user_chances, rand_num, attempts = start_game(3)
    elif(user_input == "4"):
        print("\nYou're exiting the game, goodbye!")
        quit_game = True
    else:
        print("\nPlease select a valid option from 1 to 4.")

    #loops until game is over
    while user_chances > 0:
        try:
            user_guess = input("\nEnter your guess: ").strip()
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
                    print("\nNice try, unfortunately you did not guess the number." \
                    "\nLet's try again though!")
            else:
                attempts += 1
                print("Congrats! You guessed the correct number in " + str(attempts) + " attempts." )
                user_chances = 0
                break
        except ValueError:
            print("Was expecting a number value, but was given a string instead." \
            "\nPlease input a number.")
        
        
