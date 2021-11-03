def test_liter():
    ## otwieramy i wczytujemy pliki
    import codecs
    with codecs.open('szyfrogram.txt', 'r', encoding='utf-8') as f:
        szyforgram = f.read()

    ## tworzymy tablice i wypełniamy ją zerami
    alfabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'
    liczniki = [0 for x in range(len(alfabet))]

    ## uzupełniamy tablice
    for i in range(len(szyforgram)):
        znak = szyforgram[i].upper()
        if alfabet.find(znak) >= 0:
            liczniki[alfabet.find(znak)] +=1

    ## wypisujemy jak dużo razy pojawił się znak
    f = open('dane.txt','a')
    for i in range(len(liczniki)):
        if liczniki[i] > 0:
            f.write(f'{alfabet[i]} : {liczniki[i]} \n')

    f.close()
    
    ## CSV
    with open('litery.csv', 'w') as f:
        for i in liczniki:
            f.write(f'{liczniki[i]}\n')

if __name__=='__main__':
    test_liter()