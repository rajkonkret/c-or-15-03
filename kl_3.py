class Dom:
    """
    To jest klasa Dom opisujca dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz  # pole prywatne
        self.kolor = kolor
        self.__liczba_okien = liczba_okien

    def wypisz_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.__metraz = wybor
        print("Metraz wynosi ", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.kolor = wybor
        print("teraz masz kolor", self.kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj nową liczbe okien"))
        self.__liczba_okien = wybor
        print("Metraz wynosi ", self.__liczba_okien)

    def __farba(self):
        print("Skonczyłą sie farba")


# dodac metody zmien_kolor, zmien_okna
dom_1 = Dom(23, "czerwony", 7)
print(dom_1.kolor)
dom_1.zmien_metraz()
dom_1.zmien_okna()
dom_1.zmien_kolor()
dom_1.wypisz_metraz()