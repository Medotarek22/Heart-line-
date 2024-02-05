import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
setup(width=380, height=400)
speed(0)
bgcolor("black")

for i in range(10000):
    goto(hearta(i) * 10, heartb(i) * 10)
    for j in range(5):
        color("#f73487")
        goto(0, 0)

done()

