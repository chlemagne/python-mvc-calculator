""" Equation builder module.
"""

from calculator.equation import Equation
from calculator.symbol import CalculatorSymbol


class EquationBuilder:
    """ Receives numbers (e.g. whole, fraction, positive, negative) and math operator symbols to
    build an Equation object.
    """

    class IllegalStateException(Exception):
        pass

    def __init__(self):
        self.__equation = []

    @property
    def equation(self):
        """ Return Equation object.
        """
        if self.__equation_is_empty():
            return Equation()

        if self.__is_equation_complete():
            start_pos = 0
            eq_sign_pos = self.__equation.index(CalculatorSymbol.EQ.value) + 1
            # slice equation
            expression = " ".join(self.__equation[start_pos:eq_sign_pos])
            result = self.__get_last()

            return Equation(left_side=expression, right_side=result)

        # incomplete equation means no result in the right side
        else:
            return Equation(left_side=" ".join(self.__equation))

    def clear(self):
        """ Clear equation.
        """
        self.__equation = []

    def write_number(self, number):
        """ Write number into the equation.
        """
        num_string = str(number)
        if self.__last_is_number():
            self.__replace_last(num_string)

        else:
            self.__equation.append(num_string)

    def write_addition(self):
        """ Write addition symbol to the equation.
        """
        self.__write_operation_symbol(CalculatorSymbol.ADD.value)

    def write_subtraction(self):
        """ Write subtraction symbol to the equation.
        """
        self.__write_operation_symbol(CalculatorSymbol.SUBTRACT.value)

    def write_multiplication(self):
        """ Write multiplication symbol to the equation.
        """
        self.__write_operation_symbol(CalculatorSymbol.MULTIPLY.value)

    def write_division(self):
        """ Write division symbol to the equation.
        """
        self.__write_operation_symbol(CalculatorSymbol.DIVIDE.value)

    def write_equality(self):
        """ Write equality symbol to the equation.
        """
        # ignored conditions
        if (CalculatorSymbol.EQ.value in self.__equation) or\
           (self.__last_is_equal_sign()) or\
           (self.__last_is_arithmetic()):
            # below are invalid equations:
            #   1.)     1 + 2 = 3 =
            #   2.)     50 / 2 = =
            #   3.)     78 / =
            return

        self.__equation.append(CalculatorSymbol.EQ.value)

    def __write_operation_symbol(self, symbol):
        """ Write math operatiol to the equation.
        """
        # ignore conditions
        if (CalculatorSymbol.EQ.value in self.__equation) or\
           (self.__last_is_equal_sign()):
            # below are invalid equations
            #   1.)     1 + 2 = 3 -
            #   2.)     100 * 2 = +
            return

        if self.__last_is_number():
            self.__equation.append(symbol)

        elif self.__last_is_arithmetic():
            self.__replace_last(symbol)

    def __last_is_equal_sign(self):
        """ Return True if last entry to the equation is an equal (=) sign.
        """
        return self.__get_last() == CalculatorSymbol.EQ.value

    def __last_is_arithmetic(self):
        """ Return True if last entry to the equation is a math operation
        (e.g. add, subtract, multiply, divide).
        """
        return self.__get_last() in [
            CalculatorSymbol.ADD.value,
            CalculatorSymbol.SUBTRACT.value,
            CalculatorSymbol.MULTIPLY.value,
            CalculatorSymbol.DIVIDE.value
        ]

    def __last_is_number(self):
        """ Return True if last entry to the equation is a number.
        """
        return (not self.__last_is_equal_sign()) and\
            (not self.__last_is_arithmetic())

    def __equation_is_empty(self):
        """ Return True if equation is empty.
        """
        return len(self.__equation) < 1

    def __get_last(self):
        """ Return last entry to the equation.
        """
        return None if self.__equation_is_empty() else self.__equation[-1]

    def __replace_last(self, value):
        """ Replace last entry to the equation.
        """
        if not self.__equation_is_empty():
            self.__equation.pop()

        self.__equation.append(value)

    def __is_equation_complete(self):
        """ Return True if equation contains both expression and result.
        Example is ``10 + 1 = 11``.
        """
        return (len(self.__equation) >= 3) and\
            (self.__equation[-2] == CalculatorSymbol.EQ.value)
