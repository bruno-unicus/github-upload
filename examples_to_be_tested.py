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

    def ÄndraText(self,_id,text: str) -> bool:
        self.data.Skriv(_id,text)
        return True

    def TaBortText(self,_id: int) -> None:
        return self.data.TaBort(_id)

    def HämtaText(self,_id: int) -> Optional[str]:
        return self.data.Hämta(_id) 

class Data:

    def __init__(self):
        self.databas = {}

    def Skriv(self,_id: int,text: str) -> int:
        self.databas[_id] = text
        return _id

    def TaBort(self,_id: int) -> dict:
        del self.databas[_id]
        return self.databas

    def Hämta(self,_id: int) -> Optional[str]:
        return self.databas.get(_id)

class LoginApi:
    
    def __init__(self, username = "username", password = "password"):
        self.username = username
        self.password = password
        self.response_body = None
        self.response_status = None

    def login(self) -> bool:
        url = "http://www.faketestsiteurl.com/login/start"
        post_data = { "name": self.username, "password": self.password }
        response = requests.post(url, data = post_data)
        self.response_body = response.json()
        self.response_status = response.status_code

        if self.response_status == 200:
            if self.response_body == { "token": "string" }:
                return True
        return False
        
    def use_api(self, post_data: dict):
        url = "http://www.faketestsiteurl.com/returns"
        post_headers = { "auth": self.response.token }
        response = requests.post(url, headers = post_headers, data = post_data)
        self.response_body = response.json()
        self.response_status = response.status_code

        if self.response_status == 200:
            if self.response_body == post_data:
                return True
        return False
