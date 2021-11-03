def gaderypoluki(napis):
    wynik = ''
    for i in range(len(napis)):
        match napis[i]:
            case 'g': wynik += 'a'
            case 'a': wynik += 'g'
            case 'd': wynik += 'e'
            case 'e': wynik += 'd'
            case 'r': wynik += 'y'
            case 'y': wynik += 'r'
            case 'p': wynik += 'o'
            case 'o': wynik += 'p'
            case 'l': wynik += 'u'
            case 'u': wynik += 'l'
            case 'k': wynik += 'i'
            case 'i': wynik += 'k'
            case _: wynik += napis[i]
    return wynik

if '__main__' == __name__:
    napis = str(input('podaj szyfr: '))
    print(gaderypoluki(napis))