""" Window module.
"""

from tkinter import Tk
from .button import Button
from .two_line_display import TwoLineDisplay


class Window:
    """ Window class.
    """

    def __init__(self):
        self.__tk = Tk()
        self.__buttons = {}
        self.__display = None

    def show(self):
        """ Show unresizable window.
        """
        self.__tk.resizable(False, False)
        self.__tk.mainloop()

    def create_display(self):
        """ Create display object.
        """
        self.__display = TwoLineDisplay()
        self.__display.create(self.__tk)

    def create_button(self, label, command):
        """ Create button object.
        """
        if self.__buttons.get(label):
            return

        btn = Button(label, command)
        btn.create(self.__tk)

        self.__buttons[label] = btn

    def get_display(self):
        """ Return display object.
        """
        return self.__display

    def get_button(self, label):
        """ Retrieve button object.
        """
        return self.__buttons.get(label, None)
