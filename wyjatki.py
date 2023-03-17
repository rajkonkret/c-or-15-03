def mnozenie(a, b):
    try:
        print(int(a) * int(b))
    except ValueError:
        print("Błąd wartosci")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("inny bład", e)
    else:
        print("Nie ma")
    finally:
        print("Zawsze")


def dzielenie(a, b):
    try:
        print(int(a) / int(b))
    except ZeroDivisionError:
        print("Nie dziel przez zero")


mnozenie(2, 3)
mnozenie(2, "3")
mnozenie("a", "3")
print("Działam dalej")
mnozenie("2", "3")
mnozenie((2,), "3")
print("Działam dalej")
dzielenie(2, 0)  # ZeroDivisionError
print("Działam dalej")
