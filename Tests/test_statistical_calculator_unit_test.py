#Author: Prajakta V Pendse

from statistical_calculator import Statistical_Calculator
import unittest
import  math
from CSVReader import CSV_Reader_For_Calculator

class Statistical_Calculator_Test(unittest.TestCase):

    @staticmethod
    def is_almost_equal(num1, num2):
        return math.fabs(float(num1) - float(num2)) < 0.001

    def test_mean(self):
        test_cases= CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestMean.csv")
        for test_case in test_cases:
            test_case_values = test_case[:-1]
            test_case_result = test_case[-1]
            print("Running mean test case: {}".format(test_case_values))
            self.assertTrue(Statistical_Calculator_Test.is_almost_equal(Statistical_Calculator.mean(test_case_values), test_case_result))

    def test_mean1(self):
        test_case=[]
        self.assertRaises(ValueError, Statistical_Calculator.mean, test_case)

        test_case.extend([1, 2, "something"])
        self.assertRaises(TypeError, Statistical_Calculator.mean, test_case)

    def test_zscore(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestZScore.csv")
        for test_case in test_cases:
            start_of_expected_results_index = int(len(test_case)/2)
            test_values = test_case[:start_of_expected_results_index]
            expected_results = test_case[start_of_expected_results_index:]
            print("Running Z-score test case: {}".format(test_values))

            z_scores = Statistical_Calculator.z_scores(test_values)

            self.assertEqual(len(z_scores), start_of_expected_results_index)

            for i in range(0, len(z_scores)):
                self.assertTrue(Statistical_Calculator_Test.is_almost_equal(z_scores[i], expected_results[i]))

    def test_zscore1(self):
        test_case=[]
        self.assertRaises(ValueError, Statistical_Calculator.z_scores, test_case)

        test_case=[1,2,3,4,"Test"]
        self.assertRaises(TypeError, Statistical_Calculator.z_scores, test_case)

    def test_pop_corr_coeff(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestPopulationCorrelationCoefficient.csv")
        for test_case in test_cases:
            second_sequence_start_index = int((len(test_case)-1) / 2)
            first_sequence = test_case[:second_sequence_start_index]
            second_sequence = test_case[second_sequence_start_index:-1]
            expected_population_correlation_coefficient = test_case[-1]

            print("Running Population Coefficient Coefficent for sequences test case: {} and {}".format(first_sequence, second_sequence))

            self.assertEqual(len(first_sequence), len(second_sequence), "Invalid test case: The two sequences must have equal lengths")

            self.assertTrue(Statistical_Calculator_Test.is_almost_equal(Statistical_Calculator.population_correlation_coefficient(first_sequence, second_sequence), expected_population_correlation_coefficient))

    def test_pop_corr_coeff1(self):
        first_sequence=[]
        second_sequence=[]
        self.assertRaises(ValueError, Statistical_Calculator.population_correlation_coefficient, first_sequence, second_sequence)

        first_sequence.extend([1,2,3])
        second_sequence.extend([1,2,3,4])
        self.assertRaises(ValueError, Statistical_Calculator.population_correlation_coefficient, first_sequence, second_sequence)

        first_sequence.append("Test")
        self.assertRaises(TypeError, Statistical_Calculator.population_correlation_coefficient, first_sequence,
                          second_sequence)

    def test_population_variance(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestPopulationVariance.csv")
        for test_case in test_cases:
            test_case_values = test_case[:-1]
            test_case_result = test_case[-1]
            print("Running Population Variance test case: {}".format(test_case_values))
            self.assertTrue(Statistical_Calculator_Test.is_almost_equal(Statistical_Calculator.population_variance(test_case_values),
                                                                        test_case_result))
    def test_population_variance_1(self):
        test_case=[]
        self.assertRaises(ValueError, Statistical_Calculator.population_variance, test_case)

        test_case.extend([1, 2, "something"])
        self.assertRaises(TypeError, Statistical_Calculator.population_variance, test_case)

    def test_sample_variance(self):
        test_cases = CSV_Reader_For_Calculator.get_numbers_from_file("Tests/CSVFiles/UnitTestSampleVariance.csv")
        for test_case in test_cases:
            test_case_values = test_case[:-1]
            test_case_result = test_case[-1]
            print("Running Sample Variance test case: {}".format(test_case_values))
            self.assertTrue(Statistical_Calculator_Test.is_almost_equal(
                Statistical_Calculator.variance_of_sample_proportion(test_case_values),
                test_case_result))

    def test_sample_variance1(self):
        test_case=[]
        self.assertRaises(ValueError, Statistical_Calculator.variance_of_sample_proportion, test_case)

        test_case.extend([1, 2, "something"])
        self.assertRaises(TypeError, Statistical_Calculator.variance_of_sample_proportion, test_case)


if __name__== "__main__":
    unittest.main()
