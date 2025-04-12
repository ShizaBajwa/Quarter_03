import random

def hangman():
    words = ['python', 'programming', 'hangman', 'developer', 'keyboard']
    word = random.choice(words)
    guessed = []
    tries = 6
    display = ['_'] * len(word)

    while tries > 0 and '_' in display:
        print(f"Word: {' '.join(display)} | Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You already guessed that.")
        elif guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong guess.")
            tries -= 1
        guessed.append(guess)

    if '_' not in display:
        print(f"Congrats! You guessed the word: {word}")
    else:
        print(f"Out of tries! The word was: {word}")

hangman()
