# importataan unittest jotta saadaan testit, ja importataan testattava ohjelma
import unittest
import CalculatorUtils

# luodaan luokka, ei tarvi olla sama nimi kuin itse teidostolla, mutta on selkeetä. unittest.TestCase vaaditaan testaamiseen
class MyCalculatorTest(unittest.TestCase):
    def test_CalculateSumOfIntegers_A_and_B_AssingValueToInteger_C(self):
        # Arrange
        a = int(7)
        b = int(4)
        # Act
        result = CalculatorUtils.addition(a,b)
        # Assert
        self.assertEqual(result, 11)
    def test_CalculateSubtractionOfIntegers_A_and_B_AssingValueToInteger_C(self):
        # Arrange
        a = int(7)
        b = int(4)
        # Act
        result = CalculatorUtils.subtraction(a,b)
        # Assert
        self.assertEqual(result, 3)
    def test_CalculateMultiplicationOfIntegers_A_and_B_AssingValueToInteger_C(self):
        # Arrange
        a = int(6)
        b = int(6)
        # Act
        result = CalculatorUtils.multiplication(a,b)
        # Assert
        self.assertEqual(result, 36)
    def test_CalculateDivisionOfIntegers_A_and_B_AssingValueToInteger_C(self):
        # Arrange
        a = int(20)
        b = int(5)
        # Act
        result = CalculatorUtils.division(a,b)
        # Assert
        self.assertEqual(result, 4)
# __name__ ottaa automaattisesti nimen ja sanoo että se on mainissä.
if __name__ == "__main__":
    unittest.main()