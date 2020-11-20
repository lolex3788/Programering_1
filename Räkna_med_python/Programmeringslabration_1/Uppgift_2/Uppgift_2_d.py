tal1 = float(input("Skriv ditt tal här."))
tal2 = float(input("Skriv ditt andra tal här."))

i = 0 
num = 0

for i in range(100):
    if num%tal1==0:
        print("Burr")
    if num%tal2==0:
        print("Birr")
    
    
    num += 1