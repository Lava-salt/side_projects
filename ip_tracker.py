from datetime import datetime
from time import sleep
from subprocess import Popen, PIPE
def get_time():
    return datetime.now()
print("I.P. Address Tracker")
x = input("I.P. Address to Track: ")
p = Popen(f"ping {x}", stdout = PIPE)
while True:
    if p.poll():
        print(f"{get_time()} - I.P. Address {x} Active")
    else:
        print(f"{get_time()} - I.P. Address {x} Passive")
    sleep(60)
# Please note that this isn't for hacking processes, this is just made for fun.
