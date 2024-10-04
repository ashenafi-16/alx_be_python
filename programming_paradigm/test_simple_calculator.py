import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,2), 6)
        self.assertEqual(self.calc.subtract(8,0), 8)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(8,2), 16)
        self.assertEqual(self.calc.multiply(8,5), 40)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(8,1), 8)
        self.assertEqual(self.calc.divide(8,0), None)
        self.assertEqual(self.calc.divide(8,2), 4)
        

# Remember to write additional test methods for subtract, multiply, and divide.