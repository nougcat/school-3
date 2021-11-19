from losowe_liczby import losuj

tablica = losuj(10)
print(tablica)

for x in range(len(tablica)-1):
    for j in range(len(tablica)-1):
        if tablica[j] > tablica[j+1]:
            tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    
for x in tablica:
    print(x, end=' ')