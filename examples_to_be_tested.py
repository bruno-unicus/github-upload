# -*- encoding: latin-1 -*-
import random

class firstTest():

    def addition(a: int,b: int) -> int:
        return a + b

    def subtraktion(a: int,b: int) -> int:
        return a - b

class Model:

    def __init__(self):
        self.data = Data()

    def SkapaText(self,text: str) -> int:
        _id = random.randint(3, 9)
        self.data.Skriv(_id,text)
        return _id

    def ÄndraText(self,_id,text: str) -> bool:
        self.data.Skriv(_id,text)
        if True:
            return True
        else:
            return False

    def TaBortText(self,_id: int) -> None:
        return self.data.TaBort(_id)

    def HämtaText(self,_id: int) -> str:
        return self.data.Hämta(_id) 

class Data:

    def __init__(self):
        self.databas = {}

    def Skriv(self,_id: int,text: str) -> int:
        self.databas[_id] = text
        return _id

    def TaBort(self,_id: int) -> None:
        self.databas[_id] = None
        return None

    def Hämta(self,_id: int) -> str:
        return self.databas[_id]
