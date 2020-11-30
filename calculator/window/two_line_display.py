""" Concrete implementation of display interface.
"""

from tkinter import Entry
from calculator.equation import Equation
from calculator.interface import DisplayInterface


class TwoLineDisplay(DisplayInterface):
    """ Display object containing top and bottom Tk entry objects.
    """

    def __init__(self):
        self.__top_disp = None
        self.__bot_disp = None

    def display(self, number, equation):
        """ Display equation object.
        """
        assert isinstance(equation, Equation)
        self.__write(self.__top_disp, equation.left_side)
        self.__write(self.__bot_disp, number if number else "")

    def create(self, tk):
        """ Create graphics object.
        :params tk: Tk Window root object. 
        """
        config = {
            "width": 35,
            "borderwidth": 2,
            "justify": "right",
            "state": "disabled"
        }
        self.__top_disp = Entry(tk, **config)
        self.__bot_disp = Entry(tk, **config)

    def draw(self, row=0, columnspan=4):
        """ Draw graphics object to screen.
        """
        self.__top_disp.grid(row=row, columnspan=columnspan)
        self.__bot_disp.grid(row=(row + 1), columnspan=columnspan)

    def __write(self, disp, text):
        """ Write text to Entry object.
        """
        disp.configure(state="normal")
        disp.delete(0, "end")
        disp.insert(0, text)
        disp.configure(state="disabled")
