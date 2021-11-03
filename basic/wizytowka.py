imie = str(input('podaj imie palo:'))
nazwisko = str(input('nazwisko:'))
telefon = int(input('numer 😏:'))


with open('wizytowka.txt', 'w') as f:
    f.write(f'imie: {imie}\n')
    f.write(f'nazwisko: {nazwisko}\n')
    f.write(f'nr. telefonu: {telefon}\n')