"""test cases for 1/x"""
import unittest
import calc


class CalculatorTest(unittest.TestCase):
    """test case"""
    def test_one_by_x_value(self):
        """when we take a proper value"""
        self.assertEqual(calc.one_by_x(1), 1)

    def test_one_by_x_zero_division_error(self):
        """division cannot be done with zero"""
        self.assertEqual(calc.one_by_x(0), "ZeroDivisionError")

    def test_one_by_x_value_error(self):
        """Value error--giving string instead of number"""
        result = calc.one_by_x("s")
        self.assertEqual(result, "TypeError")


if __name__ == "__main__":
    unittest.main()
