# lista = []
# print(lista)
# print(type(lista))
# lista.append("Radek")
# lista.append("MAciek")
# lista.append("Tomek")
# lista.append("Daria")
#
# print(lista)
# lista.insert(1, "Gosia")  # wstawienie pomiedzy index 0 i 1
# print(lista)
# lista[1] = "Krzysiek"  # wstawienie za element na indexie 1
# print(lista)
# lista.append("Tomek")
# print(lista)
# lista.remove("Tomek")
# print(lista)
#
# lista.reverse()
# print(lista)
# lista_2 = lista.copy()
# print(lista_2)
# lista_2.clear()
# print(lista)
# print(lista_2)
#
# print(lista.pop(0))  # pobranie po indeksie (de facto usuwa z listy ten element)
# print(lista)
# imie = lista[1]  # odczytanie elementu na indeksie 1
# print(imie)
# print(lista)
# komentarz wielu linii ctrl /
"""
dfdgsfgsd
fsdfsdf
fdsdfsd
"""

liczby = [54, 999, 34, 22, 12.54, 687]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby_2 = liczby.copy()
liczby.clear()
print(liczby_2)
print(liczby)
liczby_2[0] = 6666
print(liczby_2)

print(liczby_2[0:3])
print(liczby_2[:3])
print(liczby_2[2:])
print(liczby_2[:-1])
print(liczby_2[:-2])
print(liczby_2)
liczby_2.remove(54)
print(liczby_2)
print(len(liczby_2))  # długosc kolekcji, indexy 0..4
print(liczby_2.pop(0))
print(liczby_2)

krotka = tuple(liczby_2)
print(krotka)
# 13:32
