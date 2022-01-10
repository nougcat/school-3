# sito eratostenesa

num = int(input('podaj liczbe: '))
x = 2
tab = [False] + [True for i in range(x, num+1)]

while x * x <= num:
    for i in range(0, num-x, x): 
        tab[x * x - 2 + i] = False 
    
        x += 1

print(tab)
