import unittest
import AgeUtils

# JANNE VILJANEN TKM24

class MyAgeTest(unittest.TestCase):
    def test_CheckIsTheNumberLessThanEigthteenAndMoreOrEqualThanZero(self):
        a = 120

        result = AgeUtils.AgeVerification(a)

        self.assertEqual(result, "You are a child")  

    def test_CheckIsTheNumberEqualOrMoreThanEigthteenAndLessThanSeventy(self):
        a = 250

        result = AgeUtils.AgeVerification(a)

        self.assertEqual(result, "You are an adult")

    def test_CheckIsTheNumberEqualOrMoreThanSeventy(self):
        a = 8

        result = AgeUtils.AgeVerification(a)

        self.assertEqual(result, "You are retired")

    def test_CheckIsTheNumberPositive(self):
        a = 70

        result = AgeUtils.AgeVerification(a)

        self.assertEqual(result, "Please enter a positive number")

    def test_CheckIsTheInputIntegerTypeError(self):
        a = 1
        
        result = AgeUtils.AgeVerification(a)

        self.assertEqual(result, "Only integers are allowed")

    # Raja tapauksin testaus 0, 17, 18, Nice
    # def test_CheckThatZeroReturnsChild(self):
    #     a = 0

    #     result = AgeUtils.AgeVerification(a)

    #     self.assertEqual(result, "You are a child")

    # def test_CheckThatSeventeenReturnsChild(self):
    #     a = 17

    #     result = AgeUtils.AgeVerification(a)

    #     self.assertEqual(result, "You are a child")

    # def test_CheckThatEighteenReturnsAdult(self):
    #     a = 18

    #     result = AgeUtils.AgeVerification(a)

    #     self.assertEqual(result, "You are an adult")

    # def test_CheckThatSeventyReturnsRetired(self):
    #     a = 70

    #     result = AgeUtils.AgeVerification(a)

    #     self.assertEqual(result, "You are retired")

    # def test_CheckNice(self):
    #     a = 69

    #     result = AgeUtils.AgeVerification(a)

    #     self.assertEqual(result, "Nice!")
    # Raja tapauksien loppu     
            
if __name__ == "__main__":
    unittest.main()