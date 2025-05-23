from os import system
from random import randint, choice
from webbrowser import open
from subprocess import call
try:
    import nltk
except ModuleNotFoundError:
    system("pip install nltk")
    import nltk
nltk.download("words")
system("cls")
from nltk.corpus import words
print("One day, a brave knight decided to visit his grandmother.")
print("He packed his bag with some food and set off on his journey.")
print("While he was walking in the streets, he found a magic board.")
print("This board could open a portal to a Python project.")
print("The knight was curious and decided to touch on the board.")
print("Suddenly, he was transported to a Python code, where;")
print("There's a code to generate infinite dungeons.")
print("The knight decided to explore some dungeons while he stayed there.")
input("Enter to continue... ")
system("cls")
print("I.D.E.: Infinite Dungeon Engine")
input("\nEnter to continue... ")
system("cls")
class Dungeon:
    def __init__(self):
        self.money = 50
        self.inventory = []
        self.hp = 10
        self.beat = False
        self.swords = ["Wood Dagger", "Stone Sword", "Rusty Claymore", "Iron Broadsword", "Steel Greatsword"]
        self.armour = ["Cloth Wear", "Chain Garment", "Stone Protector", "Iron Armour", "Steel Defence"]
        self.bows = ["Wooden Bow", "Steel Bow", "Crossbow"]
        self.arrows = ["Wooden Arrow", "Steel Arrow", "Iron Arrow"]
        self.food = ["Apple", "Bread", "Meat", "Fish", "Cake"]
        self.junk = ["Horn", "Fang", "Guts", "Bone", "Flesh", "Skin", "Cloth", "Wood", "Stone"]
        self.items = ["Wood Dagger", "Stone Sword", "Rusty Claymore", "Iron Broadsword", "Steel Greatsword", "Cloth Wear", "Chain Garment", "Stone Protector", "Iron Armour", "Steel Defence", "Wooden Bow", "Steel Bow", "Crossbow", "Wooden Arrow", "Steel Arrow", "Iron Arrow", "Apple", "Bread", "Meat", "Fish", "Cake", "Horn", "Fang", "Guts", "Bone", "Flesh", "Skin", "Cloth", "Wood", "Stone"]
        self.corpus = words.words()
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def clear(self):
        system("cls")
    def displayInventory(self):
        if len(self.inventory) > 0:
            for i in range(len(self.inventory)):
                print(f"{i} - {self.inventory[i]}")
    def initGrid(self, grid, spawn):
        self.grid = grid
        self.gridVisit = self.grid.copy()
        for i in range(len(self.gridVisit)):
            self.gridVisit[i] = 0
        self.currentCoord = spawn
    def visitGrid(self):
        self.gridVisit[self.currentCoord] = 1
    def trollMarket(self):
        print("Welcome to the troll market!")
        print("Please buy my items, I live like this underground...")
        print(f"Well, you have {self.money} gold.")
        print("Do you want to buy or sell?")
        while True:
            print("1 - [Buy]")
            print("2 - [Sell]")
            x = int(input("You: "))
            if x == 1:
                print("1 - [Swords]")
                print("2 - [Armour]")
                print("3 - [Bows]")
                print("4 - [Arrows]")
                print("5 - [Food]")
                x = int(input("You: "))
                if x == 1:
                    print("1 - [Wood Dagger] - 5g, 4 damage")
                    print("2 - [Stone Sword] - 10g, 8 damage")
                    print("3 - [Rusty Claymore] - 15g, 12 damage")
                    print("4 - [Iron Broadsword] - 20g, 16 damage")
                    print("5 - [Steel Greatsword] - 25g, 20 damage")
                    x = int(input("You: "))
                    if x == 1:
                        self.money -= 5
                        self.inventory.append("Wood Dagger")
                    elif x == 2:
                        self.money -= 10
                        self.inventory.append("Stone Sword")
                    elif x == 3:
                        self.money -= 15
                        self.inventory.append("Rusty Claymore")
                    elif x == 4:
                        self.money -= 20
                        self.inventory.append("Iron Broadsword")
                    elif x == 5:
                        self.money -= 25
                        self.inventory.append("Steel Greatsword")
                elif x == 2:
                    print("1 - [Cloth Wear] - 10g, 2 defence")
                    print("2 - [Chain Garment] - 20g, 3 defence")
                    print("3 - [Stone Protector] - 30g, 4 defence")
                    print("4 - [Iron Armour] - 40g, 5 defence")
                    print("5 - [Steel Defence] - 50g, 6 defence")
                    x = int(input("You: "))
                    if x == 1:
                        self.money -= 10
                        self.inventory.append("Cloth Wear")
                    elif x == 2:
                        self.money -= 20
                        self.inventory.append("Chain Garment")
                    elif x == 3:
                        self.money -= 30
                        self.inventory.append("Stone Protector")
                    elif x == 4:
                        self.money -= 40
                        self.inventory.append("Iron Armour")
                    elif x == 5:
                        self.money -= 50
                        self.inventory.append("Steel Defence")
                elif x == 3:
                    print("1 - [Wooden Bow] - 5g, 4 damage")
                    print("2 - [Steel Bow] - 10g, 8 damage")
                    print("3 - [Crossbow] - 15g, 12 damage")
                    x = int(input("You: "))
                    if x == 1:
                        self.money -= 5
                        self.inventory.append("Wooden Bow")
                    elif x == 2:
                        self.money -= 10
                        self.inventory.append("Steel Bow")
                    elif x == 3:
                        self.money -= 15
                        self.inventory.append("Crossbow")
                elif x == 4:
                    print("1 - [Wooden Arrow] - 1g, 4 damage")
                    print("2 - [Steel Arrow] - 2g, 8 damage")
                    print("3 - [Iron Arrow] - 3g, 12 damage")
                    x = int(input("You: "))
                    if x == 1:
                        self.money -= 5
                        self.inventory.append("Wooden Arrow")
                    elif x == 2:
                        self.money -= 10
                        self.inventory.append("Steel Arrow")
                    elif x == 3:
                        self.money -= 15
                        self.inventory.append("Iron Arrow")
                elif x == 5:
                    print("1 - [Apple] - 5g, 1 health")
                    print("2 - [Bread] - 10g, 2 health")
                    print("3 - [Meat] - 15g, 3 health")
                    print("4 - [Fish] - 20g, 4 health")
                    print("5 - [Cake] - 25g, 5 health")
                    x = int(input("You: "))
                    if x == 1:
                        self.money -= 5
                        self.inventory.append("Apple")
                    elif x == 2:
                        self.money -= 10
                        self.inventory.append("Bread")
                    elif x == 3:
                        self.money -= 15
                        self.inventory.append("Meat")
                    elif x == 4:
                        self.money -= 20
                        self.inventory.append("Fish")
                    elif x == 5:
                        self.money -= 25
                        self.inventory.append("Cake")
                if self.money < 0:
                    print("Wait, you gave no money?")
                    print("You trying to scam, huh?!")
                    print("Take your money back, and I'll take my item back!")
                    self.money = 0
                    del self.inventory[-1]
                    print("Okay, now will you go?")
                else:
                    print("Cool choice, will you go now?")
                print("1 - [Go]")
                print("2 - [Stay]")
                x = int(input("You: "))
                if x == 1:
                    print("Nice to meet you and good luck!")
                    break
                elif x == 2:
                    print("You will stay now?")
                    print("Go select an item now, I hope it helps, man.")
                elif x == 3:
                    print("How did you know my secret?")
                    print("Don't tell anyone that I evade that goblin's tax.")
                    print("Also, this market's also a casino.")
                    print("Since you know my secret, I let you gamble freely.")
                    print("You can gamble money: give me money,")
                    print("I will flip a rock. If it is a head, you win double money.")
                    print("If it is a tail, you lose your money. Wanna try?")
                    print("1 - [Gamble]")
                    print("2 - [No]")
                    x = int(input("You: "))
                    if x == 1:
                        print("Okay, how much money will you give me?")
                        print(f"By the way, you have {self.money} gold.")
                        self.gamble = int(input("You: g"))
                        if self.money <= 0:
                            print("What, you have no money!")
                            print("And you trying to gamble?")
                            print("Wait - you know my secret...")
                            print("Just forget it.")
                        self.money -= self.gamble
                        if self.money < 0:
                            self.money += self.gamble
                            print("Well, that money is so much - it exceeds your money.")
                            print("Get your money back please.")
                        else:
                            print("Let's flip that rock here...")
                            if randint(0, 1) == 0:
                                print(f"Head? Here's the {self.gamble * 2}g I promised.")
                                print("Probably, I should close the gambling option...")
                            else:
                                print(f"Tail! You lose the {self.gamble}g you gave.")
                                print("Here's a lesson: don't gamble your gold and go away!")
                                print("Nice to meet you, bye the way.")
                                break
                    else:
                        print("Okay, you don't want to gamble.")

                else:
                    print("I don't understand you.")
                    print("So I assume that you'll stay.")
            else:
                print("What will you sell me?")
                self.displayInventory()
                if len(self.inventory) == 0:
                    print("You have nothing?")
                    print("Then why are you trying to sell?")
                    continue
                x = int(input("You: "))
                if x < 0 or x >= len(self.inventory):
                    print("Let me check your inventory...")
                    print("Nothing! That doesn't exist.")
                    print("So you are selling nothing.")
                    print("I understand.")
                else:
                    print(f"Okay, you are selling {self.inventory[x]}")
                    self.price = randint(1, 10)
                    self.money += self.price
                    del self.inventory[x]
                    print("OK, my plan is to sell this for -")
                    print(f"Like {self.price} gold.")
                print("Cool choice, will you go now?")
                print("1 - [Go]")
                print("2 - [Stay]")
                x = int(input("You: "))
                if x == 1:
                    print("Nice to meet you and good luck!")
                    break
                elif x == 2:
                    print("You will stay now?")
                    print("Go select an item now, I hope it helps, man.")
                elif x == 3:
                    print("How did you know my secret?")
                    print("Don't tell anyone that I evade that goblin's tax.")
                    print("Also, this market's also a casino.")
                    print("You can gamble money: give me money,")
                    print("I will flip a rock. If it is a head, you win double money.")
                    print("If it is a tail, you lose your money. Wanna try?")
                    print("1 - [Gamble]")
                    print("2 - [No]")
                    x = int(input("You: "))
                    if x == 1:
                        print("Okay, how much money will you give me?")
                        print(f"By the way, you have {self.money} gold.")
                        self.gamble = int(input("You: g"))
                        if self.money <= 0:
                            print("What, you have no money!")
                            print("And you trying to gamble?")
                            print("Wait - you know my secret...")
                            print("Just forget it.")
                        self.money -= self.gamble
                        if self.money < 0:
                            self.money += self.gamble
                            print("Well, that money is so much - it exceeds your money.")
                            print("Get your money back please.")
                        else:
                            print("Let's flip that rock here...")
                            if randint(0, 1) == 0:
                                print(f"Head? Here's the {self.gamble * 2}g I promised.")
                                print("Probably, I should close the gambling option...")
                            else:
                                print(f"Tail! You lose the {self.gamble}g you gave.")
                                print("Here's a lesson: don't gamble your gold and go away!")
                                print("Nice to meet you, bye the way.")
                                break
                else:
                    print("I don't understand you.")
                    print("So I assume that you'll stay.")
    def renderEnemy(self, hp, damage1, damage2, defence, name, coords):
        if self.gridVisit[coords] == 1:
            print(f"This room once had a {name}.")
            print("But you defeated it.")
        else:
            print("You encountered a monster!")
            print(f"It's a {name}!")
            while True:
                print(f"{name}:")
                print(f"    Health: {hp}")
                print(f"    Damage: {damage1} to {damage2} HP")
                print(f"    Defence: {defence}")
                print("You:")
                print(f"    Health: {self.hp}")
                print(f"    Money: {self.money}")
                print("1 - [Attack]")
                print("2 - [Heal]")
                print("3 - [Run]")
                x = int(input("You: "))
                if x == 1:
                    print("1 - [Sword Attack]")
                    print("2 - [Bow Attack]")
                    x = int(input("You: "))
                    if x == 1:
                        self.displayInventory()
                        while True:
                            self.selectWeapon = int(input("You: "))
                            if self.selectWeapon < 0 or self.selectWeapon >= len(self.inventory) or not(self.inventory[self.selectWeapon] in self.swords):
                                print("Invalid choice.")
                                continue
                            else:
                                break
                        print(f"You damage the enemy {self.swords.index(self.inventory[self.selectWeapon]) + 1 * 4} HP with your {self.inventory[self.selectWeapon]}")
                        hp -= self.swords.index(self.inventory[self.selectWeapon]) + 1 * 4
                        hp += defence
                        print(f"The {name} healed {defence} HP.")
                    elif x == 2:
                        self.displayInventory()
                        true = False
                        for i in self.inventory:
                            if i in self.bows:
                                true = True
                        if not true:
                            print("You don't have any bows.")
                            break
                        true = False
                        for i in self.inventory:
                            if i in self.arrows:
                                true = True
                        if not true:
                            print("You don't have any arrows.")
                            break
                        while True:
                            self.selectWeapon = int(input("You: "))
                            if self.selectWeapon < 0 or self.selectWeapon >= len(self.inventory) or not(self.inventory[self.selectWeapon] in self.bows):
                                print("Invalid choice.")
                                continue
                            else:
                                break
                        print(f"You damage the enemy {self.bows.index(self.inventory[self.selectWeapon]) + 1 * 4} HP with your {self.inventory[self.selectWeapon]}")
                        hp -= (self.bows.index(self.inventory[self.selectWeapon]) + 1 * 4) + (self.arrows.index(self.inventory[self.selectWeapon]) + 1)
                        hp += defence
                        print(f"The {name} healed {defence} HP.")
                    if hp < 0:
                        print(f"You killed the {name}!")
                        self.stuff = choice(self.junk)
                        print(f"You got some {self.stuff.lower()}.")
                        for i in range(randint(1, 10)):
                            self.inventory.append(self.stuff)
                        break
                elif x == 2:
                    true = False
                    for i in self.inventory:
                        if i in self.food:
                            true = True
                    if not true:
                        print("You don't have any food.")
                        break
                    self.displayInventory()
                    x = int(input("You: "))
                    self.choiceFood = self.inventory[x]
                    if x < 0 or x >= len(self.inventory) or not(self.choiceFood in self.food):
                        print("Invalid choice.")
                        continue
                    elif self.choiceFood in self.food:
                        print(f"You eat the {self.choiceFood.lower()} and heal {self.food.index(self.choiceFood) + 1} HP.")
                        self.hp += self.food.index(self.choiceFood) + 1
                        del self.inventory[x]
                elif x == 3:
                    if randint(1, 3) == 1:
                        print("You outran the enemy!")
                        break
                    else:
                        print("You couldn't outrun the enemy!")
                        self.damage = randint(damage1, damage2)
                        print(f"It attacked {self.damage} HP.")
                        self.hp -= self.damage
                        true = False
                        for i in self.inventory:
                            if i in self.armour:
                                true = True
                                if not true:
                                    self.selectArmour = i
                        if true:
                            print(f"Your {self.selectArmour} protected you.")
                            if randint(1, self.armour.index(self.selectArmour) + 1) == 1:
                                print(f"Your {self.selectArmour} broke!")
                                del self.inventory[self.inventory.index(self.selectArmour)]
                if self.hp < 0:
                    self.clear()
                    print("You died.")
                    quit()
                print(f"{name}:")
                print(f"    Health: {hp}")
                print(f"    Damage: {damage1} to {damage2} HP")
                print(f"    Defence: {defence}")
                print("You:")
                print(f"    Health: {self.hp}")
                print(f"    Money: {self.money}")
                self.damage = randint(damage1, damage2)
                print(f"The {name} attacked {self.damage} HP.")
                self.hp -= self.damage
                true = False
                for i in self.inventory:
                    if i in self.armour:
                        true = True
                        if not true:
                            self.selectArmour = i
                if true:
                    print(f"Your {self.selectArmour} protected you.")
                    if randint(1, self.armour.index(self.selectArmour) + 1) == 1:
                        print(f"Your {self.selectArmour} broke!")
                        del self.inventory[self.inventory.index(self.selectArmour)]
                if self.hp < 0:
                    self.clear()
                    print("You died.")
                    quit()
    def moneyTreasure(self, coords):
        if self.gridVisit[coords] == 1:
            print("This room once had a treasure.")
            print("But you got it.")
        else:
            print("This room contains a treasure!")
            self.treasure = randint(1, 200)
            print(f"You found {self.treasure} gold!")
    def stuffTreasure(self, coords):
        if self.gridVisit[coords] == 1:
            print("This room once had a treasure.")
            print("But you got it.")
        else:
            print("This room contains a treasure!")
            self.treasure = choice(self.items)
            print(f"You found some {self.treasure.lower()}!")
            for i in range(randint(1, 10)):
                self.inventory.append(self.treasure)
    def oldTreasure(self):
        print("This room contains a treasure!")
        print("But another knight took it...")
    def emptyRoom(self):
        print("This room is empty.")
    def randomPuzzle(self):
        print("Hello, I'm a goblin.")
        print("If you want to pass, guess my number.")
        self.number = randint(1, 100)
        while True:
            self.guess = int(input("You: "))
            if self.guess == self.number:
                print("You guessed it correct...")
                print("You shall enter.")
                print("Also, how's my troll friend, he has a market.")
                break
            elif self.guess < self.number:
                print("That's lower than mine.")
            elif self.guess > self.number:
                print("That's much higher than my number!")
    def wordPuzzle(self):
        print("Hello, I'm a goblin.")
        print("If you want to pass, guess if my word is real or not.")
        print("Say \"real\" or \"fake\".")
        while True:
            self.word = choice(self.corpus)
            self.real = True
            if randint(1, 2) == 1:
                self.wordlist = list(self.word)
                self.wordlist[randint(0, len(self.wordlist) - 1)] = choice(self.alphabet)
                self.real = False
            print(f"The word is {self.word}.")
            self.guess = input("You: ").lower()
            if self.guess == "real":
                if self.real:
                    print("You guessed it correct...")
                    print("You shall enter.")
                    print("Also, how's my troll friend, he has a market.")
                    break
                else:
                    print("That's incorrect.")
                    print("Try again!")
            elif self.guess == "fake":
                if not self.real:
                    print("You guessed it correct...")
                    print("You shall enter.")
                    print("Also, how's my troll friend, he has a market.")
                    break
                else:
                    print("That's incorrect.")
                    print("Try again!")
            else:
                print("I don't know what you said.")
                print("Let's try again with a new word.")
    def wordGuess(self):
        print("Hello, I'm a goblin.")
        print("If you want to pass, guess my word in 10 tours.")
        while True:
            self.word = choice(self.corpus)
            print(f"The word has {len(self.word)} letters.")
            self.guess = input("You: ").lower()
            if self.guess == self.word:
                print("You guessed it correct...")
                print("You shall enter.")
                print("Also, how's my troll friend, he has a market.")
                break
            else:
                print("That's incorrect.")
                print("But i'll say what you got.")
                for i in range(len(self.word)):
                    if self.word[i] == self.guess[i]:
                        print(f"Your letter #{i + 1}, {self.guess[i]} is in the correct place.")
                    elif self.guess[i] in self.word:
                        print(f"Your letter #{i + 1}, {self.guess[i]} is not in the correct place, but it is a letter in the word.")
                    else:
                        print(f"Your letter #{i + 1}, {self.guess[i]} is a total failed attempt.")
    def fireRoom(self):
        print("This room is on fire!")
        if randint(1, 2) == 1:
            print("You got burned!")
            self.hp -= 5
            print(f"You have {self.hp} HP left.")
            if self.hp < 0:
                self.clear()
                print("You died.")
                quit()
        else:
            print("You survived the fire.")
    def iceRoom(self):
        print("This room has icicles.")
        if randint(1, 2) == 1:
            print("An icicle fell to you!")
            self.hp -= 1
            print(f"You have {self.hp} HP left.")
            if self.hp < 0:
                self.clear()
                print("You died.")
                quit()
        else:
            print("You survived the fire.")
    def cannonRoom(self):
        print("This room has cannons.")
        if randint(1, 2) == 1:
            print("A cannon shot you!")
            self.hp -= 2
            print(f"You have {self.hp} HP left.")
            if self.hp < 0:
                self.clear()
                print("You died.")
                quit()
        else:
            print("You survived the fire.")
    def bumpRoom(self):
        print("This room consist trampolines.")
        while True:
            if randint(1, 2) == 1:
                print("You couldn't pass because of the trampolines.")
                continue
            else:
                print("You exited the room.")
                pass
    def emptyRoom(self):
        print("This room is empty.")
    def eRoom(self):
        print("This is an e-room!")
        print("You can open URL's here.")
        x = input("You: ")
        open(x)
    def fileRoom(self):
        print("This is a file room!")
        print("You can open files here.")
        x = input("You: ")
        call(x)
    def codeRoom(self):
        print("This is a code room!")
        print("You can run code here.")
        x = input("You: ")
        try:
            exec(x)
        except Exception:
            system(x)
    def keyRoom(self):
        print("This room has a key.")
        print("Keys can open dungeon exits.")
        self.inventory.append("Key")
    def exitRoom(self):
        if "Key" in self.inventory:
            print("This room has the dungeon exit door, only opened with a key.")
            print("Since you have a key, you open the lock,")
            print("And proceed outside.")
            self.beat = True
        else:
            print("This room has the dungeon exit door, only opened with a key.")
            print("Since you don't have a key, go find one.")
    def displayStats(self):
        print(f"Health: {self.hp}")
        print(f"Money: {self.money} gold")
        print("Inventory:")
        for i in self.inventory:
            print(f"    - {i}")
    def startDungeon(self, grid):
        self.initGrid(grid, 0)
        while True:
            self.displayStats()
            input()
            self.clear()
            self.locationType = self.grid[self.currentCoord]
            if self.locationType == "T":
                self.trollMarket()
            elif self.locationType == "1":
                self.renderEnemy(3, 1, 2, 0, "Dog", self.currentCoord)
            elif self.locationType == "2":
                self.renderEnemy(6, 2, 4, 1, "Zombie", self.currentCoord)
            elif self.locationType == "3":
                self.renderEnemy(10, 3, 6, 2, "Skeleton", self.currentCoord)
            elif self.locationType == "4":
                self.renderEnemy(15, 4, 8, 3, "Knight", self.currentCoord)
            elif self.locationType == "5":
                self.renderEnemy(20, 5, 10, 4, "Ogre", self.currentCoord)
            elif self.locationType == "6":
                self.renderEnemy(25, 6, 12, 5, "Ghost", self.currentCoord)
            elif self.locationType == "7":
                self.renderEnemy(30, 7, 14, 6, "Dragon", self.currentCoord)
            elif self.locationType == "8":
                self.renderEnemy(50, 10, 20, 10, "Demon", self.currentCoord)
            elif self.locationType == "m":
                self.moneyTreasure(self.currentCoord)
            elif self.locationType == "s":
                self.stuffTreasure(self.currentCoord)
            elif self.locationType == "o":
                self.oldTreasure()
            elif self.locationType == "N":
                self.numberPuzzle()
            elif self.locationType == "W":
                self.wordPuzzle()
            elif self.locationType == "w":
                self.wordGuess()
            elif self.locationType == "f":
                self.fireRoom()
            elif self.locationType == "i":
                self.iceRoom()
            elif self.locationType == "c":
                self.cannonRoom()
            elif self.locationType == "b":
                self.bumpRoom()
            elif self.locationType == "X":
                self.emptyRoom()
            elif self.locationType == "€":
                self.eRoom()
            elif self.locationType == "F":
                self.fileRoom()
            elif self.locationType == ">":
                self.codeRoom()
            elif self.locationType == "-":
                self.keyRoom()
            elif self.locationType == "+":
                self.exitRoom()
            else:
                print(self.locationType)
                print("Save code invalid.")
                print(self.grid)
                quit()
            self.visitGrid()
            print(f"Location: Room #{self.currentCoord} of 10x10 grid dungeon")
            print("1 - [Proceed left]")
            print("2 - [Proceed right]")
            print("3 - [Proceed up]")
            print("4 - [Proceed down]")
            x = int(input("You: "))
            if x == 1:
                if self.currentCoord - 1 < 0:
                    print("You can't go any farther in this direction.")
                    continue
                else:
                    self.currentCoord -= 1
            elif x == 2:
                if self.currentCoord + 1 >= len(self.grid):
                    print("You can't go any farther in this direction.")
                    continue
                else:
                    self.currentCoord += 1
            elif x == 3:
                if self.currentCoord - 10 < 0:
                    print("You can't go any farther in this direction.")
                    continue
                else:
                    self.currentCoord -= 10
            elif x == 4:
                if self.currentCoord + 10 >= len(self.grid):
                    print("You can't go any farther in this direction.")
                    continue
                else:
                    self.currentCoord += 10
            self.clear()
            if self.beat:
                break
        print("Congrats!")
        print("You finished the dungeon!")
        print("Dungeon save code:")
        for i in self.grid:
            print(i, end = "")
        quit()
while True:
    knight = Dungeon()
    knight.clear()
    print("Welcome to the Infinite Dungeon Engine!")
    print("1 - [Play Randomly Generated Dungeon]")
    print("2 - [Play Enter Dungeon Save Code]")
    print("3 - [Make Your Own Dungeon]")
    print("4 - [Community]")
    x = int(input("You: "))
    if x == 1:
        knight.clear()
        knight.grid = []
        for i in range(100):
            knight.grid.append(choice(["T", "1", "2", "3", "4", "5", "6", "7", "8", "m", "s", "o", "N", "W", "f", "i", "c", "b", "X", "€", "f", ">"]))
        knight.grid[randint(1, 99)] = "+"
        knight.grid[randint(1, 99)] = "-"
        knight.grid[0] = "T"
        while not "+" in knight.grid or not "-" in knight.grid:
            knight.grid[randint(1, 99)] = "+"
            knight.grid[randint(1, 99)] = "-"
        print("Since this dungeon is randomly generated,")
        print("Anything can happen, e.g. getting a demon (hardest monster) in the first room.")
        print("Just in case, get 1000 gold.")
        knight.money = 1000
        knight.startDungeon(knight.grid)
    elif x == 2:
        knight.clear()
        knight.grid = list(input("Dungeon save code: ").strip())
        knight.startDungeon(knight.grid)
    elif x == 3:
        print("Welcome to the dungeon maker!")
        print("You can make your own dungeon here.")
        print("To make a dungeon, you need to put letters in a 10x10 grid.")
        custom = []
        for i in range(100):
            custom.append("X")
        custom[0] = "T"
        custom[98] = "-"
        custom[99] = "+"
        for i in range(10):
            for j in range(10):
                print(end = custom[i * 10 + j])
            print()
        print("This is a sample dungeon in a 10x10 grid.")
        print("You can add rooms as letters:")
        print("T - Troll market - Place to buy and sell items")
        print("1 - Enemy - Dog")
        print("2 - Enemy - Zombie")
        print("3 - Enemy - Skeleton")
        print("4 - Enemy - Knight")
        print("5 - Enemy - Ogre")
        print("6 - Enemy - Ghost")
        print("7 - Enemy - Dragon")
        print("8 - Enemy - Demon")
        print("m - Treasure - Treasure with gold")
        print("s - Treasure - Treasure with items")
        print("o - Treasure - Already taken treasure")
        print("N - Puzzle - Goblin's number puzzle")
        print("W - Puzzle - Goblin's fake word puzzle")
        print("w - Puzzle - Goblin's word guess puzzle")
        print("f - Room - Room on fire")
        print("i - Room - Icicles fall")
        print("c - Room - Cannons shoot you")
        print("b - Room - Trampolines (you bump)")
        print("X - Room - Empty")
        print("€ - E-Room - Open URL's")
        print("F - File Room - Open files")
        print("> - Code Room - Run code")
        print("- - Key Room - Key needed to exit dungeon location")
        print("+ - Exit Room - Dungeon exit location")
        print("Make a dungeon by putting letters in a 10x10 grid,")
        print("And then make the whole grid a single line.")
        print("For example, a 4x4 grid:")
        print("TXXX\nXXXX\nXXXX\nX+XX")
        print("It'll be TXXXXXXXXXXXX+XX.")
        print("Then, enter it as a dungeon save code.")
        print("Or try my trial dungeon!")
        print("1 - [Try My Dungeon!]")
        print("2 - [Enter Save Code]")
        print("3 - [Quit]")
        x = int(input("You: "))
        if x == 1:
            knight.clear()
            knight.grid = list("T>1mWNf€Xbw2mmsWXiFfii213>bcc>323Ffsossm€F45mmm4€c4if€msoXXNNNXwW56>X-XXXcbbb>€XX+XT6FNXsmXXxf78wXms")
            print("Thanks for trying my dungeon!")
            print("As a reward, you start with 200 gold!")
            knight.money = 200
            knight.startDungeon(knight.grid)
        elif x == 2:
            knight.clear()
            knight.grid = list(input("Dungeon save code: ").strip())
            knight.startDungeon(knight.grid)
        elif x == 3:
            quit()
    elif x == 4:
        print("To message or request new room types to I.D.E.'s maker @Lava-Salt (GitHub) or post comments to I.D.E. community forum,")
        print("Go to \"https://github.com/Lava-salt/side_projects/discussions/2\"")
