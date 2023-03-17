class Dom:
    """
    To jest klasa Dom opisujca dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.metraz = metraz
        self.kolor = kolor
        self.liczba_okien = liczba_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.metraz = wybor
        print("Metraz wynosi ", self.metraz)


# dodac metody zmien_kolor, zmien_okna
dom_1 = Dom(23, "czerwony", 7)
print(dom_1.kolor)
dom_1.metraz = 45
dom_1.zmien_metraz()
