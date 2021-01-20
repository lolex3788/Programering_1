tal1 = int(input("Vilken gångertabell vill du öva på?"))


lista = []
lista2 = []


for i in range(1,11):
    tal2 = int(input(f"Vad är {i} x {tal1}?"))
    lista2.append(tal2)


for x in range(1,11):
    svar = x * tal1
    lista.append(svar)


if lista == lista2:
    print("Alla är rätt")
else:
    print("Du har fel")
    print(f"Här är svaret = {lista}")


print(" \n ")
print(lista)
print(lista2)