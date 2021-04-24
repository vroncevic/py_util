# -*- coding: UTF-8 -*-

'''
 Module
     xml_cli.py
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
     Defined class XmlCLI with attribute(s) and method(s).
     Created API for check and load informations, setup argument parser.
'''

import sys

try:
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.xml import XmlBase
    from ats_utilities.abstract import AbstractMethod
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


class XmlCLI(XmlBase):
    '''
        Defined class XmlCLI with attribute(s) and method(s).
        Created API for check and load informations, setup argument parser.
        It defines:

            :attributes:
                | __metaclass__ - Setting verbose root for XmlCLI.
                | __verbose - Enable/disable verbose option.
            :methods:
                | __init__ - Initial constructor.
                | add_new_option - Adding new option for CL interface.
                | parse_args - Parse arguments.
                | process - Process and run tool operation (Abstract method).
                | __str__ - Dunder method for XmlCLI.
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
        XmlBase.__init__(self, informations_file, verbose=verbose)
        self.__verbose = verbose
        verbose_message(XmlCLI.VERBOSE, verbose, 'init ATS xml cli')

    def add_new_option(self, *args, **kwargs):
        '''
            Adding new option for CL interface.

            :param args: List of arguments (objects).
            :type args: <list>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <dict>
            :exceptions: None
        '''
        self.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv):
        '''
            Process arguments from start.

            :param argv: Arguments.
            :type argv: <Python object(s)>
            :return: Options and arguments.
            :rtype: <Python object(s)>
            :exceptions: None
        '''
        (opts, args) = self.option_parser.parse_args(argv)
        return opts, args

    @AbstractMethod
    def process(self, verbose=False):
        '''
            Process and run tool operation (Abstract method).

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exception: NotImplementedError
        '''

    def __str__(self):
        '''
            Dunder method for XmlCLI.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0}({1}, {2})'.format(
            self.__class__.__name__, XmlBase.__str__(self), str(self.__verbose)
        )