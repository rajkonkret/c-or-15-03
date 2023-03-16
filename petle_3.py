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

lista = []
while True:
    wejscie = input("Wprowadz liczbe")
    if not wejscie.isnumeric():
        break
    lista.append(int(wejscie))

print(lista)
# 13:30
