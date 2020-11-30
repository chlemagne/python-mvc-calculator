""" Display interface module.
"""

import abc


class DisplayInterface(abc.ABC):
    """ Display interface class.
    """

    @abc.abstractmethod
    def display(self, number, equation):
        """ Display equation object.
        """
        # assert equation is an Equation object
        pass
