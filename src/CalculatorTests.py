import unittest
from Calculator import Calculator
import csv

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calulator_return_difference(self):
        self.calculator.subtraction(1, 4)
        self.assertEqual(self.calculator.result,-3)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result,0)

    def test_add_method_calculator(self):
        self.calculator.Addition(2, 2)
        self.assertEqual(self.calculator.result,4)

    def test_multiply_method_calculator(self):
        self.calculator.multiplication(4,5)
        self.assertEqual(self.calculator.result,20)

    def test_divide_method_calculator(self):
        self.calculator.division(5, 20)
        self.assertEqual(self.calculator.result,4)

    def test_square_method_calculator(self):
        self.calculator.square(5)
        self.assertEqual(self.calculator.result,25)

    def test_square_method_calculator(self):
        self.calculator.squareroot(64)
        self.assertEqual(self.calculator.result,8)


if __name__ == '__main__':
    unittest.main()
