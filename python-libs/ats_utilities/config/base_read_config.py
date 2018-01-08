# -*- coding: UTF-8 -*-
# base_read_config.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from abc import ABCMeta, abstractmethod

try:
    from ats_utilities.text.stdout_text import DBG, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseReadConfig(object):
    """
    Define class BaseReadConfig with attribute(s) and method(s).
    Class for read operation (configuration).
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __file_path - Configuration file path
        method:
            __init__ - Initial constructor
            set_file_path - Setting configuration file path
            get_file_path - Getting configuration file path
            read_configuration - Read configuration from file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = 'BASE_READ_CONFIG'

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
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :param file_path: Configuration file path
        :type file_path: <str>
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
    def read_configuration(self, verbose=False):
        """
        Read configuration from file (Abstract method).
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: Configuration object
        :rtype: <Python object(s)> | <NoneType>
        """
        pass

    def __str__(self):
        """
        Return human readable string (BaseReadConfig).
        :return: String representation of BaseReadConfig
        :rtype: <str>
        """
        return "File path {0}".format(self.__file_path)

    def __repr__(self):
        """
        Return unambiguous string (BaseReadConfig).
        :return: String representation of BaseReadConfig
        :rtype: <str>
        """
        return "{0}()".format(type(self).__name__)
