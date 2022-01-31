# -*- encoding: latin-1 -*-
import random
from typing import Optional
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

    def H�mtaText(self,_id: int) -> Optional[str]:
        return self.data.H�mta(_id) 

class Data:

    def __init__(self):
        self.databas = {}

    def Skriv(self,_id: int,text: str) -> int:
        self.databas[_id] = text
        return _id

    def TaBort(self,_id: int) -> dict:
        if _id in self.databas:
            del self.databas[_id]
        return self.databas

    def H�mta(self,_id: int) -> Optional[str]:
        return self.databas.get(_id)

class LoginApi:
    
    def __init__(self, username = "username", password = "password"):
        self.username = username
        self.password = password
        self.response = None

    def login(self) -> bool:
        url = "http://www.faketestsiteurl.com/login/start"
        post_data = { "name": self.username, "password": self.password }
        self.response = requests.post(url, data = post_data)
        
        if self.response.status_code == 200:
            if self.response.json() == { "token": "string" }:
                return True
        return False
        
    def use_api(self, post_data: dict):
        url = "http://www.faketestsiteurl.com/returns"
        token = self.response.json().get("token")
        post_headers = { "auth": token }
        self.response = requests.post(url, headers = post_headers, data = post_data)

        if self.response.status_code == 200:
            if self.response.json() == post_data:
                return True
        return False
