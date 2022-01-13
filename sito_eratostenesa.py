# sito eratostenesa

def sito(num):
    x = 2
    tab = [False, False] + [True for i in range(x, num+1)]

    while x * x <= num:
        if tab[x]:
            for i in range(x*x, num+1, x):
                tab[i] = False
            x+=1
        else: x+=1
    
    return tab

if __name__ == '__main__':
    num = int(input('podaj liczbe: '))

    tab = sito(num)

    for x in range(len(tab)):
        print(x, tab[x])