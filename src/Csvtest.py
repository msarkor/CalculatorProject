import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.csv_reader = CsvReader()

    def test_return_data_as_objects(self):


if __name__ == '__main__':
    unittest.main()
