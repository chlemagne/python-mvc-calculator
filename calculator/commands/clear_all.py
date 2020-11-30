""" Concrete implementation of a command.
"""

from calculator.interface import Command


class ClearAllCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        self.num_builder.clear()
        self.eq_builder.clear()
        self.alu.clear()

        self.display.display(self.num_builder.number, self.eq_builder.equation)
