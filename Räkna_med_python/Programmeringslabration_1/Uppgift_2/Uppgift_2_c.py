tal = float(input("Skriv ditt tal här."))
tal2 = tal       # tal fast tal2 ändras inte utan är alltid det talet användaren skrev in.

for i in range(100):
    if tal%tal2==0:
       print("Burr")

    else:
        print(tal)

    if tal == 100:
        break

    tal += 1