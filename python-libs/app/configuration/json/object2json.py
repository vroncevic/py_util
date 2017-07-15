# encoding: utf-8

from app.configuration.abstract_set_config import AbstractSetConfig
from app.configuration.file_config import FileConfig
from json import dump

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Json(AbstractSetConfig):
    """
    Define class Object2Json with attribute(s) and method(s).
    Convert a configuration object to a json format and write to file.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            __file_path - Configuration file path
        method:
            __init__ - Initial constructor
            set_configuration - Write configuration to a json file
    """

    __FORMAT = 'json'

    def __init__(self, configuration_file):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type: str
        """
        self.__file_path = configuration_file

    def set_configuration(self, configuration):
        """
        Write configuration to a json file.
        :param configuration: Configuration object
        :type: Python object(s)
        :return: Boolean status
        :rtype: bool
        """
        check_cfg_file = FileConfig.check_file(self.__file_path)
        if check_cfg_file:
            file_extension = ".{0}".format(Object2Json.__FORMAT)
            check_cfg_file_format = FileConfig.check_format(
                self.__file_path, file_extension
            )
            if check_cfg_file_format:
                try:
                    configuration_file = open(self.__file_path, 'w')
                    dump(configuration, configuration_file)
                except IOError as e:
                    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
                    print(msg)
                else:
                    configuration_file.close()
                    return True
        return False
