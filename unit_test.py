# -*- encoding: latin-1 -*-
from examples_to_be_tested import *
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
        a = random.randint(0,100)
        b = random.randint(0,100)
        c = FirstTest.subtraktion(a,b)
        self.assertLessEqual(c,a)
        self.assertLessEqual(c,b)

class TestModel(unittest.TestCase):

    def test_model_hämta(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.HämtaText(_id),"hej")

    def test_model_ändra(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.HämtaText(_id),"hej")
        model.ÄndraText(_id,"hejdå")
        self.assertEqual(model.HämtaText(_id),"hejdå")

    def test_model_ta_bort(self):
        model = Model()
        _id = model.SkapaText("hej")
        model.TaBortText(_id)
        self.assertRaises(KeyError,model.HämtaText,_id)

class TestData(unittest.TestCase):

    def test_data_skriv(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.Hämta(0),"hej")

    def test_data_hämta_icke_existerande(self):
        data = Data()
        self.assertRaises(KeyError,data.Hämta,0)

    def test_data_hämta_existerande(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.Hämta(0),"hej")

    def test_data_ta_bort(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.TaBort(0),{})
        self.assertRaises(KeyError,data.Hämta,0)

class TestLoginApi(unittest.TestCase):
    
    def test_login(self):
        requests.post = MagicMock(return_value={ "token": "string", "status_code": 200 })
        login = LoginApi()
        self.assertEqual(login.response,{ "token": "string", "status_code": 200 })

if __name__ == '__main__':
    unittest.main()
