import unittest
from Calculator import Calculator
import csv
import pprint
import importlib.util

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

    def test_squareroot_method_calculator(self):
        self.calculator.squareroot(64)
        self.assertEqual(self.calculator.result,8)

#CSV Testing
    def test_subtraction(self):
        test_data = CsvReader("ExampleCSVs/Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(int(row['Value']), int(row['Value 2'])))

    def test_Addition(self):
        test_data = CsvReader("ExampleCSVs/Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(int(row['Value']), int(row['Value 2'])))

    def test_multiplication(self):
        test_data = CsvReader("ExampleCSVs/Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(int(row['Value']), int(row['Value 2'])))

    def test_division(self):
        test_data = CsvReader("ExampleCSVs/Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(int(row['Value']), int(row['Value 2'])))

    def test_square(self):
        test_data = CsvReader("ExampleCSVs/Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(int(row['Value']), int(row['Value 2'])))

    def test_squareroot(self):
        test_data = CsvReader("ExampleCSVs/SquareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(int(row['Value']), int(row['Value 2'])))

if __name__ == '__main__':
    unittest.main()
