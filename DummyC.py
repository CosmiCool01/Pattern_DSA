import random

number = random.randint(1, 100)   # computer picks a secret number
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break   # stop the loop once the guess is right