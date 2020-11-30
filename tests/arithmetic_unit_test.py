""" Unit test module.
"""

import unittest
from calculator.arithmetic_unit import ArithmeticUnit


class ArithmeticUnitTest(unittest.TestCase):
    """ Testcase.
    """

    def setUp(self):
        self.au = ArithmeticUnit()

    def test_add(self):
        self.au.push(3)
        self.au.push(4)
        self.au.instruct(lambda x, y: x+y)
        self.assertEqual(self.au.compute(), (3+4))

    def test_subract(self):
        self.au.push(3)
        self.au.push(4)
        self.au.instruct(lambda x, y: x-y)
        self.assertEqual(self.au.compute(), (3-4))

    def test_multiply(self):
        self.au.push(3)
        self.au.push(4)
        self.au.instruct(lambda x, y: x*y)
        self.assertEqual(self.au.compute(), (3*4))

    def test_divides(self):
        self.au.push(3)
        self.au.push(4)
        self.au.instruct(lambda x, y: x/y)
        self.assertEqual(self.au.compute(), (3/4))

    def test_combinational_operation(self):
        # sequence: 12 + 12 - 4 * 3 / 10 = 6
        self.au.push(12)
        self.au.push(12)
        # 1
        self.au.instruct(lambda x, y: x+y)
        self.assertEqual(self.au.compute(), 24)
        # 2
        self.au.instruct(lambda x, y: x-y)
        self.au.push(4)
        self.assertEqual(self.au.compute(), 20)
        # 3
        self.au.instruct(lambda x, y: x*y)
        self.au.push(3)
        self.assertEqual(self.au.compute(), 60)
        # 4
        self.au.instruct(lambda x, y: x/y)
        self.au.push(10)
        self.assertEqual(self.au.compute(), 6)  # final result

    def test_successive_multiply(self):
        self.au.push(2)
        self.au.push(2)
        self.au.instruct(lambda x, y: x*y)
        self.assertEqual(self.au.compute(), 4)
        self.assertEqual(self.au.compute(), 8)
        self.assertEqual(self.au.compute(), 16)
        self.assertEqual(self.au.compute(), 32)

    def test_no_operand(self):
        self.au.instruct(lambda x, y: x+y)
        self.assertEqual(self.au.compute(), 0)
        self.assertEqual(self.au.compute(), 0)

    def test_single_operand(self):
        self.au.push(2)
        self.au.instruct(lambda x, y: x+y)
        self.assertEqual(self.au.compute(), 4)
        self.assertEqual(self.au.compute(), 6)
        self.assertEqual(self.au.compute(), 8)
        self.assertEqual(self.au.compute(), 10)
