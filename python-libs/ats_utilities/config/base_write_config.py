# -*- coding: utf-8 -*-

import sys
from abc import ABCMeta, abstractmethod

try:
    from ats_utilities.text.stdout_text import DBG, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseWriteConfig(object):
    """
    Define class BaseWriteConfig with attribute(s) and method(s).
    Class for write operation (configuration).
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __file_path - Configuration file path
        method:
            __init__ - Initial constructor
            set_file_path - Setting configuration file path
            get_file_path - Getting configuration file path
            write_configuration - Write configuration to file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = 'BASE_WRITE_CONFIG'

    def __init__(self, verbose=False):
        """
        Initial file path.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Initial configuration file path')
        COut.print_console_msg(msg, verbose=verbose)
        self.__file_path = None

    def set_file_path(self, file_path, verbose=False):
        """
        Setting configuration file path.
        :param file_path: Configuration file path
        :type file_path: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0}\n{1}".format('Setting configuration file path', file_path)
        COut.print_console_msg(msg, verbose=verbose)
        self.__file_path = file_path

    def get_file_path(self, verbose=False):
        """
        Getting configuration file path.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: Configuration file path | None
        :rtype: <str> | <NoneType>
        """
        msg = "{0}\n{1}".format(
            'Getting configuration file path', self.__file_path
        )
        COut.print_console_msg(msg, verbose=verbose)
        return self.__file_path

    @abstractmethod
    def write_configuration(self, configuration, verbose=False):
        """
        Write configuration to file (Abstract method).
        :param configuration: Configuration object
        :type configuration: <dict>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (success) | False
        :rtype: <bool>
        """
        pass

    def __str__(self):
        """
        Return human readable string (BaseWriteConfig).
        :return: String representation of BaseWriteConfig
        :rtype: <str>
        """
        return "File path {0}".format(self.__file_path)

    def __repr__(self):
        """
        Return unambiguous string (BaseWriteConfig).
        :return: String representation of BaseWriteConfig
        :rtype: <str>
        """
        return "{0}()".format(type(self).__name__)
