""" Main calculator controller interface module.
"""

from calculator.view import MainView
from calculator.standard import StandardCalculatorController


class MainController:
    """ Main calculator controller object.
    """

    def __init__(self):
        self.view = MainView()
        self.calculator = StandardCalculatorController(self.view)

    def main(self):
        """ Main loop.
        """
        # disable resizing of window
        self.view.resizable(False, False)

        # set window title and icon
        self.view.wm_title(self.calculator.name)
        self.view.wm_iconbitmap(self.view.ICON_FILEPATH)

        # run calculator main
        self.calculator.main()

        # run parent view mainloop
        self.view.mainloop()
