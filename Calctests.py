import unittest
from Calc import Calc


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calc, Calc)

    def test_results_property_calc(self):
        self.assertEqual(self.calc.result, 0)

    def test_add_method_calc(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.result, 4)

    def test_subtract_method_calc(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.result, 0)

    def test_mul_method_calc(self):
        self.assertEqual(self.calc.mul(2, 2), 4)
        self.assertEqual(self.calc.result, 4)

    def test_div_method_calc(self):
        self.assertEqual(self.calc.div(2, 2), 1)
        self.assertEqual(self.calc.result, 1)

    def test_sq_method_calc(self):
        self.assertEqual(self.calc.sq(2), 4)
        self.assertEqual(self.calc.result, 4)

    def test_sqroot_method_calc(self):
        self.assertEqual(self.calc.sqroot(4), 2)
        self.assertEqual(self.calc.result, 2)

if __name__ == '__main__':
    unittest.main()
