# WARNING: This game makes you casino addict. If you want to become casino addict, play this game.
# WARNING: Don't play this game unless you have self-control.

import random as r
import os

money = 1000
while True:
    os.system("cls")
    print(f"Money: ${money}")
    x = float(input("Bet how much money? $"))
    if r.randint(1, 2) == 1:
        print("You won the bet!")
        win = x * 2
        print(f"You earned ${win}")
    else:
        win = x * -1
        print("You lost the bet!")
    input()
    money += win
