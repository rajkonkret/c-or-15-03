a = 6
b = 7


def dodaj():
    print(a + b)


def dodaj_2(a, b):
    print(a + b)


def dodaj_3(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


oblicz_vat_2 = lambda cena, vat=23: cena * (100 + vat) / 100

dodaj()
dodaj_2(3, 2)
print(dodaj())
print("Wynik", dodaj_3(6, 5))
print(odejmij(9, 8))
wyn = odejmij(3, 4)
print(wyn + 89)
print(oblicz_vat(1000))
print(odejmij(b=7, a=3))
o = 9
n = 7
print(odejmij(o, n))
print(eval("1/2 + 5 -8 * 9"))

print(oblicz_vat_2(1000, 23))