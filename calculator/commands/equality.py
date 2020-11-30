""" Concrete implementation of a command.
"""

from calculator.interface import Command


class EqualityCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        # get collected number, as operand, from builder
        operand = self.num_builder.number

        # increment feature: successive equality presses
        if self.num_builder.number is not None:
            self.num_builder.clear()
            self.alu.push(operand)

        # compute
        result = self.alu.compute()

        # append to equation and result
        self.eq_builder.write_equality()
        self.eq_builder.write_number(result)

        self.display.display(result, self.eq_builder.equation)
