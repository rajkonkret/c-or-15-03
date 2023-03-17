odejmij = lambda a, b: a - b
print(odejmij(4, 5))

a = 10


def dodaj():
    global a
    a = 4
    b = 10
    print("Wynik=", a + b)


def odejmij():
    b = 7
    print("Wynik=", a - b)


print("Wartosc a z gory", a)
dodaj()
print("Wartosc a z gory", a)
odejmij()
print("Wartosc a z gory", a)
