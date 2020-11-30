""" Concrete implementation of a command.
"""

from calculator.interface import Command


class ChangeSignCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        self.num_builder.toggle_sign()
        self.eq_builder.write_number(self.num_builder.number)

        self.display.display(self.num_builder.number, self.eq_builder.equation)
