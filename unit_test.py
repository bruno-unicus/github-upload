# -*- encoding: latin-1 -*-
from examples_to_be_tested import *
import unittest

class TestAll(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(firstTest.addition(2,3),5)
        self.assertEqual(firstTest.addition(0,0),0)

    def test_subtraktion(self):
        self.assertEqual(firstTest.subtraktion(5,3),2)
        self.assertEqual(firstTest.subtraktion(0,0),0)

    def test_model(self):
        model = Model()
        _id = model.SkapaText("hej")
        self.assertEqual(model.HämtaText(_id),"hej")
        self.assertEqual(model.ÄndraText(_id,"hejdå"),True)
        self.assertEqual(model.HämtaText(_id),"hejdå")
        self.assertEqual(model.TaBortText(_id),None)

    def test_data(self):
        data = Data()
        self.assertEqual(data.Skriv(0,"hej"),0)
        self.assertEqual(data.Hämta(0),"hej")
        self.assertEqual(data.TaBort(0),None)

if __name__ == '__main__':
    unittest.main()

