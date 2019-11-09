from latest_scalculator import Calculator
from enum import Enum

class Statistical_Calculator(Calculator):
    def __init__(self):
        self.result = 0

    class statistical_operation(Enum):
        MEAN = 8,
        Z_SCORE = 9,
        POPULATION_CORRELATION_COEFFICIENT = 10,
        POPULATION_VARIANCE = 11,
        VARIANCE_OF_SAMPLE_PROPORTION = 12,
        UNKNOWN = 7000

    @staticmethod
    def get_operation(operation):
        o = Calculator.get_operation(operation)
        if o is not Calculator.Operation.UNKNOWN:
            return o
        else:
            o1 = operation.upper()
            if "MEAN" in operation:
                return Statistical_Calculator.statistical_operation.MEAN
            elif "Z_SCORES" in operation:
                return Statistical_Calculator.statistical_operation.Z_SCORE
            elif "POP_COR_COEFF" in operation:
                return Statistical_Calculator.statistical_operation.POPULATION_CORRELATION_COEFFICIENT
            elif "POP_VARIANCE" in operation:
                return Statistical_Calculator.statistical_operation.POPULATION_VARIANCE
            elif "VARIANCE_SAMPLE_POP" in operation:
                return Statistical_Calculator.statistical_operation.VARIANCE_OF_SAMPLE_PROPORTION
            else:
                return Statistical_Calculator.statistical_operation.UNKNOWN

    @staticmethod
    def dispatch_and_compute_result(operation, nums):
        if isinstance(operation, str):
            operation = Statistical_Calculator.get_operation(operation)

        if operation == Statistical_Calculator.statistical_operation.MEAN:
            return Statistical_Calculator.mean(nums)
        elif operation == Statistical_Calculator.statistical_operation.Z_SCORE:
            return Statistical_Calculator.z_scores(nums)
        elif operation == Statistical_Calculator.statistical_operation.POPULATION_CORRELATION_COEFFICIENT:
            return Statistical_Calculator.population_correlation_coefficient(nums[0], nums[1])
        elif operation == Statistical_Calculator.statistical_operation.POPULATION_VARIANCE:
            return Statistical_Calculator.population_variance(nums)
        elif operation == Statistical_Calculator.statistical_operation.VARIANCE_OF_SAMPLE_PROPORTION:
            return Statistical_Calculator.variance_of_sample_proportion(nums)
        else:
            return Calculator.dispatch_and_compute_result(operation, nums)

    @staticmethod
    def population_correlation_coefficient(nums1, num2):
        if not isinstance(nums1, list) or not isinstance(num2, list):
            raise  ValueError("Population correlation coefficient, invalid inputs")

        if len(nums1) != len(num2):
            raise  ValueError("Population correlation coefficient, sequences must be of the same length")

        num1_mean = Statistical_Calculator.mean(nums1)
        num2_mean = Statistical_Calculator.mean(num2)

        temp = 0.00
        for i in range(0, len(nums1)):
            temp = temp + ((nums1[i] - num1_mean)*(num2[i] - num2_mean))

        covariance = temp / len(nums1)

        nums1_standard_deviation = Statistical_Calculator.standard_deviation(nums1)
        num2_standard_deviation = Statistical_Calculator.standard_deviation(num2)

        if nums1_standard_deviation * num2_standard_deviation == 0:
            return  inf
        else:
         return covariance / (nums1_standard_deviation * num2_standard_deviation)

    @staticmethod
    def z_scores(nums):
        mean = Statistical_Calculator.mean(nums)
        standard_deviation = Statistical_Calculator.standard_deviation(nums)
        z_scores = [(num-mean)/standard_deviation for num in nums]
        return z_scores

    @staticmethod
    def population_variance(nums):
        return Calculator.square(Statistical_Calculator.standard_deviation(nums))

    @staticmethod
    def standard_deviation(nums):
        mean = Statistical_Calculator.mean(nums)
        squared_differences = [Calculator.square(num - mean) for num in nums]
        return Calculator.square_root(Statistical_Calculator.mean(squared_differences))

    @staticmethod
    def variance_of_sample_proportion(nums):
        #Ref https://www.mathsisfun.com/data/standard-deviation.html
        if len(nums) < 2:
            raise ValueError("Too few numbers")
        return Statistical_Calculator.population_variance(nums) * len(nums) / (len(nums)-1)

    @staticmethod
    def mean(nums):
        if not nums:
            raise ValueError("Empty array")
        return Calculator.addition(nums) / len(nums)

    def start_interactive_calculator(self):
        print("Welcome to the interactive mode\n "
              "Example usage:\n"
              "(1) num1 num2 ... numN MEAN\n"
              "(2) num1 num2 ... numN Z_SCORES\n"
              "(3) num1 num2 ... numN POP_COR_COEFF (you will be prompted again for second sequence)\n"
              "(4) num1 num2 ... numN POP_VARIANCE\n"
              "(5) num1 num2 ... numN VARIANCE_SAMPLE_POP\n"
              "(6) Use res to use results of computations till now\n"
              "Example: 1 2 3 4 5 MEAN"
              "Press Enter to display result and exit")

        input_str = input("Enter input: ")
        while input_str:
            input_data = self.process_input_data(input_str, Statistical_Calculator.get_operation)
            if input_data[0] == Statistical_Calculator.statistical_operation.POPULATION_CORRELATION_COEFFICIENT:
                input_data1 = self.process_input_data("{} POP_COR_COEFF".format(input("Please enter second sequence")), Statistical_Calculator.get_operation)
                self.result = Statistical_Calculator.dispatch_and_compute_result(input_data[0], [input_data[1], input_data1[1]])
            else:
                self.result = Statistical_Calculator.dispatch_and_compute_result(input_data[0], input_data[1])
            input_str = input("Enter input: ")
        print("Result: {}".format(self.result))

if __name__ == "__main__":
    sc = Statistical_Calculator()
    sc.start_interactive_calculator()