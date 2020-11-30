""" Equation module.
"""


class Equation:
    """ Equation class.
    """

    def __init__(self, left_side="", right_side=""):
        self.__left_side = left_side
        self.__right_side = right_side

    def __str__(self):
        return self.full

    @property
    def left_side(self):
        """ Return the left side of the equation including the equal sign (=).
        """
        return self.__left_side

    @property
    def right_side(self):
        """ Return the right side of the equation, representing the result.
        """
        return self.__right_side

    @property
    def full(self):
        """ Return the full equation containing both the left and right side.
        """
        if (self.left_side == "") and (self.right_side == ""):
            return ""

        return f"{self.left_side} {self.right_side}"
