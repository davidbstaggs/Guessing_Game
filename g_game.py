"""

Project 1 - Number Guessing Game
--------------------------------
"""

import random
def start_game(num):
    print("Welcome to the Guessing Game")
    ans = 0
    count = 1
    highscore = 4000
    while ans != num:
        ans = input("Please guess a number from 1 to 4000:  ")
        try:
            ans = int(ans)
            if ans < 1 or ans > 4000:
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
                    num = random.randint(1,4000)
                    count = 0
                else:
                    print("Thanks for playing!!")

            count +=1





start_game(random.randint(1,4000))
