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

class TestModel(unittest.TestCase):

    def test_model_h�mta(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.H�mtaText(_id),"hej")

    def test_model_�ndra(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.H�mtaText(_id),"hej")
        model.�ndraText(_id,"hejd�")
        self.assertEqual(model.H�mtaText(_id),"hejd�")

    def test_model_ta_bort(self):
        model = Model()
        _id = model.SkapaText("hej")
        model.TaBortText(_id)
        self.assertRaises(KeyError,model.H�mtaText,_id)

class TestData(unittest.TestCase):

    def test_data_skriv(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.H�mta(0),"hej")

    def test_data_h�mta_icke_existerande(self):
        data = Data()
        self.assertRaises(KeyError,data.H�mta,0)

    def test_data_h�mta_existerande(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.H�mta(0),"hej")

    def test_data_ta_bort(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.TaBort(0),{})
        self.assertRaises(KeyError,data.H�mta,0)

class TestLoginApi(unittest.TestCase):
    
    def test_login(self):
        requests.post = MagicMock(return_value={ "token": "string", "status_code": 200 })
        login = LoginApi()
        self.assertEqual(login.response,{ "token": "string", "status_code": 200 })

if __name__ == '__main__':
    unittest.main()
