from losowe_liczby import losuj

a = int(input('długość tablicy: '))
tablica = losuj(a)

print(tablica)

szukana = int(input('szukana liczba: '))

x = int(a/2)

while tablica[x]!=szukana:
    if tablica[x-1] < szukana and tablica[x] > szukana or x==0 or tablica[x] == tablica[-1j]:
        print('nie ma takiej liczby w zbiorze')
        exit()
    elif tablica[x] > szukana:
        x = int(x/2)
    elif x < int(a/2):
        x += int(x/2)
    else:
        x += int((a-x)/2)
    

print(f'szukana liczba jest na {x+1} pozycji')