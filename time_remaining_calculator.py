# Imagine you're downloading a game, and it says "# hours ## minutes remaining". This is an app to see when it'll be downloaded.
from datetime import datetime as d
while True:
    print(d.now())
    x = int(input("Hours remaining: "))
    y = int(input("Minutes remaining: "))
    yr = d.now().year
    mo = d.now().month
    da = d.now().day
    h = d.now().hour
    m = d.now().minute
    h += x
    m += y
    while m >= 60:
        m -= 60
        h += 1
    while h >= 60:
        h -= 60
        da += 1
    while da >= 31:
        da -= 31
        mo += 1
    while mo >= 12:
        mo -= 12
        yr += 1
    print(f"{yr}-{mo}-{da} {h}:{m}:{d.now().day}.{d.now().microsecond}")
