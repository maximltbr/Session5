# You have 3 lives. I roll the dice. If I roll 6, you win.
# If not a 6, you lose 1 life.

from random import randint

lives = 3

while lives:
    roll = randint(1,6)
    if roll == 6:
        print("You rolled a six! You win!")
        break
    else:
        print(f"You rolled a {roll}! You lose a life!")
        lives -= 1
        print(f"You have {lives} lives left")