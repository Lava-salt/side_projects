# Cool 2-D text-based sandbox game!
from os import system, name
from datetime import datetime
from subprocess import run
if name != "nt":
    print("Sandbox is not compatible with this device, please use Windows NT.")
for i in range(1, 6):
    exec(f"d_set{i}b, d_set{i}n = '1', '1'")
for i in range(1, 6):
    for j in range(1, 6):
        exec(f"d_set{i}_field{j}n, d_set{i}_field{j}list = '1', ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜']")
print("\nWelcome to Sandbox!")
print("Here, you can have up to 5 settlements with their own biomes and names!")
print("Your each settlement will have 5 fields. You can plant ASCII characters on fields.")
print("Also, you can run your codes here. Maybe you could make code for your own text-based adventure, and run it here.")
while True:
    print(f"Game #{datetime.now()}")
    print("1 to manage settlements")
    print("2 to manage fields")
    print("3 to get nation save code")
    print("4 to run code")
    print("5 to exit")
    x = int(input())
    try:
        if x == 1:
            for i in range(1, 6):
                exec(f"print('Settlement #{i}: Biome: ' + d_set{i}b + ', Name: ' + d_set{i}n)")
            x = int(input("Settlement to manage: "))
            exec(f"d_set{x}b = input('Its new biome: ')")
            exec(f"d_set{x}n = input('Its new name: ')")
        elif x == 2:
            for i in range(1, 6):
                exec(f"print('Settlement #{i}: Biome: ' + d_set{i}b + ', Name: ' + d_set{i}n)")
            d_set = int(input("Fields' settlement to manage: "))
            for i in range(1, 6):
                exec(f"print('Field #{i} of settlement #{d_set}: Name: ' + d_set{d_set}_field{i}n)")
            d_field = int(input("Its field to manage: "))
            print("1 to change name")
            print("2 to manage content of it")
            x = int(input())
            if x == 1:
                exec(f"d_set{d_set}_field{d_field}n = input('Its new name: ')")
            elif x == 2:
                d_change = ":)"
                while d_change != "exit":
                    for i in range(0, 10):
                        for i in eval(f"d_set{d_set}_field{d_field}list[{i} : {i + 10}]"):
                            print(end = i)
                        print()
                    print("Please enter \"exit\" to the field location part to exit field management.")
                    d_change = input("Change which location of the field? (number 1-100) ")
                    if d_change == "exit": break
                    else: d_change = int(d_change)
                    d_change -= 1
                    print("Recommended emojis: \"⌚⌛⏰⏳⏩⏪⏫⏬◽◾☔☕♈♉♊♋♌♍♎♏♐♑♒♓♿⚓⚽⚾⛄⛅⛎⛔⛪⛲⛳⛴⛵⛺⛽✅✊✋✨❌❎❓❔❕❗➕➖➗➰➿⬛⬜⭐⭕⛔⭐✅⏩♏⌚⬛⬜\"")
                    exec(f"d_set{d_set}_field{d_field}list[d_change] = input('New content as ASCII character: ')")
        elif x == 3:
            print("Please put the code between /* and */ to a file and run it using this program's file running feature*:\n*Use Python to run, not SubProcess or cmd.exe.\n/*")
            for i in range(1, 6):
                print(f"d_set{i}b = \"{eval(f"d_set{i}b")}\"\nd_set{i}n = \"{eval(f"d_set{i}n")}\"")
            for i in range(1, 6):
                for j in range(1, 6):
                    print(f"d_set{i}_field{j}n = \"{eval(f"d_set{i}_field{j}n")}\"\nd_set{i}_field{j}list = {eval(f"d_set{i}_field{j}list")}")
            print("*/\n")
        elif x == 4:
            print("1 to open shell")
            print("2 to execute files")
            x = int(input())
            if x == 1:
                print("1 to open cmd.exe shell")
                print("2 to open Windows PowerShell")
                print("3 to open WMI info shell")
                x = int(input())
                if x == 1:
                    system("cmd")
                elif x == 2:
                    system("powershell")
                elif x == 3:
                    system("wmic")
            elif x == 2:
                print("You will enter the things to run. But, note that data starting with \"d_\" could corrupt the software.")
                x = input("Proceed? (y/n) ")
                if "y" in x.lower():
                    print("Proceeded. Now select executor.")
                    print("1 to execute by cmd.exe")
                    print("2 to execute by Python SubProcess Module")
                    print("3 to execute on Python")
                    x = int(input())
                    if x != 3:
                        print("Now, please write the file to be executed as this format: \"[language] [file]\" e.g. \"python file.txt\"")
                        d_code = input("Prompt: ")
                    if x == 1:
                        system(d_code)
                    elif x == 2:
                        run(d_code.split(" "))
                    elif x == 3:
                        exec(open(input("File to run: "), "r").read())
        elif x == 5:
            quit()
    except Exception as e:
        print("An error occured. Please try again.")
        print(f"Error type: {e}\n")
