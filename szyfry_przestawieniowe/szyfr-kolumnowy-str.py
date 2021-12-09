def przestaw(tekst: str, klucz: str) -> str:
    iteracja_klucza=0
    szyfrogram = ''

    # ogólnie to tak funkcja zmienia tekst o klucz
    for x in range(len(tekst)):     # x to kolejny element w linii
        if ord(tekst[x]) == 32:
            szyfrogram += ' '
            continue                                                                                               # (nr. litery alfabetu + nr litery alfabatu) % 26 + 97 {aby działało ASCII}
        szyfrogram += chr((ord(tekst[x].lower())-97 + ord(klucz[iteracja_klucza%len(klucz)].lower())-97)%26 + 97)  # (ASCII elementu - 76 + (ASCII klucza - 97)) % 26 + 97
        iteracja_klucza +=1
    return szyfrogram


tekst = str(input('podaj tekst do zaszyfrowania: '))
klucz = str(input('podaj klucz: '))

a = przestaw(tekst, klucz)


print(a)