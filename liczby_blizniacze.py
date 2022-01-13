from sito_eratostenesa import sito

num = int(input('podaj liczbe: '))

tab = sito(num)

for x in range(len(tab)):
    if tab[x] and tab[x+2]:
        print(x, x+2)