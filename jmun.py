from os import system
from time import sleep
from random import randint, choice, random
print("JMUN Simulator\n")
print("Example Committees: GA, UNICEF, SC, SOCHUM, CSW, ECOSOC, FCC, ILO, LEGAL, UNIDO, JCC")
com = input("Enter committee: ")
top = input("Enter topic: ")
delnum = int(input("The number of delegates: "))
deleg = []
for i in range(delnum - 1):
    deleg.append(input(f"Enter delegate #{i + 1}: "))
your = input(f"Enter delegate #{delnum} which is you: ")
yname = input("Your own full name: ")
gnd = input("Enter gender (yes, we need that data, m/f): ")
deleg.append(your)
def clr():
    system("cls")
clr()
print("Preparation\n")
print("Write an opening speech.")
print("/----------\\")
print("OPENING SPEECH\n")
print(f"Committee: {com}")
print(f"Topic: {top}")
print(f"Country: {your}")
print(f"Delegate: {yname}\n")
print(f"Honourable Chair, {choice(["distinguished", "esteemed"])} delegates,")
opening = [f"Honourable Chair, {choice(["distinguished", "esteemed"])} delegates,"]
opening.append(input("\n    "))
for i in range(2):
    opening.append(input("\n"))
opening.append("Thank you, Honourable Chair.")
print("Thank you, Honourable Chair.\n\\----------/\n")
print("Write a position paper.")
print("/----------\\")
print("POSITION PAPER\n")
print(f"Committee: {com}")
print(f"Topic: {top}")
print(f"Country: {your}")
print(f"Delegate: {yname}\n")
print("I. Background of the Issue\n")
input("    ")
print("\nII. Country's Position\n")
input("    ")
input("\nIII. Proposed Solutions\n1. ")
input("    ")
input("\n2. ")
input("    ")
input("\n3. ")
input("    ")
print("\\----------/\n")
print("Write a general speech.")
print("/----------\\")
print("GENERAL SPEECH\n")
print(f"Committee: {com}")
print(f"Topic: {top}")
print(f"Country: {your}")
print(f"Delegate: {yname}\n")
print(f"Honourable Chair, {choice(["distinguished", "esteemed"])} delegates,")
general = [f"Honourable Chair, {choice(["distinguished", "esteemed"])} delegates,"]
general.append(input("\n"))
for i in range(4):
    general.append(input("\n"))
general.append("Thank you, Honourable Chair.")
print("Thank you, Honourable Chair.\n\\----------/\n")
print("Write motions.")
motnum = int(input("Write how many motions? "))
motions = []
for i in range(motnum):
    motions.append(input(f"Motion #{i + 1}: "))
print("\nGet dressed.")
dress = []
if gnd.lower() == "m":
    none = ["Suit", "Trousers", "Jacket", "Tie", "Dark Shoes", "Sportswear", "Jeans"," Traditional Clothes", "Military Uniform"]
else:
    none = ["Skirt", "Dress", "Trousers", "Blouse", "Too Short Skirt", "Traditional Clothes", "Facial Piercing", "Coloured Hair (How in the World you Wear this)", "Shawl"]
wear = ":)"
while wear != "quit":
    for i in range(len(none)):
        print(f"{i + 1}. {none[i]}")
    print(f"{i + 1}. Finish Getting Dressed")
    wear = int(input())
    if wear == i + 1:
        wear = "quit"
    else:
        dress.append(none[i])
        del none[none.index(dress[-1])]
input("You finished preparing. ")
clr()
print("Registration")
lobby = 472497527
while lobby > len(deleg):
    lobby = int(input("Do lobbying with how many delegates? "))
    if lobby > len(deleg):
        print("Invalid number of delegates.")
deleg2 = deleg.copy()
lobbyers = []
for i in range(lobby):
    x = randint(1, len(deleg2))
    lobbyers.append(deleg2[x])
    del deleg2[x]
nonlobby = []
for i in lobbyers:
    input("You: Do you want to do lobbying?")
    if randint(1, 2) == 1:
        input(f"{i}: What's that?")
        input("You: You second my motions, I second yours.")
    if randint(1, 2) == 1:
        input(f"{i}: Cool, I accept.")
    else:
        input(f"{i}: No, thanks.")
        nonlobby.append(i)
for i in nonlobby:
    del lobbyers[lobbyers.index[nonlobby[i]]]
input()
clr()
print("Opening Ceremony\n")
input("Secretary-General: Highly esteemed delegates,")
input("First and foremost, I would like to express my sincere gratitude for your interest and enthusiasm regarding our conference. I have the honour of serving as your Secretary-General for the 8th edition of the Troy Model United Nations Conference this year. I embrace this role with immense appreciation. Similar to previous years, we have dedicated our efforts to creating a range of engaging and diverse committees for your benefit. We take great pride in the work we have prepared for you and sincerely hope that you will find it beneficial as well. Both the academic and operations teams have been working very hard to serve you to the best of their abilities and give you an unforgettable experience. I wish to show my gratitude to the chair board, who is going to serve as your Under-Secretary-General. All my teammates made great efforts in the process leading up to the conference. Hence, they need all the praise for their hard work. I trust that all our delegates will engage in enlightening discussions throughout the three days they are with us, cultivate creative solutions to global challenges, be at the forefront of diplomacy and academia, and enjoy the experience in the process. Once again, I would like to welcome you all to both the conference and the committee. Buckle up and get ready because we have prepared an incredible ride for you.")
input(f"Under-Secretary-General: Greetings, I am the USG in the JMUN conference. I believe that today, with my experience and your enthusiasm we can experience an academic, enriching and fun day. Me and my lovely co-chairs have prepared the most easily understood and helpful study guide that we could create. At any time you can find us to ask conference related questions, we will be ready to help you. If you have any prior questions about the guide or the committee, you can email me and I will respond as quickly as possible. Eat an apple, revise hard and prepare yourself for the conference. Welcome to {com}!")
clr()
input("I will add more content. This is it for now :(")
