import os

class funzioni:

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

