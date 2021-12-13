tekst = input('podaj tekst: ')

for x in range(1, len(tekst), 2):
    print(f'{tekst[x]}{tekst[x-1]}', end='')

if len(tekst) - 2 == x:
    print(tekst[-1])