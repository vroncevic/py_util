# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class JsonBase with attribute(s) and method(s).
     Load ATS configuration/information, setup ATS CL interface.
'''

import sys

try:
    from ats_utilities import VerboseRoot
    from ats_utilities.info import ATSInfo
    from ats_utilities.checker import ATSChecker
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.json.json2object import Json2Object
    from ats_utilities.config_io.json.object2json import Object2Json
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


class JsonBase:
    '''
        Defined class JsonBase with attribute(s) and method(s).
        Load ATS configuration/information, setup ATS CL interface.
        It defines:

            :attributes:
                | __metaclass__ - Setting verbose root for JsonBase.
                | __verbose - Enable/disable verbose option.
                | tool_operational - Control ATS operational functionality.
                | json2obj - In API for informations.
                | obj2json - Out API for informations.
                | option_parser - Option parser for ATS.
            :methods:
                | __init__ - Initial constructor.
                | is_tool_ok - Checking is tool operational.
                | __str__ - Dunder method for object JsonBase.
    '''

    __metaclass__ = VerboseRoot

    def __init__(self, informations_file, verbose=False):
        '''
            Initial constructor.

            :param informations_file: Informations file path.
            :type informations_file: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:informations_file', informations_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__verbose = verbose
        informations = None
        self.tool_operational = False
        self.json2obj = Json2Object(informations_file, verbose=verbose)
        self.obj2json = Object2Json(informations_file, verbose=verbose)
        if all([self.json2obj, self.obj2json]):
            informations = self.json2obj.read_configuration(verbose=verbose)
        if informations:
            info = ATSInfo(informations, verbose=verbose)
            if info.ats_info_ok:
                self.option_parser = ATSOptionParser(
                    '{0} {1}'.format(info.name, info.build_date),
                    info.version, info.licence, verbose=verbose
                )
                self.tool_operational = True
                verbose_message(
                    JsonBase.VERBOSE, verbose, 'loaded ATS JSON base info'
                )

    def is_tool_ok(self):
        '''
            Checking is tool operational.

            :return: True (yes) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return self.tool_operational

    def __str__(self):
        '''
            Dunder method for JsonBase.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, str(self.__verbose),
            str(self.tool_operational), str(self.json2obj), str(self.obj2json)
        )
