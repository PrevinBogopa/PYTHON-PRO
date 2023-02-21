
import random
import math

# ask for lower and upper bounds
lower_bound = int(input("Enter Lower bound: "))
upper_bound = int(input("Enter Upper bound: "))

# calculate chances based on bounds
chances = round(math.log(upper_bound - lower_bound + 1, 2))
print(f"\nYou've only {chances} chances to guess the integer!\n")

# generate a random number between bounds
secret_number = random.randint(lower_bound, upper_bound)

# initialize the number of guesses
num_of_guesses = 0

# game loop
while num_of_guesses < chances:
    # ask for user's guess
    guess = int(input("Guess a number: "))
    
    # check if the guess is correct
    if guess == secret_number:
        print(f"\nCongratulations you did it in {num_of_guesses + 1} tries")
        print(f"The number is {secret_number}")
        break
    # check if the guess is too high
    elif guess > secret_number:
        print("You Guessed too high!")
    # otherwise, the guess is too low
    else:
        print("You guessed too small!")
        
    # increment the number of guesses
    num_of_guesses += 1

if num_of_guesses == chances:
    print(f"\nBetter Luck Next time!\nThe number is {secret_number}")