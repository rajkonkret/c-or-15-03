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

for i in range(6):  # 0..5
    wyn = random.choice(lista_2)
    print(wyn)
    lista_2.remove(wyn)
# 11:40
print(lista)

for cyfra in lista:
    if cyfra == 2:
        cyfra += 1  # cyfra = cyfra + 1
    print(cyfra)

list_3 = [j for j in range(10) if j % 2 == 0]
print(list_3)

# jupyter

imiona = ["Radek", "Zenek", "Marta"]

for p in imiona:
    print(p)
    print(imiona, ":", p)

# 0 Radek, 1 Zenek itd....
for p in range(len(imiona)):  # range(3) 0..2
    print(p, imiona[p])  # imion[p] - pobranie z listy po indeksie

for p, w in enumerate(imiona):  # p = index, w = imiona[p]
    print(p, w)

ludzie = ["Radek", "Janek", "Asia", "Michał"]
wiek = [47, 67, 32, 34]
jezyk = ['java', 'python', 'c++']
ind = list(range(len(ludzie)))
for p, o in enumerate(ludzie):
    print(p, o)

for p, o in enumerate(ludzie):
    print(p, o, wiek[p])

for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)

for i, o, w, j in zip(ind, ludzie, wiek, jezyk):
    print(i, o, w, j)
# hackerrank
