# -*- coding: UTF-8 -*-

'''
 Module
     yaml2object.py
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
     Defined class Yaml2Object with attribute(s) and method(s).
     Created API for reading a configuration/information from a yaml file.
'''

import sys

try:
    from yaml import load, FullLoader
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.base_read import BaseReadConfig
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Yaml2Object(BaseReadConfig):
    '''
        Defined class Yaml2Object with attribute(s) and method(s).
        Created API for reading a configuration/information from a yaml file.
        It defines:

            :attributes:
                | __metaclass__ - setting verbose root for Yaml2Object.
                | __FORMAT - format of configuration content.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | read_configuration - getting a configuration from file.
                | __str__ - dunder method for object Yaml2Object.
    '''

    __metaclass__ = VerboseRoot
    __FORMAT = 'yaml'

    def __init__(self, configuration_file, verbose=False):
        '''
            Initial constructor.

            :param configuration_file: configuration file path.
            :type configuration_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:configuration_file', configuration_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        BaseReadConfig.__init__(self, verbose=verbose)
        self.__verbose = verbose
        self.file_path = configuration_file
        verbose_message(Yaml2Object.VERBOSE, verbose, configuration_file)

    def read_configuration(self, verbose=False):
        '''
            Getting a configuration from yaml file.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: configuration object | None.
            :rtype: <Python object(s)> | <NoneType>
            :exceptions: None
        '''
        config = None
        with ConfigFile(self.file_path, 'r', Yaml2Object.__FORMAT) as yaml:
            if bool(yaml):
                config = load(yaml, Loader=FullLoader)
        verbose_message(
            Yaml2Object.VERBOSE, self.__verbose or verbose, config
        )
        return config

    def __str__(self):
        '''
            Dunder method for Yaml2Object.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, BaseReadConfig.__str__(self),
            str(self.__verbose)
        )
