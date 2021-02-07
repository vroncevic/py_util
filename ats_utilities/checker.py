# -*- coding: UTF-8 -*-

"""
 Module
     checker.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class ATSChecker with attribute(s) and method(s).
     Checking def parameters (types, values).
"""

from inspect import stack
from collections import OrderedDict

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSChecker(object):
    """
        Define class ATSChecker with attribute(s) and method(s).
        Checking def parameters (types, values).
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __start_message - Start segment of usage message
                | __list_of_params - List of parameters for def
                | __error_type - List of mapped errors
                | __error_type_index - Error type index
                | __error_value_index - Error value index
                | TYPE_ERROR - Type error id
                | VALUE_ERROR - Value error id
            :methods:
                | __init__ - Initial constructor,
                | collect_params - Collecting all parameters in one list,
                | usage_message - Preparing usage message for def,
                | check_types - Checking parameters (types) for def,
                | check_values - Checking parameters (values) for def,
                | priority_error - Setting priority error id,
                | check_params - Checking parameters for def
    """

    __slots__ = (
        'VERBOSE',
        '__start_message',
        '__list_of_params',
        '__error_type',
        '__error_type_index',
        '__error_value_index',
        'TYPE_ERROR',
        'VALUE_ERROR'
    )
    VERBOSE = 'ATS_UTILITIES::ATS_CHECKER'
    TYPE_ERROR, VALUE_ERROR = 1, 2

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__start_message = None
        self.__list_of_params = []
        self.__error_type = [0, 0]
        self.__error_type_index = []
        self.__error_value_index = []

    def collect_params(self, params_descript):
        """
            Collecting all parameters in one list.

            :param params_descript: Description for parameters
            :type params_descript: <OrderedDict>
            :exceptions: None
        """
        for type_expect, inst in params_descript.items():
            self.__list_of_params.append(
                "\n    expected parameter {0} <{1}> object at {2}".format(
                    type_expect.split(':')[1],
                    type_expect.split(':')[0],
                    hex(id(inst))
                )
            )

    def usage_message(self):
        """
            Preparing usage message for def.

            :return: Usage message for def
            :rtype: <str>
            :exceptions: None
        """
        usage_message = self.__start_message
        for index, param in enumerate(self.__list_of_params):
            usage_message += param
            if index in self.__error_type_index:
                usage_message += " wrong type"
            if index in self.__error_value_index:
                usage_message += " wrong value"
        return usage_message

    def check_types(self, params_descript):
        """
            Checking parameters (types) for def.

            :param params_descript: Parameters description
            :type params_descript: <OrderedDict>
            :exceptions: None
        """
        for index, (type_expect, inst) in enumerate(params_descript.items()):
            if type(inst).__name__ != type_expect.split(':')[0]:
                self.__error_type[0] = ATSChecker.TYPE_ERROR
                self.__error_type_index.append(index)

    def check_values(self, params_descript):
        """
            Checking parameters (values) for def.

            :param params: Parameters description
            :type params: <OrderedDict>
            :exceptions: None
        """
        for index, (type_expect, inst) in enumerate(params_descript.items()):
            if inst == None:
                self.__error_type[1] = ATSChecker.VALUE_ERROR
                self.__error_value_index.append(index)
            any_base_type = any([
                isinstance(inst, dict),
                isinstance(inst, list),
                isinstance(inst, tuple),
                isinstance(inst, set),
                isinstance(inst, frozenset),
                isinstance(inst, bytearray),
                isinstance(inst, bytes),
            ])
            if any_base_type:
                if not bool(inst):
                    self.__error_type[1] = ATSChecker.VALUE_ERROR
                    self.__error_value_index.append(index)

    def priority_error(self):
        """
            Setting priority error id.

            :return: Priority error id (TYPE_ERROR | VALUE_ERROR | 0)
            :rtype: <int>
            :exceptions: None
        """
        if self.__error_type[0] == ATSChecker.TYPE_ERROR:
            return ATSChecker.TYPE_ERROR
        if self.__error_type[1] == ATSChecker.VALUE_ERROR:
            return ATSChecker.VALUE_ERROR
        if not all(self.__error_type):
            return 0

    def check_params(self, params_descript):
        """
            Checking parameters (values) for def.

            :param params_descript: Parameters description
            :type params_descript: <list>
            :return: Usage message, status (TYPE_ERROR | VALUE_ERROR | 0)
            :rtype: <str>, <int>
            :exceptions: None
        """
        func, module, error_id = stack()[1][3], stack()[1][1], 0
        error_message, header = None, "\nmod: {0}\n  def: {1}()"
        self.__start_message = header.format(module, func)
        self.collect_params(OrderedDict(params_descript))
        self.check_types(OrderedDict(params_descript))
        self.check_values(OrderedDict(params_descript))
        error_message = self.usage_message()
        error_id = self.priority_error()
        return error_message, error_id
