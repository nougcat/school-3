# wszystkie dane
dane = input('')
k, w, m = dane.split()

wynik = (int(w)-int(k))/int(m)

if wynik == int(wynik):
    print(int(wynik))
else:
    print(int(wynik)+1)