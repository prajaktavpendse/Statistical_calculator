#Author: Prajakta V Pendse

import unittest
from latest_scalculator import Calculator
from CSVReader import CSV_Reader_For_Calculator
import math


class Unit_Test(unittest.TestCase):
    def test_add(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestAddition.csv")

        for test in test_cases:
            print("Running addition test case: {}".format(test))
            self.assertEqual(test[2], Calculator.addition([test[0], test[1]]))

    def test_subtraction(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestSubtraction.csv")

        for test in test_cases:
            print("Running subtraction test case: {}".format(test))
            self.assertEqual(test[2], Calculator.subtraction(test[1], test[0]))

    def test_division(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestDivision.csv")

        for test in test_cases:
            print("Running division test case: {}".format(test))
            self.assertTrue(math.fabs(test[2] - Calculator.division(test[1], test[0])) <= 0.001)

    def test_multiplication(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestMultiplication.csv")

        for test in test_cases:
            print("Running multiplication test case: {}".format(test))
            self.assertEqual(test[2], Calculator.multiplication([test[1], test[0]]))

    def test_square(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestSquare.csv")

        for test in test_cases:
            print("Running square test case: {}".format(test))
            self.assertEqual(test[1], Calculator.square(test[0]))

    def test_square_root(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestSquareRoot.csv")

        for test in test_cases:
            print("Running square root test case: {}".format(test))
            self.assertTrue(math.fabs(test[1] - Calculator.square_root(test[0])) <= 0.001)

    def test_process_input_data(self):
        calculator = Calculator()
        self.assertTrue(math.isnan(calculator.result))

        result_list = calculator.process_input_data("1 2 3 4 5 ADD")
        self.assertEqual(result_list, [Calculator.Operation.ADD, [1, 2, 3, 4, 5]])

        result_list = calculator.process_input_data("1 2 DIVISION")
        self.assertEqual(result_list, [Calculator.Operation.DIVIDE, [1, 2]])

    def test_dispatch_and_compute_result(self):
        result = Calculator.dispatch_and_compute_result(Calculator.Operation.ADD, [1,2,3])
        self.assertEqual(result, 6)

        # Should ignore the remaining numbers after the first two
        result = Calculator.dispatch_and_compute_result(Calculator.Operation.SUBTRACT, [2, 1, 3, 4, 5])
        self.assertEqual(result, 1)
