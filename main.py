from Cavaddru import Cavaddru
from DBManager import DBManager
from funzioni import funzioni
import os

def menu(mod = "normal",clist = []):
    if mod == "test":
        testmenu = "-----------\ntestmenu:\n-1: inserisci\n-2: lista\n-----------"
        cmd = ""
        while cmd != "q":
            funzioni.cls()
            print(testmenu)
            cmd = input("inserisci comando (q per uscire)")
            if cmd == "1":
                funzioni.cls()
                nome = input("nome")
                clist.append(Cavaddru(nome))
                cmd = ""
            if cmd == "2":
                funzioni.cls()
                for c in clist:
                    print(c)
                cmd = input("inserisci comando (vuoto per tornare al main menu - q per uscire)")
    return clist

clist = DBManager.cread()

DBManager.cwrite(menu("test",clist))