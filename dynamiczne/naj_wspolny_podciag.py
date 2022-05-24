pierwszy_wyraz = input('podaj pierwszy wyraz: ')
drugi_wyraz = input('podaj drugi wyraz: ')

podciag = ''

zaczynamy_od = 0
for x in pierwszy_wyraz:
    for i in range(zaczynamy_od, len(drugi_wyraz)):
        if x == drugi_wyraz[i]:
            podciag += x
            zaczynamy_od = i + 1
            break
        
print(f'{podciag} - {len(podciag)}')