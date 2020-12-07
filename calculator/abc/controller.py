""" Application controller interface module.
"""

import abc


class ControllerInterface(abc.ABC):
    """ Application controller abstract class.
    """

    @abc.abstractproperty
    def name(self):
        """ Return calculator name.
        """
        pass

    @abc.abstractmethod
    def main(self):
        """ Run controller.
        """
        pass
