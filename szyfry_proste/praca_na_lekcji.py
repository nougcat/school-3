
with open('dane.txt', 'r') as f:
    dane = f.read()


for x in range(62):
    imie = dane.split("\n")[x]
    if len(imie) == 4:
        print(imie)

        with open('imiona.txt','a') as f:
            f.write(f'{imie}\n')