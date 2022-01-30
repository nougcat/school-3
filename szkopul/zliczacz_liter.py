# Zlicza wszystkie znaki

# funkcja liczy znaki 
def policz_znaki(linijka):
    odp = [0 for x in range(26)]
    odp_wielkie = [0 for x in range(26)]
    line = linijka.split()
    for slowo in line:
        for x in range(len(slowo)):
            val = ord(slowo[x])
            if val >= ord('a'):
                odp[val - ord('a')] += 1
            else:
                odp_wielkie[val - ord('A')] += 1
    return odp, odp_wielkie

# ile wierszy
num = int(input(''))

wynik_male, wynik_wielkie = [], []

# wczytaj wiersze i wywołaj funkcje
for x in range(num):
    linijka = input('')
    wynik = policz_znaki(linijka)
    wynik_male += wynik[0]
    wynik_wielkie += wynik[1]

# wypisujemy małe litery
for i in range(26):
    tmp = 0
    for x in range(num):
        tmp += int(wynik_male[i + (x * 26)])
    if tmp != 0:
        print(chr(ord('a') + i), tmp)

# wypisujemy duże ltery
for i in range(26):
    tmp = 0
    for x in range(num):
        tmp += int(wynik_wielkie[i + (x * 26)])
    if tmp != 0:
        print(chr(ord('A') + i), tmp)