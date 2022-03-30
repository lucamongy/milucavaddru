import os

class funzioni:

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def inserimento_cv():
        funzioni.cls()
        nome = input("nome")
        return nome