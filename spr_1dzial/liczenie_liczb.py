num = int(input('podaj liczbe: '))

liczniki = [0 for x in range(10)]

for x in range(len(str(num))):
    a = str(num)[x]
    liczniki[int(a)] += 1


for i in range(10):
    if liczniki[i] > 0:
        print(f'{i} -> {liczniki[i]}')