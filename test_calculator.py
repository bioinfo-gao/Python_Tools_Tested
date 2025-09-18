# test_calculator.py
# reticulate::repl_python() # <======== activated python in R env
import unittest
from calculator import add, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 3), 3.33333333, places=7)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)


if __name__ == '__main__':
    unittest.main()
    
