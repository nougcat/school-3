tekst = str(input('podaj tekst do zaszyfrowania: '))
klucz = str(input('podaj klucz: '))
szyfrogram = ''

iteracja_klucza=0
for x in range(len(tekst)):     # x to kolejny element w linii
    if ord(tekst[x]) == 32:
        szyfrogram += ' '
        continue                                                                                               # (nr. litery alfabetu + nr litery alfabatu) % 26 + 97 {aby działało ASCII}
    szyfrogram += chr((ord(tekst[x].lower())-97 + ord(klucz[iteracja_klucza%len(klucz)].lower())-97)%26 + 97)  # (ASCII elementu - 76 + (ASCII klucza - 97)) % 26 + 97
    iteracja_klucza +=1

print(szyfrogram)