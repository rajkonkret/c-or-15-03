import random

lista = []
lista_pa = []
for i in range(10):  # 0..9
    if i % 2 == 0:  # % reszta z dzielenia 10/3 = 3 r 1
        print(i)
        lista_pa.append(i)

    print(i)
    lista.append(i)

print(lista)
print(lista_pa)

lista_2 = list(range(1, 50))

for i in range(6):
    wyn = random.choice(lista_2)
    print(wyn)
    lista_2.remove(wyn)
