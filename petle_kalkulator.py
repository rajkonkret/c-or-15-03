while True:
    a = int(input("Podaj pierwsza liczbe"))
    b = int(input("Podaj druga liczbe"))
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")
    wybor = input("Podaj opcje (1-5)")
    if wybor == '1':
        print(a + b)
    elif wybor == '2':
        print(a - b)
    elif wybor == '3':
        print(a * b)
    elif wybor == '4':
        if b == 0:
            print("nie dzilimy przez zero")
        else:
            print(a / b)
    else:
        break
