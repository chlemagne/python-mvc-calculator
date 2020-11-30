""" Unit test module.
"""

import unittest
from calculator.equation_builder import EquationBuilder


class EquationBuilderTest(unittest.TestCase):
    """ Testcase.
    """

    def setUp(self):
        self.builder = EquationBuilder()
        self.test_data = [
            "99 + 1 − 50 × 2 ÷ 2 = 50"
        ]

    def test_basic_eqn_build(self):
        # test data 1
        self.builder.write_number(99)
        self.builder.write_addition()
        self.builder.write_number(1)

        self.builder.write_subtraction()
        self.builder.write_number(50)

        self.builder.write_multiplication()
        self.builder.write_number(2)

        self.builder.write_division()
        self.builder.write_number(2)

        self.builder.write_equality()
        self.builder.write_number(50)

        equation = self.builder.equation
        self.assertEqual(
            equation.full,
            self.test_data[0]
        )
        self.assertEqual(
            equation.left_side,
            "99 + 1 − 50 × 2 ÷ 2 ="
        )
        self.assertEqual(
            equation.right_side,
            "50"
        )

        self.builder.clear()

    def test_empty_equation(self):
        equation = self.builder.equation
        self.assertEqual(
            equation.full,
            ""
        )
