""" Concrete implementation of a command.
"""

from calculator.interface import Command


class BuildNumberCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        self.num_builder.append(arg)
        self.eq_builder.write_number(self.num_builder.number)

        self.display.display(self.num_builder.number, self.eq_builder.equation)
