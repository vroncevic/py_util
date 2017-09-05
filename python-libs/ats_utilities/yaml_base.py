# -*- coding: utf-8 -*-

import sys
from abc import ABCMeta, abstractmethod

try:
    from ats_utilities.text import COut
    from ats_utilities.text.stdout_text import ATS, DBG, ERR, RST
    from ats_utilities.ats_info import ATSInfo
    from ats_utilities.yaml_settings import YamlSettings
    from ats_utilities.option.ats_option_parser import ATSOptionParser
    from ats_utilities.config.check_base_config import CheckBaseConfig
    from ats_utilities.error.ats_value_error import ATSValueError
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class YamlBase(ATSInfo, YamlSettings, ATSOptionParser):
    """
    Define class YamlBase with attribute(s) and method(s).
    Load a settings, create a CL interface and run operation.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __tool_operational - Control operational flag
        method:
            __init__ - Initial constructor
            add_new_option - Adding new option for CL interface
            get_tool_status - Getting tool status
            set_tool_status - Setting tool status
            process - Process and run tool operation (Abstract method)
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = 'YAML_BASE'

    def __init__(self, base_config_file, verbose=False):
        """
        Setting version, build date, name and license of App/Tool/Script.
        :param base_config_file: Configuration file path
        :type base_config_file: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Checking YAML configuration')
        COut.print_console_msg(msg, verbose=verbose)
        YamlSettings.__init__(self, base_config_file, verbose)
        self.__tool_operational = False
        configuration = self.read_configuration(verbose)
        check_configuration = CheckBaseConfig.is_correct(
            configuration, verbose
        )
        if configuration and check_configuration:
            ATSInfo.__init__(self, configuration, verbose)
            statuses = []
            tool_version = self.get_ats_version()
            statuses.append(tool_version)
            tool_build_date = self.get_ats_build_date()
            statuses.append(tool_build_date)
            tool_name = self.get_ats_name()
            statuses.append(tool_name)
            tool_lic = self.get_ats_license()
            statuses.append(tool_lic)
            if all(status for status in statuses):
                tool_info = "{0} {1}".format(tool_version, tool_build_date)
                ATSOptionParser.__init__(
                    self, tool_info, tool_name, tool_lic, verbose
                )
                self.__tool_operational = True
            else:
                msg = "\n{0} {1}{2} of {3} {4}\n".format(
                    cls.VERBOSE, ERR,
                    'Missing version/build_date/name or license', ATS, RST
                )
                raise ATSValueError(msg)
        else:
            msg = "\n{0} {1}{2} of {3}{4}\n".format(
                cls.VERBOSE, ERR, 'Wrong configuration structure', ATS, RST
            )
            raise ATSValueError(msg)

    def add_new_option(self, *args, **kwargs):
        """
        Adding new option for CL interface.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        """
        self.add_operation(*args, **kwargs)

    def get_tool_status(self, verbose=False):
        """
        Getting tool status.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (tool ready) | False
        :rtype: <bool>
        """
        msg = "Tool status [{0}]".format(self.__tool_operational)
        COut.print_console_msg(msg, verbose=verbose)
        return self.__tool_operational

    def set_tool_status(self, tool_status, verbose=False):
        """
        Setting tool status.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :param tool_status: Tool status (boolean)
        :type tool_status: <bool>
        """
        msg = "Tool status [{0}]".format(tool_status)
        COut.print_console_msg(msg, verbose=verbose)
        self.__tool_operational = tool_status

    @abstractmethod
    def process(self, verbose=False):
        """
        Process and run tool operation (Abstract method).
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        pass

    def __str__(self):
        """
        Return human readable string (YamlBase).
        :return: String representation of YamlBase
        :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (YamlBase).
        :return: String representation of YamlBase
        :rtype: <str>
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
