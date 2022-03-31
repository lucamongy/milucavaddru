from Cavaddru import Cavaddru
from DBManager import DBManager
from funzioni import funzioni
import os


def menu(mod = "normal",clist = []):
    if mod == "test":
        testmenu = "---------------------\ntestmenu:\n-1: inserisci\n-2: lista\n---------------------"
        cmd = ""
        while cmd != "q":
            funzioni.cls()
            print(testmenu)
            cmd = input("inserisci comando (q per uscire)")
            #       INSERIMENTO
            if cmd == "1":
                clist.append(funzioni.inserimento_cv())
                cmd = ""
            #       VISUALIZZAZIONE
            if cmd == "2":
                funzioni.cls()
                funzioni.lista_cv()
                os.system("pause")
            #       ALLENAMENTO POTENZA    
            if cmd == "3":
                funzioni.cls()
                try: 
                    selected = int(input("Inserire id cavallo"))
                    try :

                        print(clist[selected - 1])
                        clist[selected - 1].allenamento_spd()
                        print("\n|\n|\nv")
                        print(clist[selected - 1])
                    except:
                        print("Id non valido")
                except:
                    print("Valore non numerico")
                os.system("pause")
            if cmd == "show":
                print(clist)
                os.system("pause")
    return clist

clist = DBManager.cread()

DBManager.cwrite(menu("test",clist))