from random import randint, seed 


wymiary=6
pole = []
for x in range(wymiary):
    pole += [[randint(0,9) for x in range(wymiary)]]

print(pole)