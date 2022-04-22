
nazwisko = input('podaj nazwisko: ')
pesel = int(input('podaj pesel: '))
srednia = float(input('podaj srednia: '))
dyslekcja = input('dyslekcja?: ')

text ={
    'nazwisko': nazwisko,
    'pesel': pesel,
    'srednia': srednia,
    'dyslekcja': dyslekcja
}

print(text)

with open('osoba.txt', 'w') as f:
    f.write(text)