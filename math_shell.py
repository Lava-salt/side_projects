# Here's a code terminal -- to display math equations!
from os import system
system("cls")
from math import *
from statistics import *
from random import *
try:
    from numpy import *
    from scipy import *
    from matplotlib import *
except ModuleNotFoundError:
    system("pip install numpy")
    system("cls")
    system("pip install scipy")
    system("cls")
    system("pip install matplotlib")
    system("cls")
    from numpy import *
    from scipy import *
    from matplotlib import *
system("cls")
print("Functional Mathematics Shell")
print("Type \"help\" for help.")
while True:
    cmd = input(">>> ")
    cmd = cmd.replace("×", "*")
    cmd = cmd.replace("÷", "/")
    cmd = cmd.replace("^", "**")
    cmd = cmd.replace("&&", "and")
    cmd = cmd.replace("||", "or")
    cmd = cmd.replace("!", "not")
    cmd = cmd.replace("~", "not")
    if cmd.lower() == "help":
        print("Help on functional mathematics shell:")
        print("\"f(x) = x\" = Define function \"f(x)\" as \"return x\"")
        print("\"x = 1\" = Define variable \"x\" as \"1\"")
        print("+ = Addition")
        print("- = Subtraction")
        print("*, × = Multiplication")
        print("/, ÷ = Division")
        print("** = Exponentiation")
        print("// = Floor division")
        print("% = Modulo")
        print("Boolean operators: ==, !=, <, >, <=, >=, &&, ||, !, ~")
    elif "=" in cmd:
        try:
            exec(f"""
def {cmd.split('=')[0].strip()}:
    return {"=".join(cmd.split('=')[1:]).strip()}
""")
            print(f"Defined function \"{cmd.split('=')[0].strip()}\" as \"{"=".join(cmd.split('=')[1:]).strip()}\"")
        except Exception:
            try:
                exec(f"{cmd.split('=')[0].strip()} = {"=".join(cmd.split('=')[1:]).strip()}")
                print(f"Defined variable {cmd.split('=')[0].strip()} as \"{eval("=".join(cmd.split('=')[1:]).strip())}\"")
            except Exception:
                try:
                    print(eval(cmd))
                except Exception as e:
                    print(e)
    else:
        try:
            print(eval(cmd))
        except Exception as e:
            print(e)
