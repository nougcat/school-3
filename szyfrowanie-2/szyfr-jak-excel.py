# idk to jest dziwny szyfr

slowo = str(input('podaj slowo: '))
ilosc_kolumn = int(input('podaj liczbe: '))

while (len(slowo)%ilosc_kolumn != 0): slowo += 'x'  # dopełniamy tekst do póki nie jest wielokrotnością ilości kolumn

wynik = ''

# ogólnie to ta pętla wypisuje co któryś element stringa, a potem co któryś +1
# dla hasła DUPA i klucza 2
# D P
# U A
# == DPUA
for i in range(ilosc_kolumn):
    for x in range(int(len(slowo)/ilosc_kolumn)):
        wynik += slowo[i + x * ilosc_kolumn]

print(wynik)