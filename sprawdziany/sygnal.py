tablica = []
wszystkie_linijki = []


with open('sygnaly.txt', 'r') as f:
    for x in range(1000):
        slowo = f.readline()
        if (x+1)%40 == 0:
            tablica.append(slowo)
        wszystkie_linijki.append(slowo)
        


for x in range(len(tablica)):
    slowo = tablica[x]
    print(slowo[9],end='')

print()

najwieksza_liczba=0

for x in range(len(wszystkie_linijki)):
    a = wszystkie_linijki[x]
    if len(a) > najwieksza_liczba:
        najdluzsza_linijka=x
        najwieksza_liczba = len(a)

with open('odp.txt', 'a') as f:
    f.write(f'{wszystkie_linijki[najdluzsza_linijka]}')