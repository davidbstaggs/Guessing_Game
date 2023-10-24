"""

Project 1 - Number Guessing Game
--------------------------------
"""

import random
def start_game(num):
    print("Welcome to the Guessing Game")
    ans = 0
    count = 1
    highscore = 10
    while ans != num:
        ans = input("Please guess a number from 1 to 10:  ")
        try:
            ans = int(ans)
            if ans < 1 or ans > 10:
                raise ValueError(f"{ans} is outside the range of numbers")
        except ValueError as err:
            print(f"Oh no, we ran into an issue ({err}), please try again")
        else:
            if ans > num:
                print("It's lower")
            elif ans < num:
                print("It's higher")
            else:
                print("You got it!")
                print(f"That took you {count} times")
                if count < highscore:  # Check if the current score is a new highscore
                    highscore = count
                    print(f"New highscore: {highscore} attempts!")
                working = input(f"Would you like to play again?  (Y)es/(N)o   ")
                if working.lower() in "yes":
                    print(f"Great, remember, the high score to beat is {highscore}!")
                    num = random.randint(1,10)
                    count = 0

                else:
                    print("Thanks for playing!!")

            count +=1





start_game(random.randint(1,10))

