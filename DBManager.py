import json
from Cavaddru import Cavaddru

class DBManager:



    @staticmethod
    def cread():
        clist = []
        dictList = []
        try:
            with open('cavaddri.dbs', 'r+', encoding='utf-8') as db:
                for c in db.readlines():
                    dictList.append(json.loads(c))
        except(FileNotFoundError):
            print("File cavaddri inesistente.")
            return clist
        for c in dictList:
            codice = c["codice"]
            nome = c["nome"]
            pwr = c["pwr"]
            spd = c["spd"]
            stm = c["stm"]
            clist.append(Cavaddru(nome,codice,pwr,spd,stm))
        return clist

    @staticmethod
    def cwrite(clist):
       with open('cavaddri.dbs', 'w', encoding='utf-8') as db:
          for c in clist:
               json.dump(c.todict(), db)
               db.write("\n")