from random import randint, seed
from webbrowser import Konqueror 

def ruch(pole[], koordynaty):
    if koordynaty[0] == pole[-1][koordynaty[1]]:
        a = 0
    else:
        a = pole[koordynaty+1]
    if koordynaty[1] == pole[koordynaty[1]][-1]:
        b = 0
    else:
        b = pole[koordynaty]

wymiary=6
pole = []
for x in range(wymiary):
    pole += [[randint(0,9) for x in range(wymiary)]]

print(pole)

koordynaty = [0,0]

ruch(pole, koordynaty)