pierwszy_wyraz = input('podaj pierwszy wyraz: ')
drugi_wyraz = input('podaj drugi wyraz: ')

podciag = ''

for x in pierwszy_wyraz:
    for i in drugi_wyraz:
        if x == i:
            print(x, end='')
            podciag += x
            break

print('\n', len(podciag))