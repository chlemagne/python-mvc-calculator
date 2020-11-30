""" Command abstract module.
"""

import abc


class Command(abc.ABC):
    """ Command abstract class.
    """

    def __init__(self, num_builder, eq_builder, alu, display):
        self.num_builder = num_builder
        self.eq_builder = eq_builder
        self.alu = alu
        self.display = display

    @abc.abstractmethod
    def execute(self, arg):
        """ Execute.
        """
        pass
