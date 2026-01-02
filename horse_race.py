# Horse race simulation, but after each race, their winning chances change.

from random import randint
from time import sleep
from os import system
print("Welcome to the Horse Race Simulator!")
print("If you think this just prints a random horse name, you're wrong.")
print("Because if they win, the chance of it winning increases.")
print("Long later, only one horse will be able to win.")
horses = [
    "White",
    "Green",
    "Peacock",
    "Plum",
    "Scarlet",
    "Mustard",
    "Orchid",
    "Violet",
    "Azure",
    "Cyan"
]
chances = [10] * 10
interval = float(input("Interval between races (seconds): "))
matches = horses.copy()
debug = 0
while True:
    for i in range(10):
        print(f"Horse {i + 1}#: {horses[i]} - {chances[i]}% Win Chance")
    while True:
        for i in range(10):
            big = 100
            if randint(0, big) <= chances[i]:
                print(f"{horses[i]} won the latest race.")
                winner = horses[i]
                break
            else:
                big -= chances[i]
        try:
            debug = winner
            break
        except Exception:
            continue
    matches.append(winner)
    for i in range(10):
        percentage = 0
        for j in matches:
            if j == horses[i]:
                percentage += 1
        percentage = 100 / len(matches) * percentage
        chances[i] = percentage
    sleep(interval)
    system("cls")
