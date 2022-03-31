from Cavaddru import Cavaddru
import os


class funzioni:

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def inserimento_cv():
        funzioni.cls()
        return Cavaddru(input("Inserisci nome:\t"))

    @staticmethod
    def lista_cv(clist = []):
        for c in clist:
            print(c)