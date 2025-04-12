import random

def play():
    user = input("Choose 'rock', 'paper', or 'scissors': ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    if is_win(user, computer):
        return "You won!"
    return "You lost!"

def is_win(player, opponent):
    return (player == 'rock' and opponent == 'scissors') or \
           (player == 'scissors' and opponent == 'paper') or \
           (player == 'paper' and opponent == 'rock')

print(play())
