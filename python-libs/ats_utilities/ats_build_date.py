# -*- coding: UTF-8 -*-
# ats_build_date.py
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
    from ats_utilities.console_io.error import Error
    from ats_utilities.console_io.verbose import Verbose
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class ATSBuildDate(object):
    """
        Define class ATSBuildDate with attribute(s) and method(s).
        Keep, set, get build date of App/Tool/Script.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __build_date - Build date of App/Tool/Script
            method:
                __init__ - Initial constructor
                set_ats_build_date - Setting build date of App/Tool/Script
                get_ats_build_date - Getting build date of App/Tool/Script
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_UTILITIES::ATS_BUILD_DATE]'

    def __init__(self, build_date=None, verbose=False):
        """
            Initial build date of App/Tool/Script.
            :param build_date: Build date of App/Tool/Script | None
            :type build_date: <str> | <NoneType>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        if verbose:
            ver = Verbose()
            ver.message = "{0}".format('Initial build date')
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        self.__build_date = build_date

    def set_ats_build_date(self, build_date, verbose=False):
        """
            Setting build date of App/Tool/Script.
            :param build_date: Build date of App/Tool/Script
            :type build_date: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = self.__class__, stack()[0][3], False
        if build_date is None:
            txt = 'Argument: missing build_date <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(build_date, str):
            txt = 'Argument: expected build_date <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        self.__build_date = build_date

    def get_ats_build_date(self, verbose=False):
        """
            Getting build date of App/Tool/Script.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Build date of App/Tool/Script | None
            :rtype: <str> | <NoneType>
        """
        return self.__build_date

    def __str__(self):
        """
            Return human readable string (ATSBuildDate).
            :return: String representation of ATSBuildDate
            :rtype: <str>
        """
        return "{0} build date {1}".format(self.__class__, self.__build_date)

    def __repr__(self):
        """
            Return unambiguous string (ATSBuildDate).
            :return: String representation of ATSBuildDate
            :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__build_date)
