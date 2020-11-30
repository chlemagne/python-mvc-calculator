""" Concrete implementation of the Arithmetic Unit object.
"""

from calculator.symbol import CalculatorSymbol


class ArithmeticUnit:
    """ Arithmetic unit class.
    """

    class OperandPair:
        """ Two operands.
        """

        MAX_COUNT = 2

        def __init__(self):
            self.__ix = 0                   # index
            self.__cqrray = [None, None]    # circular array

        def __str__(self):
            return str(self.__cqrray)

        @property
        def first(self):
            """ Return first operand.
            """
            try:
                return self.__cqrray[0]
            except IndexError:
                return None

        @property
        def second(self):
            """ Return second operand.
            """
            try:
                return self.__cqrray[1]
            except IndexError:
                return None

        def push(self, value):
            """ Append right.
            """
            self.__cqrray[self.__ix] = value
            self.__ix += 1
            self.__ix %= self.MAX_COUNT

        def pushleft(self, value):
            """ Append left.
            """
            self.__cqrray[0] = value
            self.__ix = 1

    def __init__(self):
        self.__result = None
        self.__instruction = None
        self.__op = self.OperandPair()

    @property
    def first(self):
        """ Return first operand.
        """
        return self.__op.first

    @property
    def second(self):
        """ Return second operand.
        """
        return self.__op.second

    @property
    def result(self):
        """ Return previous computed result.
        """
        return self.__result

    def clear(self):
        """ Clear first and second operands.
        """
        self.__result = None
        self.__instruction = None
        self.__op = self.OperandPair()

    def push(self, value):
        """ Push value into the register for operation.
        """
        self.__op.push(value)

    def instruct(self, func):
        """ Set arithmetic operation.
        :params func: lambda function
        """
        self.__instruction = func

    def compute(self):
        """ Apply instruction to values in register.
        """
        # special case if first operand is not given
        if self.first is None:
            self.__op.pushleft(0)

        # special case if second operand is not given
        if (self.second is None):
            self.__op.push(self.first)

        self.__result = self.__instruction(self.first, self.second)
        self.__op.pushleft(self.__result)
        return self.__result
