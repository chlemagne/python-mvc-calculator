""" Unittest.
"""

import unittest
from calculator.standard.operands_model import OperandsModel


class OperandsModelTest(unittest.TestCase):
    """ Operands model test suite.
    """

    def test_initial_operand(self):
        # steps
        model = OperandsModel()
        initial_operand = model.get(0)

        # test
        self.assertEqual(initial_operand, "0")

    def test_first_operand_push(self):
        # test data
        test_value = "1"

        # steps
        model = OperandsModel()
        model.push(test_value)
        operands_count = model.count()

        # test
        self.assertEqual(operands_count, 1)
        self.assertEqual(model.get(0), test_value)

    def test_second_operand_push(self):
        # test data
        test_data = ["5", "10"]

        # steps
        model = OperandsModel()
        for data in test_data:
            model.push(data)
        operands_count = model.count()

        self.assertEqual(operands_count, 2)
        self.assertEqual(model.get(0), test_data[0])
        self.assertEqual(model.get(1), test_data[1])
