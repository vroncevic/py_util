# -*- coding: utf-8 -*-

from json import load

try:
    from ats_utilities.config.base_read_config import BaseReadConfig
    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.error.ats_value_error import ATSValueError
    from ats_utilities.text.stdout_text import DBG, RST
except ImportError as e:
    msg = "\n{0}\n".format(e)
    print(msg)
    exit(-1)  # Force close python module #####################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Json2Object(BaseReadConfig):
    """
    Define class Json2Object with attribute(s) and method(s).
    Convert a configuration from json file to an object config.
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

    __FORMAT = 'json'
    VERBOSE = '[JSON_TO_OBJECT]'

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
        super(Json2Object, self).__init__(verbose)
        self.set_file_path(configuration_file)

    def read_configuration(self, verbose=False):
        """
        Read configuration from file.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Configuration object
        :rtype: Python object(s) | NoneType
        """
        cls = self.__class__
        jsn_path, content = self.get_file_path(), None
        if verbose:
            msg = "{0} {1}{2}\n{3}{4}".format(
                cls.VERBOSE, DBG, 'Read configuration from file', jsn_path, RST
            )
            print(msg)
        check_jsn_file = FileChecking.check_file(jsn_path, verbose)
        if check_jsn_file:
            file_extension = ".{0}".format(cls.__FORMAT)
            check_cfg_file_format = FileChecking.check_format(
                jsn_path, file_extension, verbose
            )
            if check_cfg_file_format:
                try:
                    with ConfigFile(jsn_path, 'r') as configuration_file:
                        content = load(configuration_file)
                except ATSValueError as e:
                    print(e)
                else:
                    if content:
                        if verbose:
                            msg = "{0} {1}".format(cls.VERBOSE, 'Done')
                            print(msg)
        return content

    def __str__(self):
        """
        Return human readable string (Json2Object).
        :return: String representation of Json2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Json2Object).
        :return: String representation of Json2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
