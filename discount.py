from datetime import date, timedelta

# today = date.today()
# print(today)
# print(today.year)
# print(today.timetuple())
# tomorow = today + timedelta(days=1)  # today + 1 day = tomorrow
# products = [
#     {'sku': '1', 'expiration_date': today, 'price': 100.0},
#     {'sku': '2', 'expiration_date': tomorow, 'price': 50},
#     {'sku': '3', 'expiration_date': today, 'price': 20}
# ]
# for i in range(1, 6):  # 0..4
#
#     for product in products:
#         if product['expiration_date'] != today:
#             continue
#         product['price'] *= 0.8  # p = p * 0.8
#         print(
#             'Price for sku', product['sku'],
#             'is now', product['price']
#         )
#     print(i)


print("Podaj liczbe ocen")
liczba_ocen = int(input())
suma = 0
i = 1

while i <= liczba_ocen:
    print("Podaj ocene " + str(i) + ":")
    ocena = float(input())
    if ocena < 0:
        continue
    suma += ocena  # suma =suma +ocena
    i += 1
print("Suma ocen " + str(suma))
print("Średnia ocen " + str(suma / liczba_ocen))
