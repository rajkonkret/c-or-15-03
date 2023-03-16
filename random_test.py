import random

print(random.randint(1, 6))  # losuje od 1 do 6
print(random.random() * 10)  # losuje od 0 do 1 i * 10 daje nam od 0 do 9.99 float
print(random.randrange(6))  # losuje od 0..5
print(random.randrange(1, 6))  # losuje od 1..5

lista = [5, 7, 9, 34, 55, 0]
print(random.choice(lista))
lista_2 = list(range(1, 50))
print(lista_2)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
