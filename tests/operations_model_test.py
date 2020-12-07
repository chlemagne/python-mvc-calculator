""" Unittest.
"""

import unittest
from calculator.standard.operations_model import (
    UniOperation,
    BiOperation,
    Square,
    SquareRoot,
    Reciprocal,
    Add,
    Subtract,
    Multiply,
    Divide,
    Modulo
)


class OperationsModelTest(unittest.TestCase):
    """ Operations model test suite.
    """

    def test_operation_category(self):
        # steps
        square = Square
        multiply = Multiply

        # test
        self.assertTrue(issubclass(square, UniOperation))
        self.assertTrue(issubclass(multiply, BiOperation))

    def test_uni_operand_operations(self):
        # steps
        square = Square
        square_root = SquareRoot

        # test
        self.assertEqual(square.eval(5), 25)
        self.assertEqual(square_root.eval(25), 5)

    def test_bi_operand_operations(self):
        # steps
        add = Add
        sub = Subtract
        mul = Multiply
        div = Divide

        # test
        self.assertEqual(add.eval(1, 2), 3)
        self.assertEqual(sub.eval(5, -2), 7)
        self.assertEqual(mul.eval(1.5, -5), -7.5)
        self.assertEqual(div.eval(6, 0.5), 12)
