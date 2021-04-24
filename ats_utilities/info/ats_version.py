# -*- coding: UTF-8 -*-

'''
 Module
     ats_version.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     ats_utilities is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     ats_utilities is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class ATSVersion with attribute(s) and method(s).
     Created API for App/Tool/Script version in one property object.
'''

import sys

try:
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.7.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVersion:
    '''
        Defined class ATSVersion with attribute(s) and method(s).
        Created API for App/Tool/Script version in one property object.
        It defines:

            :attributes:
                | __metaclass__ - Setting verbose root for ATSVersion.
                | __verbose - Enable/disable verbose option.
                | __version - App/Tool/Script version.
            :methods:
                | __init__ - Initial constructor.
                | version - Property methods for set/get operations.
                | is_not_none - Checking is App/Tool/Script version None.
                | __str__ - Dunder method for ATSVersion.
    '''

    __metaclass__ = VerboseRoot

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__version = None

    @property
    def version(self):
        '''
            Property method for getting App/Tool/Script version.

            :return: App/Tool/Script version | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__version

    @version.setter
    def version(self, version):
        '''
            Property method for setting App/Tool/Script version.

            :param version: App/Tool/Script version.
            :type version: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:version', version)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__version = version
        verbose_message(ATSVersion.VERBOSE, self.__verbose, version)

    def is_not_none(self):
        '''
            Checking is App/Tool/Script version None.

            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self.__version)

    def __str__(self):
        '''
            Dunder method for ATSVersion.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), self.__version
        )