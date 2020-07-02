import unittest
import csv, ClassFactory
import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.csv_reader = CsvReader('ExampleCSVs/Addition.csv')

    def test_return_data_as_objects(self):
1

if __name__ == '__main__':
    unittest.main()
