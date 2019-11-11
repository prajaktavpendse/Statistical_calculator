#Author: Prajakta V Pendse

import unittest
from CSVReader import  CSV_Reader_For_Calculator
import math

class CSVReader_Unit_tests(unittest.TestCase):
    def test_normal_execution(self):
        print("CSV Reader tests: Checking for normal execution")
        test_cases= CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestMean.csv")
        self.assertEqual(len(test_cases), 3)
        for test_case in test_cases:
            self.assertTrue(isinstance(test_case, list))
            self.assertTrue(len(test_case)>0)
            for num in test_case:
                self.assertTrue(not math.isnan(float(num)))

    def test_file_not_found(self):
        print("CSV Reader tests: File not found")
        self.assertRaises(FileNotFoundError, CSV_Reader_For_Calculator.get_numbers_from_file, "ThisFileDoesNotExist.csv")
