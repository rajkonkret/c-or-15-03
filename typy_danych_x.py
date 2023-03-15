# rajkonkret660@gmail.com

# PEP8
wiek = 47  # int
rok = 2023
temp = 36.6  # float - zmiennoprzecinkowy

# wypisac zawartos tych zmiennych
print(wiek)
print(rok)
print(type(rok), type(wiek))

print(temp)

print(wiek * rok)
print(wiek - rok)
print(wiek + rok)
print(4 / 2)
print(type(4 / 2))  # zmiana na float
print(wiek // rok)
print(type(wiek // rok))  # czesc całkowita dzielenia - int
print(wiek ** rok)  # potegowanie
print(54 - (5 * 43) + (4 / 2 + 4) / 2)
# numPy, mat

print("\tSprawdzam zmienna temp {} {}\n".format(wiek, temp))
print(f"\tSprawdzam zmienna temp {wiek} {temp}")

print(f"""
    zmienna {temp}
    zmienna {wiek}
""")

imie = "Radek Radek"
print(imie)
imie.lower()  # małe litery
print(imie.lower())
imie_2 = imie.upper()  # duże litery
print(imie_2)
print(imie.capitalize())  # pierwsza litera zdania duza
print(imie.count("a"))

print("False/True")
czy_znasz_Python = False
print(czy_znasz_Python)
print(int(czy_znasz_Python))  # 1 - True, 0 - False
print(type(czy_znasz_Python))