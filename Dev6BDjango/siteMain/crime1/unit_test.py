from django.test import TestCase
from extraMethods import userData
from crime1.functions import addmoney, addExperience

class unit_test(TestCase):

    def test_addMoney(self):
        addmoney(1)
        self.assertEqual(userData.userData.money, 1)
        userData.userData.money = 0
        addmoney(2)
        self.assertEqual(userData.userData.money, 2)
        userData.userData.money = 0
        addmoney(100)
        self.assertEqual(userData.userData.money, 100)
        userData.userData.money = 0
        addmoney(150)
        self.assertEqual(userData.userData.money, 150)
        userData.userData.money = 0
        addmoney(2000)
        self.assertEqual(userData.userData.money, 2000)
        userData.userData.money = 0
        addmoney(500000)
        self.assertEqual(userData.userData.money, 500000)
        userData.userData.money = 0



    def test_experience(self):
        addExperience()
        self.assertEqual(userData.userData.crime1exp, 10)
        userData.userData.crime1exp = 0