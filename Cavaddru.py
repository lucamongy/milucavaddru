import random

class Cavaddru:
    codice = 1

    def __init__(self,nome,codice=0,pwr=0,spd=0,stm=0):
        self.nome = nome

        if codice == 0: #codice da autoincrementare
            self.codice = Cavaddru.codice
        else:   #codice fornito
            self.codice = codice
            Cavaddru.codice = codice
        Cavaddru.codice +=1

        #power
        if pwr == 0:
            self.pwr = Cavaddru.power()
        else:
            self.pwr = pwr

        #speed
        if spd == 0:
            self.spd = 1
        else:
            self.spd = spd

        #stamina
        if stm == 0:
            self.stm = 1
        else:
            self.stm = stm

    def todict(self):
        d = {}
        d["nome"] = self.nome
        d["codice"] = self.codice
        d["pwr"] = self.pwr
        d["spd"] = self.spd
        d["stm"] = self.stm

        return d

    def __str__(self):
        s = f"\n----------\n-Nome Caviaddru: {self.nome}\n-Pputenza: {self.pwr}\n-Velocità: {self.spd}\n-Stamina: {self.stm}\n----------"
        return s
    @staticmethod
    def power():
        pwr = random.randint(1,100)
        return pwr

    def allenamento_spd(self):
        if self.spd < 100:
            self.spd += 1
            answer = "Allenamento potenza avvenuto"        
        else:
            answer = "Cavaddu alla massima potenza"
        return answer
