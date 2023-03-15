dict = {}
set_empty = set()  # pusty set
print(dict)
print(type(dict))
print(set_empty)
print(type(set_empty))
dict['imie'] = "Radek"
print(dict)
dict['wiek'] = 39
print(dict)
dict['imie'] = "Stefan"
print(dict)
dict['wiek'] = 28
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
lista = [44, 55, 66, 88]
dict['liczby'] = lista
print(dict)
dict_2 = {'imie': ['Radek', 'Tomek']}
print(dict_2)

# dict_3 = {'imie': 'name', 'kot': 'cat', 'okno': 'window', 'woda': 'water'}
# dict_3.update({"pies": "dog"})
# print("MAmy w słowniku ", dict_3.keys())
# key = input("Podaj wyraz")  # input zawsze daje str
# print(dict_3[key.lower().replace(" ", "")])
#
# print(dict_3)

a = float(input("podaj liczbe a"))  # rzutowanie str na float
b = float(input("podaj liczbe b"))
print(a + b)
g = "5"
print(int(g) + 6)