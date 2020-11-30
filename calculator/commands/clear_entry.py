""" Concrete implementation of a command.
"""

from calculator.interface import Command


class ClearEntryCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        self.num_builder.clear()
        self.display.display(self.num_builder.number, self.eq_builder.equation)
