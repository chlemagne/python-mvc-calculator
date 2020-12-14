""" Standard calculator controller module.
"""

from .view import View
from .number_model import NumberModel
from .operands_model import OperandsModel
from calculator.abc import ControllerInterface
from .operations_model import (
    OperationABC,
    UniOperation,
    BiOperation,
    Square,
    SquareRoot,
    Reciprocal,
    Add,
    Subtract,
    Multiply,
    Divide,
    Modulo
)


class Controller(ControllerInterface):
    """ Standard calcualtor controller object.
    """

    def __init__(self, parent):
        self.result = None  # stores the last result when pressing the equal button
        self.operation = None
        self.view = View(parent)
        self.number = NumberModel()
        self.operands = OperandsModel()

    @property
    def name(self):
        """ Return calculator name.
        """
        return "Standard Calculator"

    def main(self):
        """ Run standard calculator controller.
        """
        self.view.draw()
        self.top_disp = self.view.displays.get(self.view.Labels.TOP_DISP)
        self.bot_disp = self.view.displays.get(self.view.Labels.BOT_DISP)

        # set initial bottom display to zero (0)
        self.bot_disp.set(self.number.join())

        # bind button callback functions
        label_callbacks = [
            [self.view.Labels.ONE,          self._press_one],
            [self.view.Labels.TWO,          self._press_two],
            [self.view.Labels.THREE,        self._press_three],
            [self.view.Labels.FOUR,         self._press_four],
            [self.view.Labels.FIVE,         self._press_five],
            [self.view.Labels.SIX,          self._press_six],
            [self.view.Labels.SEVEN,        self._press_seven],
            [self.view.Labels.EIGHT,        self._press_eight],
            [self.view.Labels.NINE,         self._press_nine],
            [self.view.Labels.ZERO,         self._press_zero],
            [self.view.Labels.SIGN_TGL,     self._press_change_sign],
            [self.view.Labels.DECIMAL_PT,   self._press_decimal_point],
            [self.view.Labels.DEL,          self._press_backspace],
            [self.view.Labels.CE,           self._press_clear_entry],
            [self.view.Labels.CA,           self._press_clear_all],
            [self.view.Labels.ADD,          self._press_add],
            [self.view.Labels.SUBTRACT,     self._press_subtract],
            [self.view.Labels.MULTIPLY,     self._press_multiply],
            [self.view.Labels.DIVIDE,       self._press_divide],
            [self.view.Labels.EQ,           self._press_equals],
        ]
        for entry in label_callbacks:
            label, callback = entry
            btn = self.view.buttons.get(label)
            btn.bind("<Button-1>", callback)

    def _update_display(self, label, text):
        """ Update display with value text.
        """
        display = self.view.displays.get(label)
        display.set(text)

    def _press_one(self, event):
        """ Call back method for button ONE.
        """
        self.number.append(self.number.Symbols.ONE)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_two(self, event):
        """ Call back method for button TWO.
        """
        self.number.append(self.number.Symbols.TWO)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_three(self, event):
        """ Call back method for button THREE.
        """
        self.number.append(self.number.Symbols.THREE)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_four(self, event):
        """ Call back method for button FOUR.
        """
        self.number.append(self.number.Symbols.FOUR)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_five(self, event):
        """ Call back method for button FIVE.
        """
        self.number.append(self.number.Symbols.FIVE)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_six(self, event):
        """ Call back method for button SIX.
        """
        self.number.append(self.number.Symbols.SIX)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_seven(self, event):
        """ Call back method for button SEVEN.
        """
        self.number.append(self.number.Symbols.SEVEN)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_eight(self, event):
        """ Call back method for button EIGHT.
        """
        self.number.append(self.number.Symbols.EIGHT)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_nine(self, event):
        """ Call back method for button NINE.
        """
        self.number.append(self.number.Symbols.NINE)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_zero(self, event):
        """ Call back method for button ZERO.
        """
        self.number.append(self.number.Symbols.ZERO)
        self._update_display(
            self.view.Labels.BOT_DISP,
            self.number.join()
        )

    def _press_change_sign(self, event):
        """ Call back method for button CHANGE SIGN.
        """
        self.number.change_sign()
        number = self.number.join()

        self._update_display(self.view.Labels.BOT_DISP, number)

    def _press_decimal_point(self, event):
        """ Call back method for button DECIMAL POINT.
        """
        symbol = self.number.Symbols.DECIMAL_PT
        self.number.append(symbol)
        number = self.number.join()

        self._update_display(self.view.Labels.BOT_DISP, number)

    def _press_backspace(self, event):
        """ Call back method for button DEL.
        """
        self.number.backspace()
        number = self.number.join()

        self._update_display(self.view.Labels.BOT_DISP, number)

    def _press_clear_entry(self, event):
        """ Call back method for button CE.
        """
        self.number.new()
        number = self.number.join()

        self._update_display(self.view.Labels.BOT_DISP, number)

    def _press_clear_all(self, event):
        """ Call back method for button CE.
        """
        self.number.new()
        self.result = None
        self.operands.clear()
        self.operation = None
        number = self.number.join()

        self._update_display(self.view.Labels.BOT_DISP, number)

    def _press_add(self, event):
        """ Call back method for button ADD.
        """
        self._perform_bi_operand_operation(Add)

    def _press_subtract(self, event):
        """ Call back method for button SUBTRACT.
        """
        self._perform_bi_operand_operation(Subtract)

    def _press_multiply(self, event):
        """ Call back method for button MULTIPLY.
        """
        self._perform_bi_operand_operation(Multiply)

    def _press_divide(self, event):
        """ Call back method for button DIVIDE.
        """
        self._perform_bi_operand_operation(Divide)

    def _perform_bi_operand_operation(self, operation):
        """ Perform a bi-operand operation.
        """
        # scenario when pressing an operation button after equal button has been pressed
        if self.result is not None:
            self.operands.clear()
            # scenario when after pressing equals, a number has been entered
            if self.number.is_appended():
                self.operands.push(self.number.join())
                self.number.new()
            # scenario when after pressing equals, an operation had been pressed
            else:
                self.operands.push(self.result)
                self.result = None

        # normal scenario
        else:
            self.operands.push(self.number.join())
            self.number.new()

        if (self.operands.count() == 2) and (self.operation is not None):
            x = self.operands.get(0)
            y = self.operands.get(1)
            decimal_pt = self.number.Symbols.DECIMAL_PT.value
            x = float(x) if (decimal_pt in x) else int(x)
            y = float(y) if (decimal_pt in y) else int(y)

            result = self.operation.eval(x, y)

            self.operands.clear()
            self.operands.push(result)
            self._update_display(self.view.Labels.BOT_DISP, result)

        self.operation = operation

    def _press_equals(self, event):
        """ Call back method for button EQUAL.
        """
        if self.operation is None:
            return

        if issubclass(self.operation, BiOperation):
            number = self.number.join() if self.number.is_appended() else self.operands.get(0)
            self.number.new()
            self.operands.push(number)

            x = self.operands.get(0)
            y = self.operands.get(1)
            self.operands.clear()
            # cast to either int or float
            decimal_pt = self.number.Symbols.DECIMAL_PT.value
            x = float(x) if (decimal_pt in x) else int(x)
            y = float(y) if (decimal_pt in y) else int(y)

            x = self.operation.eval(x, y)
            self.result = x
            self.operands.push(x)
            self.operands.push(y)
            self._update_display(self.view.Labels.BOT_DISP, x)
