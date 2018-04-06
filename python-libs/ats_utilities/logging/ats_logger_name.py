# -*- coding: UTF-8 -*-
# ats_logger_name.py
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
from inspect import stack

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerName(object):
    """
        Define class ATSLoggerName with attribute(s) and method(s).
        Logging mechanism for App/Tool/Script.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __logger_name - Logger name
            method:
                __init__ - Initial constructor
                set_logger_name - Setting logger name
                get_logger_name - Getting logger name
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_LOGGER_NAME'

    def __init__(self, logger_name=None, verbose=False):
        """
            Initial constructor.
            :param logger_name: Logger name
            :type logger_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = ATSLoggerName
        verbose_message(cls.VERBOSE, verbose, 'Initial ATS logger Name')
        self.__logger_name = logger_name

    def set_logger_name(self, logger_name, verbose=False):
        """
            Setting logger name.
            :param logger_name: Logger name
            :type logger_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = ATSLoggerName, stack()[0][3]
        logger_name_txt = 'Argument: expected logger_name <str> object'
        logger_name_msg = "{0} {1} {2}".format(
            cls.VERBOSE, func, logger_name_txt
        )
        if logger_name is None or not logger_name:
            raise ATSBadCallError(logger_name_msg)
        if not isinstance(logger_name, str):
            raise ATSTypeError(logger_name_msg)
        verbose_message(
            cls.VERBOSE, verbose, 'Set ATS logger name', logger_name
        )
        self.__logger_name = logger_name

    def get_logger_name(self, verbose=False):
        """
            Getting logger name.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Logger name
            :rtype: <str>
        """
        cls = ATSLoggerName
        verbose_message(
            cls.VERBOSE, verbose, 'ATS logger name', self.__logger_name
        )
        return self.__logger_name

    def __str__(self):
        """
            Return human readable string (ATSLoggerName).
            :return: String representation of ATSLoggerName
            :rtype: <str>
        """
        cls = ATSLoggerName
        return "{0} Logger name {1}".format(cls.__name__, self.__logger_name)

    def __repr__(self):
        """
            Return unambiguous string (ATSLoggerName).
            :return: String representation of ATSLoggerName
            :rtype: <str>
        """
        cls = ATSLoggerName
        return "{0}(\'{1}\')".format(cls.__name__, self.__logger_name)
