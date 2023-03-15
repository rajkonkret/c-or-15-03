tuple_1 = "Tomek", "Michał", "Asia", "Kasia"
tuple_2 = "RADEK",
tuple_3 = 43, 55, 22.43, 11, 200

print(tuple_1)
# wyswietlic tuple i ich typ
print(type(tuple_1))
print(tuple_2)
# wyswietlic tuple i ich typ
print(type(tuple_2))
print(tuple_3)
# wyswietlic tuple i ich typ
print(type(tuple_3))
print(tuple_1.count("Tomek"))  # liczba wystapien
print(tuple_1.index("Asia"))
name = tuple_1[2]
print(name)

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
tuple_1 = "Tomek", "Michał", "Asia", "Kasia"

print(len(tuple_1))
imie_1, *imie_2, imie_3 = tuple_1  # rozpakowanie tupli

print(imie_1)
print(type(imie_1))
print(imie_2)
print(imie_3)

lista = list(tuple_1)
print(lista)
print(tuple_1)
