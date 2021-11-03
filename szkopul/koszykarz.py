k = float(input('podaj k:'))
w = float(input('podaj w:'))
m = float(input('podaj m:'))

wynik = (w-k)/m

if wynik == int(wynik):
    print(int(wynik))
else:
    print(int(wynik)+1)