""" Concrete implementation of a command.
"""

from calculator.interface import Command


class AdditionCommand(Command):
    """ Command class.
    """

    def execute(self, arg):
        """ Execute.
        """
        # prevent successive presses of the same math operation
        if self.num_builder.number is None:
            self.eq_builder.write_addition()
            self.display.display(self.alu.result, self.eq_builder.equation)
            self.alu.instruct(lambda x, y: x + y)
            return

        # append to equation
        self.eq_builder.write_addition()

        # get collected number, as operand, from builder
        operand = self.num_builder.number
        self.num_builder.clear()
        self.alu.push(operand)

        number = operand
        if (self.alu.first is not None) and (self.alu.second is not None):
            number = self.alu.compute()

        self.display.display(number, self.eq_builder.equation)

        # set next instruction
        self.alu.instruct(lambda x, y: x + y)
