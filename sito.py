# sito eratostenesa

num = int(input('podaj liczbe: '))
x = 2
tab = [False] + [True for i in range(x, num+1)]

while x * x < num:
    for i in range(x, i * x, 2):
        tab[i] = False

        x += 2


for x in range(len(tab)):
    print(x, tab[x])