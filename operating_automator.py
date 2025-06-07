from os import getcwd as _getcwd
from os import path as _path
from os import listdir as _dir
from os import name as _name
from os import chdir as _chdir
from os import remove as _remove
from os import rmdir as _rmdir
from os import rename as _rename
from os import system as _system
from sys import platform as _platform
from datetime import datetime as _dt
from subprocess import Popen as _popen
from subprocess import PIPE as _pipe
from subprocess import call as _call
from webbrowser import open as _open
from time import sleep as _sleep
_cond, _do, _one, _dCond, _dDo = [], [], [], [], []
print("Welcome to Operating Automator!")
print("Operating Automator is used for doing computer tasks automatically if a condition's true.")
print("You can add multiple if-then statements to automate tasks easily, like Kodu Game Lab.")
print("This is a side project of @Lava-salt (GitHub) that's like Power Automate.")
print("NOTE: In this process, DO NOT name or use any variables with an underscore (\"_\") as the first letter.")
print("You'll notice \"(as Python data)\" sometimes. It means that if you're going to add a string,\nwrite it between quotation, because it'll understand it as evaluated Python data.")
while True:
    print("1 - Add new conditional branch")
    print("2 - Delete existing conditional branch")
    print("3 - List all conditional branches")
    print("4 - Automate all conditions")
    _x = int(input())
    if _x == 1:
        print("First, add the condition:")
        print("1 - Check current working directory")
        print("2 - Check chosen directory content")
        print("3 - Check current working directory content")
        print("4 - Check operating system name")
        print("5 - Check system platform")
        print("6 - Check directory existance")
        print("7 - Check file size")
        print("8 - Check I.P. address activity (active / passive)")
        print("9 - Check Python variable data")
        print("10 - Check file content")
        print("11 - Python boolean is true")
        print("12 - Always")
        _x = int(input())
        if _x == 1:
            _x = input("Do task if current working directory is (as Python data): ")
            _cond.append(f"_cwd == {_x}")
            _dCond.append(f"If current working directory is {_x}:")
        elif _x == 2:
            _x = input("Directory (as Python data): ")
            _y = input("Do task if directory has (as Python data): ")
            _cond.append(f"_dir({_x}) == {_y}")
            _dCond.append(f"If directory \"{_x}\" is {_y}:")
        elif _x == 3:
            _x = input("Do task if current working directory has (as Python data): ")
            _cond.append(f"_dir({_cwd}) == {_x}")
            _dCond.append(f"If current working directory is {_x}:")
        elif _x == 4:
            _x = input("Do task if operating system name is (as Python data): ")
            _cond.append(f"_name == {_x}")
            _dCond.append(f"If operating system name is {_x}:")
        elif _x == 5:
            _x = input("Do task if system platform is (as Python data): ")
            _cond.append(f"_platform == {_x}")
            _dCond.append(f"If system platform is {_x}:")
        elif _x == 6:
            _x = input("Do task if this directory exists (as Python data): ")
            _cond.append(f"_path.exists({_x})")
            _dCond.append(f"If directory {_x} exists: ")
        elif _x == 7:
            _x = input("Check this directory (as Python data): ")
            _y = float(input("Do task if directory size as bytes is: "))
            _cond.append(f"_path.getsize({_x}) == {_y}")
            _dCond.append(f"If file in directory {_x} is {_y} bytes:")
        elif _x == 8:
            _x = input("Do task if this I.P. address is active (as Python data): ")
            _cond.append(f"_popen(f'ping {_x}', stdout = _pipe).poll()")
            _dCond.append(f"If I.P. address {_x} is active:")
        elif _x == 9:
            _x = input("Check Python variable: ")
            _y = input("Do task if variable is (as Python data): ")
            _cond.append(f"{_x} == {_y}")
            _dCond.append(f"If Python variable {_x} is {_y}:")
        elif _x == 10:
            _x = input("Check content of file (as Python data): ")
            _y = input("Do task if file's content is (as Python data): ")
            _cond.append(f"open({_x}, \"r\").read() == {_y}")
            _dCond.append(f"If file {_x}'s content is {_y}:")
        elif _x == 11:
            _x = input("Do task if this Python boolean is true (as Python data): ")
            _cond.append(_x)
            _dCond.append(f"If Python boolean {_x} is true:")
        elif _x == 12:
            _cond.append(f"True")
            _dCond.append("Always:")
        print("Will the task be done if the condition is true or not?")
        print("For example if you chose \"Check file size\", choosing \"not\" here will do the task if given file's size's not equal to given integer.")
        _x = input("True or not? (t/n) ").lower()
        if _x == "n":
            _cond[-1] = "if not(" + _cond[-1] + "):"
            _dCond[-1] = "Do task if this is false: " + _dCond[-1]
        else:
            _cond[-1] = "if " + _cond[-1] + ":"
            _dCond[-1] = "Do task if this is true: " + _dCond[-1]
        _x = input("Will the task be done a single time or always if true? (s/a) ").lower()
        if _x == "s":
            _one.append("Do Only a Single Time")
        else:
            _one.append("Do Always if True")
        print("Lastly, add the task to do if condition is true:")
        print("1 - Change current working directory")
        print("2 - Delete file")
        print("3 - Delete directory")
        print("4 - Rename file")
        print("5 - Print file content")
        print("6 - Add text to a file")
        print("7 - Replace file content")
        print("8 - Output text")
        print("9 - Open file")
        print("10 - Open website")
        print("11 - Run Python command")
        print("12 - Print Pyhton data")
        print("13 - Run shell command")
        _x = int(input())
        if _x == 1:
            _x = input("Change directory to (Python \"os.chdir()\" method, as Python data): ")
            _do.append(f"_chdir({_x})")
            _dDo.append(f"Change directory to {_x}")
        elif _x == 2:
            _x = input("Remove file in directory (as Python data): ")
            _y = input("Remove file (as Python data): ")
            _do.append(f"_remove(_path.join({_x}, {_y}))")
            _dDo.append(f"Remove file {_y} in {_x}")
        elif _x == 3:
            _x = input("Remove directory in parent directory (as Python data): ")
            _y = input("Remove directory (as Python data): ")
            _do.append(f"_rmdir(_path.join({_x}, {_y}))")
            _dDo.append(f"Remove directory {_y} in parent directory {_x}")
        elif _x == 4:
            _x = input("Directory of file to rename (as Pyhton data): ")
            _y = input("Its new name (as Python data): ")
            _do.append(f"_rename({_x}, {_y})")
            _dDo.append(f"Rename {_x}, {_y}")
        elif _x == 5:
            _x = input("Print content of file (as Python data): ")
            _do.append(f"open({_x}, \"r\").read()")
            _dDo.append(f"Print file {_x}'s content")
        elif _x == 6:
            _x = input("File to add text (as Python data): ")
            _y = input("Text to add (as Python data): ")
            _do.append(f"open({_x}, \"a\").write({_y})")
            _dDo.append(f"Add text {_y} to file {_x}")
        elif _x == 7:
            _x = input("File to replace its text (as Python data): ")
            _y = input("Text to replace with (as Python data): ")
            _do.append(f"open({_x}, \"w\").write({_y})")
            _dDo.append(f"Replace file {_x}'s text with {_y}")
        elif _x == 8:
            _x = input(f"Text to output (as Python data): ")
            _do.append(f"print({_x})")
            _dDo.append(f"Output text {_x}")
        elif _x == 9:
            _x = input("File to open (Python \"subprocess.call()\" method, as Python data): ")
            _do.append(f"_call({_x})")
            _dDo.append(f"Open file {_x}")
        elif _x == 10:
            _x = input("URL to open (as Python data): ")
            _do.append(f"_open({_x})")
            _dDo.append(f"Open URL {_x}")
        elif _x == 11:
            _x = input("Python command to run (as Python data): ")
            _do.append(_x)
            _dDo.append(f"Run Python command {_x}")
        elif _x == 12:
            _x = input(f"Python data to print (as Python data): ")
            _do.append(f"print({_x})")
            _dDo.append(f"Print Python data {_x}")
        elif _x == 13:
            _x = input(f"Run shell command (as Python data): ")
            _do.append(f"_system({_x})")
            _dDo.append(f"Run shell command {_x}")
    elif _x == 2:
        for i in range(len(_dCond)):
            print(f"{i + 1} - {_one[i]}: {_dCond[i]} {_dDo[i]}")
        _x = int(input("Conditional branch to delete: ")) - 1
        del _one[x], _cond[_x], _dCond[_x], _do[_x], _dDo[_x]
    elif _x == 3:
        for i in range(len(_dCond)):
            print(f"{i + 1} - {_one[i]} {_dCond[i]} {_dDo}")
        _system("pause")
    elif _x == 4:
        _time = float(input("How much seconds will conditional branches be automated? "))
        _interval = float(input("Interval between checking conditions: "))
        _rep = int(_time / _interval)
        for i in range(_rep):
            _system("cls")
            for i in range(len(_dCond)):
                if _one[i] == "Do Only a Single Time":
                    exec(_cond[i] + _do[i])
                    _one[i] = "Already Done"
                elif _one[i] == "Do Always if True":
                    exec(_cond[i] + _do[i])
            print(f"Time: {_dt.now()}")
            _sleep(_interval)
    _system("cls")
