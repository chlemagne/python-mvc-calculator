""" Standard calculator input number module.
"""

import math
import enum
from collections import deque


class NumberModel:
    """ Standard calculator input number object.
    """

    class Symbols(enum.Enum):
        ZERO = "0"
        ONE = "1"
        TWO = "2"
        THREE = "3"
        FOUR = "4"
        FIVE = "5"
        SIX = "6"
        SEVEN = "7"
        EIGHT = "8"
        NINE = "9"
        NEGATIVE = "-"
        DECIMAL_PT = "."

    def __init__(self):
        self._appended = False
        self._digits = deque([self.Symbols.ZERO.value])

    def new(self):
        """ Create a new number.
        """
        self._digits.clear()
        self._appended = False
        self._digits.append(self.Symbols.ZERO.value)

    def append(self, symbol):
        """ Append NumberModel.Symbol to number.
        """
        assert isinstance(symbol, self.Symbols)

        # replace (default) initial zero (0) value.
        # this does not apply when appending a decimal point
        if (self._is_zero()) and (symbol != self.Symbols.DECIMAL_PT):
            self._digits.pop()

        # number should only contain one decimal point
        if (self._digits.count(self.Symbols.DECIMAL_PT.value) > 0) and\
                (symbol is self.Symbols.DECIMAL_PT):
            return

        self._appended = True
        self._digits.append(symbol.value)

    def backspace(self):
        """ Delete last added digit.
        """
        if self._is_zero():
            return

        is_one_digit_pos = len(self._digits) == 1 and\
            (self._digits[0] != self.Symbols.ZERO.value)

        is_one_digit_neg = len(self._digits) == 2 and\
            (self._digits[0] == self.Symbols.NEGATIVE.value)

        if is_one_digit_pos or is_one_digit_neg:
            self.new()
            return

        self._digits.pop()

    def change_sign(self):
        """ Change sign from positive to negative, and vice versa.
        """
        if self._is_zero():
            return

        if self._digits[0] != self.Symbols.NEGATIVE.value:
            self._digits.appendleft(self.Symbols.NEGATIVE.value)
        else:
            self._digits.popleft()

    def join(self):
        """ Join digits and return as string.
        """
        return "".join(self._digits)

    def is_appended(self):
        """ Return true if a value, zero or non-zero, has been appended.
        """
        return self._appended

    def _is_zero(self):
        """ Return True if number is zero (initial value).
        """
        return (len(self._digits) == 1) and\
            (self._digits[0] == self.Symbols.ZERO.value)
