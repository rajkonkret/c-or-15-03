licznik = 0

while True:
    licznik += 1
    print("Komunikat")
    if licznik == 10:
        break
licznik = 0
while licznik < 10:
    print("komunikat")
    licznik += 1

# lista = []
# while True:
#     wejscie = input("Wprowadz liczbe")
#     if not wejscie.isnumeric():
#         break
#     lista.append(int(wejscie))

# print(lista)
# 13:30

slownik = {"pan": "Tomek", "pani": "Ania"}
print(slownik)

# print({value: key for key, value in slownik.items()})

# print(slownik['pan'][1])
slownik_2 = {}
for a, b in slownik.items():  # zamiana klucza z wartoscią w slowniku
    slownik_2[b] = a

print(slownik_2)
