import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randit(min_value, max_value)

    return roll

while True: 
    players = input("Enter the number of players (2 - 4): ")
    if players.isdidgit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else: 
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    should_roll = input("Would you like to roll (y)? ")
    if should_roll.lower() != "y":
        break

        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
        else: