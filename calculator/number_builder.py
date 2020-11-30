""" Number builder module.
"""

import enum
from collections import deque


class NumberBuilder:
    """ Receives single digit to build whole and decimal (fraction) numbers.
    """

    class BuildTarget(enum.Enum):
        """ NumberBuilder build target.
        """
        WHOLE_PART = enum.auto()
        FRACTION_PART = enum.auto()

    def __init__(self):
        self.__is_positive = True
        self.__whole_digits = deque([])
        self.__fraction_digits = deque([])
        self.__target = self.BuildTarget.WHOLE_PART

    @property
    def number(self):
        """ Return whole and decimal number.
        """
        if self.__is_empty():
            return None

        whole = 0
        num_whole_digits = len(self.__whole_digits) - 1
        for place_value, digit in enumerate(self.__whole_digits):
            whole += digit * self.__power_of_10(num_whole_digits - place_value)

        fraction = 0.0
        for place_value, digit in enumerate(self.__fraction_digits):
            fraction += digit / self.__power_of_10(place_value + 1)

        # combine whole and fraction
        full = whole + (fraction if fraction != 0.0 else 0)
        return (full) if (self.__is_positive) else (-1 * full)

    def clear(self):
        """ Reset to zero.
        """
        self.__whole_digits = deque([])
        self.__fraction_digits = deque([])
        self.__is_positive = True
        self.__target = self.BuildTarget.WHOLE_PART

    def set_build_target(self, target):
        """ Change build target to NumberBuilder.BuildTarget.WHOLE_PART or
        NumberBuilder.BuildTarget.FRACTION_PART.
        """
        assert isinstance(target, self.BuildTarget)
        self.__target = target

    def toggle_sign(self):
        """ Toggle number from positive to negative, and vice versa.
        """
        self.__is_positive = not self.__is_positive

    def backspace(self):
        """ Delete last digit.
        """
        if len(self.__whole_digits) < 1:
            self.__is_positive = True
            return

        if self.__is_target_whole_part():
            self.__whole_digits.pop()

        else:
            self.__fraction_digits.pop()
            if len(self.__fraction_digits) < 1:
                self.__target = self.BuildTarget.WHOLE_PART

    def append(self, digit):
        """ Append digit into the number.
        """
        if self.__is_target_whole_part():
            self.__whole_digits.append(int(digit))

        else:
            self.__fraction_digits.append(float(digit))

    def __is_target_whole_part(self):
        """ Return True if build target is set to
        NumberBuilder.BuildTarget.WHOLE_PART.
        """
        return self.__target == self.BuildTarget.WHOLE_PART

    def __power_of_10(self, nth):
        """ Return 10 raise to nth power.
        """
        return 10 ** nth

    def __is_empty(self):
        """ Return true if no digit had been appended to the builder.
        """
        return (len(self.__whole_digits) < 1) and\
            (len(self.__fraction_digits) < 1)
