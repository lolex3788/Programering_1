pengar = int(input("Hur mycket pengar har du?"))

tusenlappar = 0
femhundralappar = 0
tvåhundralappar = 0
hundralappar = 0
femtiolappar = 0
tjugolappar = 0
tiokronor = 0
femkronor = 0
tvåkronor = 0
enkronor = 0

while pengar >= 1000:
    tusenlappar += 1
    pengar -= 1000

while pengar >= 500:
    tusenlappar += 1
    pengar -= 500

while pengar >= 200:
    tvåhundralappar += 1
    pengar -= 200

while pengar >= 100:
    hundralappar += 1
    pengar -= 100

while pengar >= 50:
    femtiolappar += 1
    pengar -= 50

while pengar >= 20:
    tjugolappar += 1
    pengar -= 20

while pengar >= 10:
    tiokronor += 1
    pengar -= 10

while pengar >= 5:
    femkronor += 1
    pengar -= 5

while pengar >= 2:
    tvåkronor += 1
    pengar -= 2

while pengar >= 1:
    enkronor += 1
    pengar -= 1


print(tusenlappar, femhundralappar, tvåhundralappar, hundralappar, femtiolappar, tjugolappar, tiokronor, femkronor, tvåkronor, enkronor)
print(f"{pengar} pengar kvar")