# -*- coding: UTF-8 -*-

'''
 Module
     object2xml.py
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
     Defined class Object2Xml with attribute(s) and method(s).
     Created API for writing a configuration to file a xml.
'''

import sys

try:
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.config_io.base_write import BaseWriteConfig
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Xml(BaseWriteConfig):
    '''
        Defined class Object2Xml with attribute(s) and method(s).
        Created API for writing a configuration to file a xml.
        It defines:

            :attributes:
                | __FORMAT - Format of configuration content.
            :methods:
                | __init__ - Initial constructor.
                | write_configuration - Write configuration to a xml file.
                | __str__ - Dunder method for object Object2Xml.
    '''

    __FORMAT = 'xml'

    def __init__(self, configuration_file):
        '''
            Initial constructor.

            :param configuration_file: Configuration file path.
            :type configuration_file: <str>
            :exceptions: None
        '''
        BaseWriteConfig.__init__(self)
        self.file_path = configuration_file

    def write_configuration(self, configuration):
        '''
            Write configuration to a xml file.

            :param configuration: Configuration object.
            :type: <BeautifulSoup>
            :return: True (success) | False.
            :rtype: <bool>
            :exception: None
        '''
        status = False
        if configuration is None:
            return status
        with ConfigFile(self.file_path, 'w', Object2Xml.__FORMAT) as xml:
            if bool(xml):
                xml.write('{0}'.format(configuration))
                status = True
        return True if status else False

    def __str__(self):
        '''
            Dunder method for Object2Xml.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, BaseWriteConfig.__str__(self)
        )
