from gaderypoluki import gaderypoluki

with open('gaderypoluki.txt', 'r') as f:
    kod = f.read()

szyfrogram = gaderypoluki(kod)

with open('zakodowany.txt', 'w') as f:
    f.write(szyfrogram)