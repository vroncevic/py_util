# encoding: utf-8

from configparser import ConfigParser

from ats_utilities.config.base_read_config import BaseReadConfig
from ats_utilities.config.config_context_manager import ConfigFile
from ats_utilities.config.file_checking import FileChecking
from ats_utilities.error.ats_value_error import ATSValueError
from ats_utilities.text.stdout_text import DBG, RST

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Ini2Object(BaseReadConfig):
    """
    Define class Ini2Object with attribute(s) and method(s).
    Convert configuration from an ini file to an object with structure composed
    of sections, properties, and values.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            VERBOSE - Verbose prefix console text
        method:
            __init__ - Initial constructor
            read_configuration - Read configuration from file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'ini'
    VERBOSE = '[INI_TO_OBJECT]'

    def __init__(self, configuration_file, verbose=False):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type configuration_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Setting interface', RST
            )
            print(msg)
        super(Ini2Object, self).__init__(verbose)
        self.set_file_path(configuration_file)

    def read_configuration(self, verbose=False):
        """
        Read configuration from file.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Configuration object
        :rtype: ConfigParser | NoneType
        """
        cls = self.__class__
        file_path, content = self.get_file_path(), None
        if verbose:
            msg = "{0} {1}{2}\n{3}{4}".format(
                cls.VERBOSE, DBG, 'Read configuration from file', file_path, RST
            )
            print(msg)
        check_cfg_file = FileChecking.check_file(file_path, verbose)
        if check_cfg_file:
            file_extension = ".{0}".format(Ini2Object.__FORMAT)
            check_cfg_file_format = FileChecking.check_format(
                file_path, file_extension, verbose
            )
            if check_cfg_file_format:
                try:
                    with ConfigFile(file_path, 'r') as configuration_file:
                        content = ConfigParser()
                        content.read_file(configuration_file)
                except ATSValueError as e:
                    print(e)
                else:
                    if content:
                        if verbose:
                            msg = "{0} {1}".format(cls.VERBOSE, 'Done')
                            print(msg)
                        return content
        return None

    def __str__(self):
        """
        Return human readable string (Ini2Object).
        :return: String representation of Ini2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Ini2Object).
        :return: String representation of Ini2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
