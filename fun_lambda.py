wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(5))
print(wiek(15))
print(wiek(21))

lista = [1, 2, 7, 8, 10, 55]
tmp = list(map(lambda x: x * 2, lista))
print(
    f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")  # mapuje czyli wykonuje operacje na elementach kolekcji
print(f"{tmp}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # filtruje i zwraca tylko spełniajace warunek
# x > 8
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")
# x > 3 , x < 20
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
