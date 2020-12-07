""" Unittest.
"""

import unittest
from calculator.standard.number_model import NumberModel


class NumberModelTest(unittest.TestCase):
    """ Number model test suite.
    """

    def setUp(self):
        self.number = NumberModel()

    def test_append(self):
        # steps
        self.number.new()
        appended_a = self.number.is_appended()
        self.number.append(self.number.Symbols.ONE)
        appended_b = self.number.is_appended()

        # test
        self.assertFalse(appended_a)
        self.assertTrue(appended_b)

    def test_initial_number(self):
        # steps
        self.number.new()
        self.number.change_sign()
        self.number.append(self.number.Symbols.ZERO)

        # test
        self.assertEqual(self.number.join(), "0")

    def test_append_single_digit(self):
        # steps
        self.number.new()
        self.number.append(self.number.Symbols.ONE)

        # test
        self.assertEqual(self.number.join(), "1")

    def test_append_whole_numbers(self):
        # steps
        self.number.new()
        self.number.append(self.number.Symbols.ONE)
        self.number.append(self.number.Symbols.TWO)
        self.number.append(self.number.Symbols.THREE)

        # test
        self.assertEqual(self.number.join(), "123")

    def test_append_fraction_numbers(self):
        # steps
        self.number.new()
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.ONE)
        self.number.append(self.number.Symbols.TWO)
        self.number.append(self.number.Symbols.THREE)

        # test
        self.assertEqual(self.number.join(), "0.123")

    def test_append_combination(self):
        # steps
        self.number.new()
        self.number.append(self.number.Symbols.ONE)
        self.number.append(self.number.Symbols.TWO)
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.THREE)
        self.number.append(self.number.Symbols.FOUR)

        # test
        self.assertEqual(self.number.join(), "12.34")

    def test_negative_combination(self):
        # steps
        self.number.new()
        self.number.append(self.number.Symbols.ONE)
        self.number.append(self.number.Symbols.TWO)
        self.number.change_sign()
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.DECIMAL_PT)
        self.number.append(self.number.Symbols.THREE)
        self.number.change_sign()
        self.number.append(self.number.Symbols.FOUR)
        self.number.change_sign()

        # test
        self.assertEqual(self.number.join(), "-12.34")

    def test_backspace(self):
        #################################################
        # scenario 1: positive numbers
        #################################################
        # steps
        self.number.new()
        for _ in range(1, 10):
            self.number.append(self.number.Symbols.ONE)

        for _ in range(1, 10):
            self.number.backspace()
        # test
        self.assertEqual(self.number.join(), "0")

        #################################################
        # scenario 2: negative numbers
        #################################################
        # steps
        self.number.new()
        for _ in range(1, 10):
            self.number.append(self.number.Symbols.ONE)
        self.number.change_sign()

        for _ in range(1, 10):
            self.number.backspace()
        # test
        self.assertEqual(self.number.join(), "0")

        #################################################
        # scenario 3: backspace on zero (0)
        #################################################
        # test
        self.number.new()
        self.number.backspace()
        self.number.backspace()
        # test
        self.assertEqual(self.number.join(), "0")
