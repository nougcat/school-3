
with open('popr.txt', 'r') as f:
    tab = []
    for x in f:
        tab.append(x.split())


suma = 0
ile_5 = 0

suma_wiersz = []
for x in tab:
    for i in x:
        suma += int(i)

        if int(i) == 5: ile_5 +=1
    
    suma_wiersz.append(suma)
    suma = 0

suma_calkowita = 0

naj_wiersz = 0

for i, x in enumerate(suma_wiersz):
    suma_calkowita += x
    
    if int(x) > suma_wiersz[naj_wiersz]:
        naj_wiersz = i




print(f'suma = {suma_calkowita}')
print(f'ile 5 = {ile_5}')
print(f'największa suma w wierszu = {suma_wiersz[naj_wiersz]} dla wiersza nr {naj_wiersz}')