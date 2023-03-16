# fh = open('test.log', 'a')
# fh.write("Test")
# fh.close()
#
# with open('test.log', encoding='utf-8') as fh:
#     for l in fh:
#         print(l.strip())

lista = [1, 2, 3, 4]
print(type(lista))
tmp = str(lista)
print(type(tmp))

with open('dane.txt', 'w') as file_h:
    file_h.write(tmp)

lista_2 = []
with open('dane.txt', 'r') as fh:
    for l in fh:
        lista_2.append(l)

print(lista_2)

for i in lista_2:
    print(i)

tmp_l = lista_2[0].replace("[", "")
tmp_l = tmp_l.replace("]", "")
tmp_l = tmp_l.split(",")
print(tmp_l)
lista_int = []
for i in tmp_l:
    lista_int.append(int(i.strip()))

print(lista_int)

# ast - zamiana string na liste
