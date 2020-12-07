""" Main calculator view interface module.
"""

import os
from tkinter import Tk
from calculator import BASE_DIR


class MainView(Tk):
    """ Main calculator view object.
    """

    ICON_FILEPATH = os.path.join(BASE_DIR, "assets", "calculator.ico")

    def __init__(self):
        Tk.__init__(self)
