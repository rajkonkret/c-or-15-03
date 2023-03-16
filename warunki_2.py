# lista = []
#
# lang = input("Wpisz znany Ci język programowania")
#
# match lang.lower():
#     case "python":
#         lista.append(lang)
#     case "java":
#         lista.append(lang)
#     case "c++":
#         lista.append(lang)
#     case _:
#         print("Nie znam takiego jezyka")
#
# print(lista)
# odp = input("Podaj date Chrztu Polski")
match odp:
    case "966":
        print("ok")
    case _:
        print("Ty głabie")
