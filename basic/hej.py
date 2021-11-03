imie = str(input("podaj imie: "))
wiek = int(input("podaj wiek: "))

import datetime
year = datetime.datetime.now().year

if imie[-1] == "a":
    print("jesteś babom")
    zaimek = "aś"
else:
    print("jesteś chop")
    zaimek = "eś"

print(f"Część {imie} urodził{zaimek} się w {year - wiek} roku")