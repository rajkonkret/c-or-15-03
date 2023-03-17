from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisujaca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lece z szybkoscia", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    to jest klasa Orzel
    """

    def poluj(self):
        print("Tu", self.gatunek, ". Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, ". Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Ide sobie podziobac")

    def wydaj_odglos(self):
        print("kokokokoko")


# 14:45

# orzel = Ptak("orzel", 10)
# kura = Ptak("kura", 0)
# kura.wydaj_odglos()
# orzel.latam()
# kura.latam()
orzel_2 = Orzel("orzel", 10)
orzel_2.poluj()
orzel_2.latam()
kura_2 = Kura("kura")
kura_2.latam()
kura_2.dziobanie()
kura_2.wydaj_odglos()
