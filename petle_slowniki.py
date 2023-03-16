dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictionary)
for k in dictionary:
    print(k)

for v in dictionary.values():
    print(v)

for k in dictionary.keys():
    print(k)

for k, v in dictionary.items():
    print(k, "=>", v)
# stworzyc dowolny slownik i wypisac klucz, wartosci lub itemy
for i in range(1, 10, 2):  # (start, koniec, krok)
    print(i)

for i in range(-10, 1, 1):
    print(i)

for i in range(10, 1, -1):
    print(i)
