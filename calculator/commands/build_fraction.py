""" Concrete implementation of a command.
"""

from calculator.interface import Command


class SetBuilderTypeToFractionCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        self.num_builder.set_build_target(
            self.num_builder.BuildTarget.FRACTION_PART)
        self.display.display(self.num_builder.number, self.eq_builder.equation)
