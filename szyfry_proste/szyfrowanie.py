def zaszyfruj():
    text = str(input("Dej teks:"))
    key = int(input("Dej klucz:"))
    wynik = ""
    for i in range(len(text)):
        znak = text[i]
        if znak.upper()>="A" and znak.upper()<="Z":
            kod=chr(ord(znak)+key)
            if znak<='Z' and kod>'Z' or znak>='z' and kod>'z': kod = kod-26
            wynik += kod
        else:
            wynik += znak
    return wynik

if '__main__' == __name__:
    print("Szyfrogram:", zaszyfruj())