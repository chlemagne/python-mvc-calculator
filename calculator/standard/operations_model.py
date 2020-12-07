""" Standard calculator operations model module.
"""

import abc
import math
import fractions
import decimal


class OperationABC(abc.ABC):
    """ Operation interface.
    """

    @abc.abstractstaticmethod
    def eval():
        """ Evaluate operation.
        """
        pass


class UniOperation(OperationABC):
    """ Uni-operand operation object category.
    """
    pass


class BiOperation(OperationABC):
    """ Bi-operand operation object category.
    """
    pass


class Square(UniOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x):
        """ Raise x to the 2nd power.
        """
        return x ** 2


class SquareRoot(UniOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x):
        """ Square root of x.
        """
        return math.sqrt(x)


class Reciprocal(UniOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x):
        """ Get reciprocal of x.
        """
        return 1 / x


class Add(BiOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x, y):
        """ Add x and y.
        """
        return x + y


class Subtract(BiOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x, y):
        """ Subtract y from x.
        """
        return x - y


class Multiply(BiOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x, y):
        """ Multiply x and y.
        """
        return x * y


class Divide(BiOperation):
    """ Concrete operation object.
    """

    PRECISION = 5

    @staticmethod
    def eval(x, y):
        """ Divide y from x.
        """
        decimal.getcontext().prec = Divide.PRECISION
        quotient = decimal.Decimal(x) / decimal.Decimal(y)
        return float(quotient)


class Modulo(BiOperation):
    """ Concrete operation object.
    """

    @staticmethod
    def eval(x, y):
        """ Modulo divide y from x.
        """
        return x % y
