""" Unit test module.
"""

import unittest
from calculator.number_builder import NumberBuilder


class NumberBuilderTest(unittest.TestCase):
    """ Testcase.
    """

    def setUp(self):
        self.builder = NumberBuilder()

    def test_basic_number_build(self):
        # build +5961.4861
        for digit in [5, 9, 6, 1]:
            self.builder.append(digit)

        self.builder.set_build_target(
            self.builder.BuildTarget.FRACTION_PART
        )

        for digit in [4, 8, 6, 1]:
            self.builder.append(digit)

        self.assertEqual(
            self.builder.number,
            5961.4861
        )

        self.builder.clear()

    def test_negative_build(self):
        # build -75.003
        for digit in [7, 5]:
            self.builder.append(digit)

        self.builder.toggle_sign()

        self.builder.set_build_target(
            self.builder.BuildTarget.FRACTION_PART
        )

        for digit in [0, 0, 3]:
            self.builder.append(digit)

        self.assertEqual(
            self.builder.number,
            -75.003
        )

        self.builder.clear()

    def test_all_whole(self):
        # build 123,456,789
        for digit in range(1, 10):
            self.builder.append(digit)

        self.assertEqual(
            self.builder.number,
            123456789
        )

        self.builder.clear()

    def test_all_fraction(self):
        # build 0.005750023
        self.builder.set_build_target(
            self.builder.BuildTarget.FRACTION_PART
        )

        for digit in [0, 0, 5, 7, 5, 0, 0, 2, 3]:
            self.builder.append(digit)

        self.assertEqual(
            self.builder.number,
            0.005750023
        )

        self.builder.clear()

    def test_clear_builder(self):
        # build +5961.4861
        for digit in [5, 9, 6, 1]:
            self.builder.append(digit)

        self.builder.set_build_target(
            self.builder.BuildTarget.FRACTION_PART
        )

        for digit in [4, 8, 6, 1]:
            self.builder.append(digit)

        self.builder.clear()

        self.assertEqual(
            self.builder.number,
            None
        )

        self.builder.clear()

    def test_backspace_builder(self):
        # build +5961.4861
        for digit in [5, 9, 6, 1]:
            self.builder.append(digit)

        self.builder.set_build_target(
            self.builder.BuildTarget.FRACTION_PART
        )

        for digit in [4, 8, 6, 1]:
            self.builder.append(digit)

        self.builder.backspace()  # del 1
        self.builder.backspace()  # del 6

        self.assertEqual(
            self.builder.number,
            5961.48
        )

        self.builder.clear()
