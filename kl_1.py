class Human:
    """
    To jest klasa opisujaca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        """
        metoda witająca
        :return:
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


cz_1 = Human()  # obiekt klasy Human
print(cz_1.__doc__)
print(cz_1.plec)
cz_1.imie = "radek"
cz_1.powitanie()
cz_1.ruszaj()