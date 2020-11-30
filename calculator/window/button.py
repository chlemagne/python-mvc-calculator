""" Tk button module.
"""

from tkinter import Button as TkButton


class Button:
    """ Tk button application class.
    """

    def __init__(self, label, command):
        self.__label = label
        self.__button = None
        self.__command = command

    def create(self, tk):
        """ Create graphics object.
        :params tk: Tk Window root object.
        """
        config = {
            "padx": 15,
            "pady": 7
        }
        self.__button = TkButton(
            tk,
            text=self.__label,
            command=self.__click,
            **config
        )

    def draw(self, row, column):
        """ Draw graphics object to screen.
        """
        self.__button.grid(row=row, column=column)

    def __click(self):
        """ Call back method.
        """
        if self.__command:
            self.__command.execute(arg=self.__label)
