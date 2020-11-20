import matplotlib.pyplot as plt 
import random as rnd
import math

G = 0
num = 0
Antal = int(input("Skriv antalet punkter här."))

for i in range(-1, Antal):
    X = rnd.uniform(-1, 1)
    Y = rnd.uniform(-1, 1)
    D = math.sqrt(X**2 + Y**2)
    if D < 1:
        plt.plot(X, Y, '*b')
        num += 1
    else:
        plt.plot(X, Y, '*g')


Decimal = num / Antal
Procent = Decimal * 100
G = Decimal * 4


print(Procent)
print(G)


# 

plt.show()
