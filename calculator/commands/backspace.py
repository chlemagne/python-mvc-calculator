""" Concrete implementation of a command.
"""

from calculator.interface import Command


class BackspaceCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        self.num_builder.backspace()

        self.display.display(self.num_builder.number, self.eq_builder.equation)
