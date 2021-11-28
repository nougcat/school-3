from sorted_random import losuj

# tworzymy tablice
a = int(input('długość tablicy: '))
tablica = losuj(a)

# wyświetlamy tablice
print(tablica)

# prosimy o ktorą liczbę wyszukać
szukana = int(input('szukana liczba: '))

# zaczynamy sprawdzanie od połowy tablicy
x = int(a/2)

while tablica[x]!=szukana: # dopóki nie znajdziemy liczby:
    if tablica[x-1] < szukana and tablica[x] > szukana or x==0 or tablica[x] == tablica[-1]: # nie ma takiej liczby w zbiorze
        print('nie ma takiej liczby w zbiorze')
        exit()
    elif tablica[x] > szukana:      # jeśli x jest większy
        x = int(x/2)
    elif x < int(a/2):              # jeśli jest mniejsza
        x += int(x/2)
    else:                           # jeśli
        x += int((a-x)/2)
    

print(f'szukana liczba jest na {x+1} pozycji')