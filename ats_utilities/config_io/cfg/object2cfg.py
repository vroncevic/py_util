# -*- coding: UTF-8 -*-

'''
 Module
     object2cfg.py
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
     Defined class Object2Cfg with attribute(s) and method(s).
     Created API for writing configuration/information to a cfg file.
'''

import sys

try:
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.base_write import BaseWriteConfig
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


class Object2Cfg(BaseWriteConfig):
    '''
        Defined class Object2Cfg with attribute(s) and method(s).
        Created API for writing configuration/information to a cfg file.
        It defines:

            :attributes:
                | __metaclass__ - setting verbose root for Object2Cfg.
                | __FORMAT - format of configuration content.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | write_configuration - write config to a cfg file.
                | __str__ - dunder method for object Object2Cfg.
    '''

    __metaclass__ = VerboseRoot
    __FORMAT = 'cfg'

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
        BaseWriteConfig.__init__(self, verbose=verbose)
        self.__verbose = verbose
        self.file_path = configuration_file
        verbose_message(Object2Cfg.VERBOSE, verbose, configuration_file)

    def write_configuration(self, configuration, verbose=False):
        '''
            Write configuration to a cfg file.

            :param configuration: configuration object | None.
            :type configuration: <Python object(s)> | <NoneType>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        verbose_message(Object2Cfg.VERBOSE, verbose, configuration)
        if configuration is None:
            return status
        with ConfigFile(self.file_path, 'w', Object2Cfg.__FORMAT) as cfg:
            if bool(cfg):
                for key in configuration:
                    config_value = configuration.get(key)
                    line = '{0} = {1}\n'.format(key, config_value)
                    cfg.write(line)
                status = True
        return status

    def __str__(self):
        '''
            Dunder method for Object2Cfg.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, BaseWriteConfig.__str__(self),
            str(self.__verbose)
        )
