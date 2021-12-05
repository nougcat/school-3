slowo = str(input('podaj slowo: '))
ilosc_kolumn = int(input('podaj liczbe: '))

a = ilosc_kolumn - len(slowo)%ilosc_kolumn
if a == ilosc_kolumn: a = 0
for x in range(a): slowo += 'x'


print(slowo)
wynik = ''

for i in range(ilosc_kolumn):
    for x in range(int(len(slowo)/ilosc_kolumn)):
        print(x * ilosc_kolumn)
        wynik += slowo[i + x * ilosc_kolumn]

print(wynik)