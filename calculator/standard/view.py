""" Standard calcualtor view module.
"""

import enum
from tkinter import Frame, Button, Entry, StringVar


class View(Frame):
    """ Standard calculator view object.
    """

    class Labels(enum.Enum):
        """ Standard calculator view component labels
        """
        # displays
        TOP_DISP = enum.auto()
        BOT_DISP = enum.auto()

        # numpad digits
        ZERO = "0"
        ONE = "1"
        TWO = "2"
        THREE = "3"
        FOUR = "4"
        FIVE = "5"
        SIX = "6"
        SEVEN = "7"
        EIGHT = "8"
        NINE = "9"
        SIGN_TGL = "+/-"
        DECIMAL_PT = "."

        # uni-operand operations
        RECIPROCAL = "1/x"
        SQUARE = "x²"
        SQR_ROOT = "√x"

        # bi-operand operations
        ADD = "+"
        SUBTRACT = "−"
        MULTIPLY = "×"
        DIVIDE = "÷"
        MODULO = "%"

        # others
        CE = "CE"
        CA = "CA"
        DEL = "DEL"
        EQ = "="

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.displays = {}
        self.buttons = {}

    def draw(self):
        """ Draw view.
        """
        self.pack()
        ###################################################
        # Create displays
        ###################################################
        config = {
            "width": 35,
            "borderwidth": 2,
            "justify": "right",
            "state": "disabled"
        }
        displays = [
            # label                  # row   # columnpsan
            # [self.Labels.TOP_DISP,   0,      4],
            [self.Labels.BOT_DISP,   1,      4]
        ]
        for display in displays:
            text_var = StringVar()
            label, row, columnspan = display  # unpack display
            entry = Entry(self, textvariable=text_var, **config)
            entry.grid(row=row, columnspan=columnspan)

            self.displays[label] = text_var

        ###################################################
        # Create buttons
        ###################################################
        config = {"padx": 15, "pady": 7}
        buttons = [
            # label                   # row   # column
            [self.Labels.MODULO,      2,      0],
            [self.Labels.CE,          2,      1],
            [self.Labels.CA,          2,      2],
            [self.Labels.DEL,         2,      3],
            [self.Labels.RECIPROCAL,  3,      0],
            [self.Labels.SQUARE,      3,      1],
            [self.Labels.SQR_ROOT,    3,      2],
            [self.Labels.DIVIDE,      3,      3],
            [self.Labels.SEVEN,       4,      0],
            [self.Labels.EIGHT,       4,      1],
            [self.Labels.NINE,        4,      2],
            [self.Labels.MULTIPLY,    4,      3],
            [self.Labels.FOUR,        5,      0],
            [self.Labels.FIVE,        5,      1],
            [self.Labels.SIX,         5,      2],
            [self.Labels.SUBTRACT,    5,      3],
            [self.Labels.ONE,         6,      0],
            [self.Labels.TWO,         6,      1],
            [self.Labels.THREE,       6,      2],
            [self.Labels.ADD,         6,      3],
            [self.Labels.SIGN_TGL,    7,      0],
            [self.Labels.ZERO,        7,      1],
            [self.Labels.DECIMAL_PT,  7,      2],
            [self.Labels.EQ,          7,      3]
        ]
        for button in buttons:
            label, row, column = button  # unpack button
            btn = Button(self, text=label.value, **config)
            btn.grid(row=row, column=column)

            self.buttons[label] = btn
