from os import system
system("cls")
print("You need to run the compatability test first.")
print("Is there a symbol like this: \"퟿\"")
x = input("On top of the output screen? (y/n) ")
if x.lower() == "y":
    print("Then, your Python IDE is not compatible.")
    print("Try Visual Studio Code.")
    quit()
else:
    print("Then, your Python IDE is compatible.")
from random import randint, choice
from webbrowser import open
from subprocess import call
from datetime import datetime
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
print("Suddenly; he was transported to a Python code, where;")
print("There's a code to generate infinite dungeons.")
print("The knight decided to explore some dungeons while he stayed there.")
input("Enter to continue... ")
system("cls")
print("I.D.E.: Infinite Dungeon Engine")
input("\nEnter to continue... ")
system("cls")
class Dungeon:
    def secsToday(self):
        return datetime.now().hour * 60 * 60 + datetime.now().minute * 60 + datetime.now().second
    def __init__(self):
        self.money = 15
        self.inventory = []
        self.hp = 10
        self.bankStorage = 0
        self.bankTimeOld = self.secsToday()
        self.bankTimeNew = self.secsToday()
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
        self.hints = ['In troll markets, you can buy swords with gold.', 'In troll markets, you can buy armour with gold.', 'In troll markets, you can buy bows with gold.', 'In troll markets, you can buy arrows with gold.', 'In troll markets, you can buy food with gold.', 'In troll markets, you can sell your items with gold.', 'The troll in troll market has a company TrollCo, which has 3 branches.', 'TrollCo branch #1 is a cartography branch.', 'TrollCo branch #1 (cartography branch) lets you map all the places that have a specific room type.', "TrollCo branch #1 (cartography branch) lets you map a specific coordinate's room type.", 'TrollCo branch #2 is an information branch.', 'TrollCo branch #2 (information branch) lets you buy hints, like this one.', 'TrollCo branch #3 is a crafting branch.', 'TrollCo branch #3 (information branch) lets you craft useful items from useless junk.', 'TrollCo branch #4 is an economic branch.', 'TrollCo branch #4 (economic branch) lets you withdraw and deposit gold.', 'Some rooms are walls, so you can\'t pass through them.', 'You can sometimes find monsters on rooms.', 'You can fight monsters with swords, or bows and arrows.', 'Bows can shoot far away but can end; but swords only shoot close distances, so there\'s a chance that the monster will run away.', 'If you want to deal damage with a bow, you must have at least 1 arrow.', 'If you want to heal, eat food.', 'Armour can protect you from damage.', 'Armour have a durability, which is shown in the "defence" stat of them.', 'Monsters can damage you from a random select range.', 'Monsters can resist some damage, which is shown in their "defence" stat.', 'Dogs, zombies and skeletons are easy-tier monsters.', 'Knights, ogres and ghosts are medium-tier monsters.', 'Dragons and demons are hard-tier monsters.', 'Defeating a monster gives you random useless items, but you can get gold by selling them.', 'Defeating a monster gives you random useless items, but you can craft items from them in TrollCo Branch #3.', 'The dungeon has some treasure that include gold.', 'The dungeon has some treasure that include useful items like swords, armour, bows, arrows or food.', 'The dungeon has some treasure that include useless items, but you can get gold by selling them.', 'The dungeon has some treasure that\xa0are already taken by another person.', 'You can find rooms that are empty.', "There's a goblin, which has a random number guessing puzzle.", "There's a goblin, which has a puzzle where you say if a word is real or fake.", "There's a goblin, which has a puzzle where\xa0guess a word.", 'One room is on fire, you can burn!', 'One room has icicles that can fall on you!', 'One room has a booby trap - shooting cannons!', 'One room has trampolines which bump you.', "There's a room where you can open URL's.", "There's a room where you can open\xa0files.", "There's a room where you can\xa0run codes, and maybe cheat codes if you know this game's OOP architecture.", "There's a room to warp you in a random place.", "There's a room to warp you in\xa0specific places with gold.", 'To exit a dungeon, you must find the exit room and a key to open it.']
        self.assets = ["T", "C", "I", "M", "B", "1", "2", "3", "4", "5", "6", "7", "8", "m", "s", "o", "N", "W", "w", "f", "i", "c", "b", "X", "€", "f", ">", "?", "!"]
        self.allAssets = ["T", "C", "I", "M", "B", "0", "1", "2", "3", "4", "5", "6", "7", "8", "m", "s", "o", "N", "W", "w", "f", "i", "c", "b", "X", "€", "f", ">", "?", "!", "-", "+"]
        self.allAssetsEmoji = ["🏪", "🗺️", "ℹ️", "🛠️", "🪙", "🧱", "🐕", "🧟", "🩻", "🧙", "🧌", "👻", "🐉", "👹", "💰", "🛄", "🧰", "🔢", "🔤", "📑", "🔥", "🧊", "🏹", "🦘", "⬜", "🌐", "📁", "🖥️", "🌀", "💸", "🗝️", "🚪"]
        self.selectArmour = ""
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
        self.mapGrid = self.gridVisit.copy()
        for i in range(len(self.mapGrid)):
            self.mapGrid[i] = "⬜"
        self.currentCoord = spawn
    def visitGrid(self):
        self.gridVisit[self.currentCoord] = 1
        if self.mapGrid[self.currentCoord] == "⬜":
            self.mapGrid[self.currentCoord] = self.allAssetsEmoji[self.allAssets.index(self.grid[self.currentCoord])]
    def roomTypes(self):
        print("T - Troll Market - Place to buy and sell items")
        print("C - Troll Cartographer - Buy specific rooms' locations")
        print("I - Troll İnformation - Buy hints and tactics")
        print("M - Troll Maker - Craft items from your junk")
        print("B - Troll Bank - Deposit gold to it, and get it later")
        print("0 - Wall - A full room that's covered by wall, so you can't pass through")
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
        print("? - Warp Room - Warps you to a random place")
        print("! - Warp Room - Warps you to a select place with gold")
        print("- - Key Room - Key needed to exit dungeon location")
        print("+ - Exit Room - Dungeon exit location")
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
                print(f"Know that you have {self.money} gold left.")
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
                    print("Please don't tell, I beg you.")
                    print("Would you not tell if I let you use this market's secret?")
                    print("This market has a ... casino.")
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
    def trollCartographer(self):
        print("I'm the troll from the market!")
        print("I've founded TrollCo, which is an underground company for everything.")
        print("For example, this is its cartography branch.")
        print("You can do these here:")
        print("1 - [Get a specific room type's all coordinates] (40g)")
        print("2 - [Get a select coordinate's contents] (10g)")
        x = int(input("You: "))
        if x == 1:
            print("Okay, select the room type please:")
            self.roomTypes()
            x = input("You: ")
            self.spend = 40
            self.money -= self.spend
            if self.money < 0:
                print("What? You have money less than my price!")
                print("Go map out that yourself!")
            else:
                print("I marked all the places that has that room type, specifically; the")
                for i in range(len(self.grid)):
                    if self.grid[i] == x:
                        print(i)
                        self.mapGrid[i] = self.grid[i]
                print("coordinates. (0 = Top Left, 9 = Top Right, 90 = Bottom Left, 99 = Bottom Right)")
        elif x == 2:
            print("Okay, select the room coordinate please:")
            print("(0 = Top Left, 9 = Top Right, 90 = Bottom Left, 99 = Bottom Right)")
            x = input("You: ")
            self.spend = 10
            self.money -= self.spend
            if self.money < 0:
                print("What? You have money less than my price!")
                print("Go map out that yourself!")
            else:
                self.visitGrid[x] = self.grid[x]
                print(f"I mapped that place, which is shown as \"{self.grid[x]}\" in our system.")
                print("The system looks like:")
                self.roomTypes()
        else:
            print("What are you saying? This is not the ordinary troll market!")
            print("This is a serious branch of a serious company!")
            print("Also, good luck on your adventure.")
    def trollInfo(self):
        print("I'm the troll from the market!")
        print("I've founded TrollCo, which is an underground company for everything.")
        print("For example, this is its information branch.")
        print("Where you can buy hints for 3 gold.")
        print("1 - [Buy one]")
        print("2 - [Don't buy]")
        x = int(input("You: "))
        if x == 1:
            self.spend = 3
            self.money -= self.spend
            if len(self.hints) == 0:
                if self.money < 0:
                    print("Well, you got all my hints.")
                    print("You must be wise now - and very rich.")
                    print("But you're now bankrupt, ahhh...")
                else:
                    print("Well, you got all my hints.")
                    print("You must be wise now - and very rich.")
                    print("But you have still lots of money, how?!")
                self.money += self.spend
            elif self.money < 0:
                print("What? You have money less than my price!")
                print("Go figure out hints yourself!")
            else:
                print("Here you go, the hint is:")
                self.hintInt = randint(0, len(self.hints) - 1)
                print(self.hints[self.hintInt])
                del self.hints[self.hintInt]
        elif x == 2:
            print("Goodbye.")
        else:
            print("What are you saying? This is not the ordinary troll market!")
            print("This is a serious branch of a serious company!")
            print("Also, good luck on your adventure.")
    def trollMaker(self):
        print("I'm the troll from the market!")
        print("I've founded TrollCo, which is an underground company for everything.")
        print("For example, this is its crafting branch.")
        print("Where you can craft items for free.")
        print("Will you craft something?")
        while True:
            print("1 - [Craft]")
            print("2 - [Go]")
            x = int(input("You: "))
            if x == 1:
                print("There's a variety to craft.")
                print("1 - [Wood Dagger] - Wood, Bone")
                print("2 - [Stone Sword] - Stone, Fang")
                print("3 - [Rusty Claymore] - Stone, Horn")
                print("4 - [Iron Broadsword] - Stone, Guts, Fang")
                print("5 - [Steel Greatsword] - Stone, Cloth, Guts, Bone")
                print("6 - [Cloth Wear] - Cloth")
                print("7 - [Chain Garment] - Stone, Flesh")
                print("8 - [Stone Protector] - Stone, Bone")
                print("9 - [Iron Armour] - Stone, Guts, Skin, Wood")
                print("10 - [Steel Defence] - Stone, Fang, Flesh, Skin, Cloth")
                print("11 - [Wooden Bow] - Wood, Cloth")
                print("12 - [Steel Bow] - Stone, Cloth")
                print("13 - [Crossbow] - Stone, Wood, Skin, Cloth")
                print("14 - [Wooden Arrow] - Wood, Horn")
                print("15 - [Steel Arrow] - Stone, Horn, Fang")
                print("16 - [Iron Arrow] - Stone, Bone")
                print("17 - [Meat] - Flesh, Stone")
                print("18 - [Fish] - Flesh, Cloth")
                print("19 - [Cake] - Guts, Flesh, Skin")
                x = int(input("You: "))
                if x == 1:
                    if "Wood" in self.inventory and "Bone" in self.inventory:
                        del self.inventory[self.inventory.index("Wood")]
                        del self.inventory[self.inventory.index("Bone")]
                        self.inventory.append("Wood Dagger")
                        print("I've made a Wood Dagger for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 2:
                    if "Stone" in self.inventory and "Fang" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Fang")]
                        self.inventory.append("Stone Sword")
                        print("I've made a Stone Sword for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 3:
                    if "Stone" in self.inventory and "Horn" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Horn")]
                        self.inventory.append("Rusty Claymore")
                        print("I've made a Rusty Claymore for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 4:
                    if "Stone" in self.inventory and "Guts" in self.inventory and "Fang" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Guts")]
                        del self.inventory[self.inventory.index("Fang")]
                        self.inventory.append("Iron Broadsword")
                        print("I've made an Iron Broadsword for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 5:
                    if "Stone" in self.inventory and "Cloth" in self.inventory and "Guts" in self.inventory and "Bone" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Cloth")]
                        del self.inventory[self.inventory.index("Guts")]
                        del self.inventory[self.inventory.index("Bone")]
                        self.inventory.append("Steel Greatsword")
                        print("I've made a Steel Greatsword for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 6:
                    if "Cloth" in self.inventory:
                        del self.inventory[self.inventory.index("Cloth")]
                        self.inventory.append("Cloth Wear")
                        print("I've made a Cloth Wear for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 7:
                    if "Stone" in self.inventory and "Flesh" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Flesh")]
                        self.inventory.append("Chain Garment")
                        print("I've made a Chain Garment for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 8:
                    if "Stone" in self.inventory and "Bone" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Bone")]
                        self.inventory.append("Stone Protector")
                        print("I've made a Stone Protector for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 9:
                    if "Stone" in self.inventory and "Guts" in self.inventory and "Skin" in self.inventory and "Wood" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Guts")]
                        del self.inventory[self.inventory.index("Skin")]
                        del self.inventory[self.inventory.index("Wood")]
                        self.inventory.append("Iron Armour")
                        print("I've made Iron Armour for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 10:
                    if "Stone" in self.inventory and "Fang" in self.inventory and "Flesh" in self.inventory and "Skin" in self.inventory and "Cloth" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Fang")]
                        del self.inventory[self.inventory.index("Flesh")]
                        del self.inventory[self.inventory.index("Skin")]
                        del self.inventory[self.inventory.index("Cloth")]
                        self.inventory.append("Steel Defence")
                        print("I've made Steel Defence for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 11:
                    if "Wood" in self.inventory and "Cloth" in self.inventory:
                        del self.inventory[self.inventory.index("Wood")]
                        del self.inventory[self.inventory.index("Cloth")]
                        self.inventory.append("Wooden Bow")
                        print("I've made a Wooden Bow for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 12:
                    if "Stone" in self.inventory and "Cloth" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Cloth")]
                        self.inventory.append("Steel Bow")
                        print("I've made a Steel Bow for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 13:
                    if "Stone" in self.inventory and "Wood" in self.inventory and "Skin" in self.inventory and "Cloth" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Wood")]
                        del self.inventory[self.inventory.index("Skin")]
                        del self.inventory[self.inventory.index("Cloth")]
                        self.inventory.append("Crossbow")
                        print("I've made a Crossbow for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 14:
                    if "Wood" in self.inventory and "Horn" in self.inventory:
                        del self.inventory[self.inventory.index("Wood")]
                        del self.inventory[self.inventory.index("Horn")]
                        self.inventory.append("Wooden Arrow")
                        print("I've made a Wooden Arrow for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 15:
                    if "Stone" in self.inventory and "Horn" in self.inventory and "Fang" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Horn")]
                        del self.inventory[self.inventory.index("Fang")]
                        self.inventory.append("Steel Arrow")
                        print("I've made a Steel Arrow for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 16:
                    if "Stone" in self.inventory and "Bone" in self.inventory:
                        del self.inventory[self.inventory.index("Stone")]
                        del self.inventory[self.inventory.index("Bone")]
                        self.inventory.append("Iron Arrow")
                        print("I've made an Iron Arrow for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 17:
                    if "Flesh" in self.inventory and "Stone" in self.inventory:
                        del self.inventory[self.inventory.index("Flesh")]
                        del self.inventory[self.inventory.index("Stone")]
                        self.inventory.append("Meat")
                        print("I've made some Meat for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 18:
                    if "Flesh" in self.inventory and "Cloth" in self.inventory:
                        del self.inventory[self.inventory.index("Flesh")]
                        del self.inventory[self.inventory.index("Cloth")]
                        self.inventory.append("Fish")
                        print("I've made some Fish for you!")
                    else:
                        print("You don't have the items for me to craft!")
                elif x == 19:
                    if "Guts" in self.inventory and "Flesh" in self.inventory and "Skin" in self.inventory:
                        del self.inventory[self.inventory.index("Guts")]
                        del self.inventory[self.inventory.index("Flesh")]
                        del self.inventory[self.inventory.index("Skin")]
                        self.inventory.append("Cake")
                        print("I've made a Cake for you!")
                    else:
                        print("You don't have the items for me to craft!")
                else:
                    print("What item are you talking about?")
            elif x == 2:
                break
            print("Cool, now will you craft again?")
    def trollBank(self):
        print("I'm the troll from the market!")
        print("I've founded TrollCo, which is an underground company for everything.")
        print("For example, this is its economic branch.")
        print("You can deposit and withdraw gold here.")
        print("We actually note the inflation and the stock market down here,")
        print("So if you invest here, your money will increase a bit.")
        print(f"You have {self.money} gold.")
        print("1 - [Deposit gold]")
        print("2 - [Withdraw gold]")
        x = int(input("You: "))
        if x == 1:
            self.moneyPut = int(input("How much gold will you deposit? "))
            if self.moneyPut < 0:
                print("Are you trying to deposit negative money?")
                print("Are you OK, this place tracks inflation by tracking if random dogs or stuff catch our money and stuff.")
                print("This is the most serious branch of TrollCo, so get serious, too.")
            elif self.moneyPut == 0:
                print("Are you giving me no money and making me believe that you're seriously depositing?")
                print("Are you OK, this place tracks inflation by tracking if random dogs or stuff catch our money and stuff.")
                print("This is the most serious branch of TrollCo, so get serious, too.")
            elif self.moneyPut > self.money:
                print("Are you trying to deposit more money than what you have?")
                print("Are you OK, this place tracks inflation by tracking if random dogs or stuff catch our money and stuff.")
                print("This is the most serious branch of TrollCo, so get serious, too.")
            else:
                print(f"Then I'll deposit {self.moneyPut} gold to the vault.")
                self.money -= self.moneyPut
                self.bankStorage += self.moneyPut
        elif x == 2:
            x = int(input("How much gold will you withdraw?"))
            if x < 0:
                print("Are you trying to withdraw negative money?")
                print("Are you OK, this place tracks inflation by tracking if random dogs or things catch our money and stuff.")
                print("This is the most serious branch of TrollCo, so get serious, too.")
            elif x > self.bankStorage:
                print("You can't withdraw more than you deposited!")
                print("Are you OK, this place tracks inflation by tracking if random dogs or things catch our money and stuff.")
                print("This is the most serious branch of TrollCo, so get serious, too.")
            else:
                print(f"Then I'll withdraw {x} gold from the vault.")
                self.bankTimeNew = self.secsToday()
                self.investRate = (self.bankTimeNew - self.bankTimeOld) / 1800 * 0.1
                print(f"Your investment has increased by {self.investRate} so the gold amount you withdrew is {x + x * self.investRate}.")
                self.bankStorage -= x
                x += x * self.investRate
                self.bankTimeOld = self.bankTimeNew
                self.bankTimeNew = self.secsToday()
                self.money += x
    def wall(self):
        print("This room is a covered up by a wall.")
        print("You couldn't go there, so you returned to the room you came from.")
        if self.whereYouCame == 1:
            self.currentCoord += 1
        elif self.whereYouCame == 2:
            self.currentCoord -= 1
        elif self.whereYouCame == 3:
            self.currentCoord += 10
        elif self.whereYouCame == 4:
            self.currentCoord -= 10
    def renderEnemy(self, hp, damage1, damage2, defence, name, coords):
        if self.gridVisit[coords] == 1:
            print(f"This room once had one {name}.")
            print("But you defeated it.")
        else:
            print("You encountered a monster!")
            print(f"It's an underground {name}!")
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
                        if randint(1, 2) == 1:
                            print(f"You damage the enemy {self.swords.index(self.inventory[self.selectWeapon]) + 1 * 4} HP with your {self.inventory[self.selectWeapon]}")
                            hp -= self.swords.index(self.inventory[self.selectWeapon]) + 1 * 4
                            hp += defence
                            print(f"The {name} healed {defence} HP.")
                        else:
                            print(f"The {name} ran away, and your sword couldn't reach it.")
                    elif x == 2:
                        self.displayInventory()
                        self.bowPresent = False
                        for i in self.inventory:
                            if i in self.bows:
                                self.bowPresent = True
                        if not true:
                            print("You don't have any bows.")
                            break
                        self.arrowPresent = False
                        for i in self.inventory:
                            if i in self.arrows:
                                self.arrowPresent = True
                        if not self.arrowPresent:
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
                        for i in range(randint(1, 3)):
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
                        self.armourPresent = False
                        for i in self.inventory:
                            if i in self.armour:
                                self.armourPresent = True
                                self.selectArmour = i
                        if self.armourPresent:
                            print(f"Your {self.selectArmour} protected you.")
                            if randint(1, self.armour.index(self.selectArmour) + 1) == 1:
                                print(f"Your {self.selectArmour} broke!")
                                del self.inventory[self.inventory.index(self.selectArmour)]
                if self.hp < 0:
                    print(f"You were beaten up by the wild {name}.")
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
                self.armourPresent = False
                for i in self.inventory:
                    if i in self.armour:
                        self.armourPresent = True
                        self.selectArmour = i
                if self.armourPresent:
                    print(f"Your {self.selectArmour} protected you.")
                    if randint(1, self.armour.index(self.selectArmour) + 1) == 1:
                        print(f"Your {self.selectArmour} broke!")
                        del self.inventory[self.inventory.index(self.selectArmour)]
                if self.hp < 0:
                    print(f"You were chased (and lost) by the {name.lower()}.")
                    quit()
    def moneyTreasure(self, coords):
        if self.gridVisit[coords] == 1:
            print("This room once had a treasure.")
            print("But you got it.")
        else:
            print("This room contains a treasure!")
            self.treasure = randint(1, 20)
            print(f"You found {self.treasure} gold!")
    def stuffTreasure(self, coords):
        if self.gridVisit[coords] == 1:
            print("This room once had a treasure.")
            print("But you got it.")
        else:
            print("This room contains a treasure!")
            self.treasure = choice(self.items)
            print(f"You found some {self.treasure.lower()}!")
            for i in range(randint(1, 5)):
                self.inventory.append(self.treasure)
    def oldTreasure(self):
        print("This room contains a treasure!")
        print("But another knight took it...")
    def numberPuzzle(self):
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
                print("You were set ablaze by the fire.")
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
                print("You turned into frost particles by an icicle.")
                quit()
        else:
            print("You survived the icicles.")
    def cannonRoom(self):
        print("This room has cannons.")
        if randint(1, 2) == 1:
            print("A cannon shot you!")
            self.hp -= 2
            print(f"You have {self.hp} HP left.")
            if self.hp < 0:
                print("You were blasted into oblivion by a cannon.")
                quit()
        else:
            print("You survived the cannons.")
    def bumpRoom(self):
        print("This room consists trampolines.")
        while True:
            if randint(1, 2) == 1:
                print("You couldn't pass because of the trampolines.")
                continue
            else:
                print("You exited the room.")
                break
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
    def warpRandom(self):
        print("This room warps you to a random place!")
        input()
        self.currentCoord = randint(0, 99)
    def warpRoom(self):
        print("This room warps you to a select place for 30 gold!")
        print("1 - [Warp]")
        print("2 - [Pass]")
        if x == 1:
            self.spend = 30
            self.money -= self.spend
            if self.money < 0:
                print("You don't have sufficient money.")
            else:
                print("Where to warp?")
                self.currentCoord = int(input("You: "))
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
            elif self.locationType == "C":
                self.trollCartographer()
            elif self.locationType == "I":
                self.trollInfo()
            elif self.locationType == "M":
                self.trollMaker()
            elif self.locationType == "B":
                self.trollBank()
            elif self.locationType == "0":
                self.wall()
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
            elif self.locationType == "?":
                self.warpRandom()
            elif self.locationType == "!":
                self.warpRoom()
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
            for i in range(10):
                for j in range(10):
                    if self.currentCoord == self.mapGrid[i * 10 + j]:
                        print(end = "❌")
                    else:
                        print(end = self.mapGrid[i * 10 + j])
                print()
            print("1 - [Proceed left]")
            print("2 - [Proceed right]")
            print("3 - [Proceed up]")
            print("4 - [Proceed down]")
            print("5 - [Stay]")
            x = int(input("You: "))
            self.whereYouCame = x
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
    print("2 - [Enter Dungeon Save Code]")
    print("3 - [Generate Save Code]")
    print("4 - [Make Your Own Dungeon]")
    print("5 - [Community]")
    x = int(input("You: "))
    if x == 1:
        knight.clear()
        knight.grid = []
        for i in range(100):
            knight.grid.append(choice(knight.assets))
        knight.grid[randint(1, 99)] = "+"
        knight.grid[randint(1, 99)] = "-"
        knight.grid[0] = "T"
        while not "+" in knight.grid or not "-" in knight.grid:
            knight.grid[randint(1, 99)] = "+"
            knight.grid[randint(1, 99)] = "-"
        print("Since this dungeon is randomly generated,")
        print("Anything can happen, e.g. getting a demon (hardest monster) in the first room.")
        print("Just in case, get 100 gold.")
        knight.money = 100
        knight.startDungeon(knight.grid)
    elif x == 2:
        knight.clear()
        knight.grid = list(input("Dungeon save code: ").strip())
        knight.startDungeon(knight.grid)
    elif x == 3:
        knight.clear()
        knight.grid = []
        for i in range(100):
            knight.grid.append(choice(knight.assets))
        knight.grid[randint(1, 99)] = "+"
        knight.grid[randint(1, 99)] = "-"
        knight.grid[0] = "T"
        while not "+" in knight.grid or not "-" in knight.grid or not knight.grid[0] == "T":
            knight.grid[randint(1, 99)] = "+"
            knight.grid[randint(1, 99)] = "-"
            knight.grid[0] = "T"
        print("Here is your randomly generated save code:")
        for i in knight.grid:
            print(end = i)
        quit()
    elif x == 4:
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
        print("You can add rooms as letters:")
        knight.roomTypes()
        print("Make a dungeon by putting letters in a 10x10 grid,")
        print("And then make the whole grid a single line.")
        print("For example, a 4x4 grid:")
        print("TXXX\nXXXX\nXXXX\nX+XX")
        print("It'll be TXXXXXXXXXXXX+XX.")
        print("Then, enter it as a dungeon save code.")
        print("Maybe, try a random dungeon...")
        print("1 - [Enter Save Code]")
        print("2 - [Try Random Dungeon]")
        print("3 - [Generate Save Code]")
        print("4 - [Quit]")
        x = int(input("You: "))
        if x == 1:
            knight.clear()
            knight.grid = list(input("Dungeon save code: ").strip())
            knight.startDungeon(knight.grid)
        elif x == 2:
            knight.clear()
            knight.grid = []
            for i in range(100):
                knight.grid.append(choice(knight.assets))
            knight.grid[randint(1, 99)] = "+"
            knight.grid[randint(1, 99)] = "-"
            knight.grid[0] = "T"
            while not "+" in knight.grid or not "-" in knight.grid or not knight.grid[0] == "T":
                knight.grid[randint(1, 99)] = "+"
                knight.grid[randint(1, 99)] = "-"
                knight.grid[0] = "T"
            print("Since this dungeon is randomly generated,")
            print("Anything can happen, e.g. getting a demon (hardest monster) in the first room.")
            print("Just in case, get 100 gold.")
            knight.money = 100
            knight.startDungeon(knight.grid)
        elif x == 3:
            knight.clear()
            knight.grid = []
            for i in range(100):
                knight.grid.append(choice(knight.assets))
            knight.grid[randint(1, 99)] = "+"
            knight.grid[randint(1, 99)] = "-"
            knight.grid[0] = "T"
            while not "+" in knight.grid or not "-" in knight.grid or not knight.grid[0] == "T":
                knight.grid[randint(1, 99)] = "+"
                knight.grid[randint(1, 99)] = "-"
                knight.grid[0] = "T"
            print("Here is your randomly generated save code:")
            for i in knight.grid:
                print(end = i)
            quit()
        elif x == 4:
            quit()
    elif x == 5:
        print("To message or request new room types to I.D.E.'s maker @Lava-Salt (GitHub) or post comments to I.D.E. community forum,")
        print("Go to \"https://github.com/Lava-salt/side_projects/discussions/2\"")
        quit()
