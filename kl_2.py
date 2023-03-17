class Human:
    """
    Klasa opisująca człowieka
    """

    def __init__(self, imie, wiek=0, plec='m'): # konstruktor dla klasy Human
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

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


cz_1 = Human("Radek")
cz_1 = Human("Radek", 36, 'p')
cz_1.powitanie()
cz_1.ruszaj()
