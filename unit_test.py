# -*- encoding: latin-1 -*-
import requests
import random
from examples_to_be_tested import FirstTest, Data, Model, LoginApi 
import unittest
from unittest.mock import MagicMock

class TestMatematik(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(FirstTest.addition(2,3),5)
        self.assertEqual(FirstTest.addition(0,0),0)

    def test_subtraktion(self):
        self.assertEqual(FirstTest.subtraktion(5,3),2)
        self.assertEqual(FirstTest.subtraktion(0,0),0)

    def test_addition_random(self):
        a = random.randint(0,100)
        b = random.randint(0,100)
        c = FirstTest.addition(a,b)
        self.assertGreaterEqual(c,a)
        self.assertGreaterEqual(c,b)

    def test_subtraktion_random(self):
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = FirstTest.subtraktion(a,b)
        self.assertTrue(c < a or c < b)

class TestModel(unittest.TestCase):

    def test_model_hämta_existerande(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.HämtaText(_id),"hej")

    def test_model_ändra_existerande(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.HämtaText(_id),"hej")
        model.ÄndraText(_id,"hejdå")
        self.assertEqual(model.HämtaText(_id),"hejdå")

    def test_model_ta_bort_existerande(self):
        model = Model()
        _id = model.SkapaText("hej")
        model.TaBortText(_id)
        self.assertEqual(model.HämtaText(_id),None)

    def test_model_hämta_icke_existerande(self):
        model = Model()
        self.assertEqual(model.HämtaText(0),None)

    def test_model_ändra_icke_existerande(self):
        model = Model()
        model.ÄndraText(0,"hejdå")
        self.assertEqual(model.HämtaText(0),"hejdå")

    def test_model_ta_bort_icke_existerande(self):
        model = Model()
        model.TaBortText(0)
        self.assertEqual(model.HämtaText(0),None)

class TestData(unittest.TestCase):

    def test_data_skriv(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.Hämta(0),"hej")

    def test_data_hämta_icke_existerande(self):
        data = Data()
        self.assertEqual(data.Hämta(0),None)

    def test_data_hämta_existerande(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.Hämta(0),"hej")

    def test_data_ta_bort_icke_existerande(self):
        data = Data()
        self.assertEqual(data.TaBort(0),{})

    def test_data_ta_bort_existerande(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.TaBort(0),{})
        self.assertEqual(data.Hämta(0),None)

class TestLoginApi(unittest.TestCase):

    class mock_valid_login:
        def __init__(self):
            self.status_code = 200
            self.body = { "token": "string" }
        def json(self):
            return self.body
    
    class mock_invalid_login:
        def __init__(self):
            self.status_code = 403
            self.body = {}
        def json(self):
            return self.body
    
    class mock_valid_use_api:
        def __init__(self, response_body):
            self.status_code = 200
            self.body = response_body
        def json(self):
            return self.body
    
    class mock_invalid_use_api:
        def __init__(self):
            self.status_code = 403
            self.body = {}
        def json(self):
            return self.body

    def test_valid_login(self):
        login = LoginApi()

        requests.post = MagicMock(return_value=self.mock_valid_login())
        self.assertEqual(login.login(),True)

    def test_invalid_login(self):
        login = LoginApi(username="test",password="test")

        requests.post = MagicMock(return_value=self.mock_invalid_login())
        self.assertEqual(login.login(),False)

    def test_valid_use_api(self):
        login = LoginApi()

        requests.post = MagicMock(return_value=self.mock_valid_login())
        login.login()
        post_data = { "test": "test" }
        requests.post = MagicMock(return_value=self.mock_valid_use_api(post_data))
        self.assertEqual(login.use_api(post_data),True)

    def test_invalid_use_api(self):
        login = LoginApi(username="test",password="test")

        requests.post = MagicMock(return_value=self.mock_invalid_login())
        login.login()
        post_data = { "test": "test" }
        requests.post = MagicMock(return_value=self.mock_invalid_use_api())
        self.assertEqual(login.use_api(post_data),False)

if __name__ == '__main__':
    unittest.main()
