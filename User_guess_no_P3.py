import random

def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
    print(f"Congratulations! You guessed the number {number} correctly!")

guess(100)
