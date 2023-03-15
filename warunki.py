# czy_znasz_Pythona = True
#
# odp = input("Czy znasz pythona?(t/n)")
#
# if odp.lower() == 't':
#     print("Brawo")
# else:
#     print("Idz sie uczyc")
#
# print("Koniec")
# podatek = 0.0
# zarobki = int(input("Podaj dochod"))
# dodac, ze pomiedzy 30 tys a 100 tys podatek 20%
# if zarobki < 10000:
#     podatek = 0.05
# elif zarobki < 30000:
#     podatek = 0.1
# elif zarobki < 100000:
#     podatek = 0.2
# else:
#     podatek = 0.7
#
# print(f"Zapłacisz {zarobki * podatek} zł")
# suma_zam = 167
# if suma_zam > 100:
#     rabacik = 25
# else:
#     rabacik = 0
# print("suma zam", suma_zam, "rabat", rabacik)
# rabacik = 25 if suma_zam > 100 else 0
# print("suma zam", suma_zam, "rabat", rabacik)

lista_bledow = []
alert_system = 'email'
error = 'medium'
error_message = "Stało sie cos strasznego"
if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'critical':
        lista_bledow.append("critical")
    elif error == 'medium':
        lista_bledow.append('medium')
    else:
        lista_bledow.append("Nieznany")
else:
    pass

print(lista_bledow)
