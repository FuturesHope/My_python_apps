

import random, sys

#start the game: Describe, tell the rules, ask for the name
print("Hi, this is the 'Guess the number' game")
print('You will be given 6 chances to guess a num from 1 to 20 including with the help of hints')
player_name = input("Please write your name ")
secret_number = random.randint(1,21)
print(f"Lets's start the game {player_name}, i picked a number, guess it..")
#ask for the guessings

for num_of_guesses in range(1,7):
    try:
        player_guess=int(input("What's your guess? "))
        if(player_guess == secret_number):
            print(f"Yes, you guessed it in {num_of_guesses}! It's {secret_number}")
            sys.exit()
        elif(player_guess<secret_number):
            print("Go higher..")
        elif(player_guess>secret_number):
            print("Take lower..")
    except Exception:
        print("An error occured, contact Al..")
# If code arrived here , that means that 6 guesses expired
print(f"You ran out of 6 chances, the num was {secret_number}")
