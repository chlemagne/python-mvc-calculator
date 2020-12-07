""" Standard calculator operands model module.
"""

from collections import deque


class OperandsModel:
    """ Standard calculator operands model object.
    """

    def __init__(self):
        self._pushed_zero = False
        self._operands = deque(["0"])  # operands initially contains zero (0)

    @property
    def operands(self):
        """ Operands.
        """
        return self._operands

    def get(self, index):
        """ Return operand at index.
        """
        return str(self.operands[index])

    def count(self):
        """ Return the number of operands.
        """
        return len(self.operands)

    def clear(self):
        """ Clear operands.
        """
        self.__init__()

    def push(self, value):
        """ Push operand value.
        """
        if value == "0":
            self._pushed_zero = True
            return

        if (len(self.operands) == 1) and\
                (self.operands[0] == "0") and\
                (not self._pushed_zero):
            self.operands.pop()

        self.operands.append(str(value))
