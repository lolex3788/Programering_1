import random as random

femmor = 0

for i in range(100001):
    tärning = random.randint(1, 6)
    if tärning == 5:
        femmor += 1


print(f"{femmor} antal femmor var kastade")
print(f"antal gånger tärningen var kastad : {i}")