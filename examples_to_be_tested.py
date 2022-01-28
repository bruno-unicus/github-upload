# -*- encoding: latin-1 -*-
import random
import requests

class FirstTest:

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

    def �ndraText(self,_id,text: str) -> bool:
        self.data.Skriv(_id,text)
        return True

    def TaBortText(self,_id: int) -> None:
        return self.data.TaBort(_id)

    def H�mtaText(self,_id: int) -> str:
        return self.data.H�mta(_id) 

class Data:

    def __init__(self):
        self.databas = {}

    def Skriv(self,_id: int,text: str) -> int:
        self.databas[_id] = text
        return _id

    def TaBort(self,_id: int) -> dict:
        del self.databas[_id]
        return self.databas

    def H�mta(self,_id: int) -> str:
        return self.databas[_id]

class LoginApi:
    
    def __init__(self, username = "username", password = "password"):
        post_data = { "name": username, "password": password }
        url = "http://www.faketestsiteurl.com/login/start"
        self.response = requests.post(url, data = post_data)

    def use_api(self, post_data: dict):
        url = "http://www.faketestsiteurl.com/returns"
        post_headers = { "auth": self.response.token }
        self.response = requests.post(url, headers = post_headers, data = post_data)
