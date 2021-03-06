# -*- coding: UTF-8 -*-

'''
 Module
     meta_thread.py
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
     Defined class ThreadSafeSingletonMeta with attribute(s) and method(s).
     Created API for auto-register singleton object.
'''

from threading import Lock

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ThreadSafeSingletonMeta(type):
    '''
        Defined class ThreadSafeSingletonMeta with attribute(s) and method(s).
        Created API for auto-register singleton object.
        It defines:

            :attributes:
                | __INSTANCES - class dictionary for collecting instances.
                | __LOCK - thread lock object.
            :methods:
                | __call__ - check instance and setup instance.
                | __str__ - dunder method for ThreadSafeSingletonMeta.
    '''

    __INSTANCES = {}
    __LOCK = Lock()

    def __call__(cls, *args, **kwargs):
        '''
            Check instance and setup instance.

            :param *args: iteration object.
            :type *args: <iter>
            :param **kwargs: iteration object.
            :type **kwargs: <dict>
            :return: python object instance.
            :rtype: <Python Object>
            :exception: NotImplementedError
        '''
        with ThreadSafeSingletonMeta.__LOCK:
            if cls not in cls.__INSTANCES:
                cls.__INSTANCES[cls] = super(
                    ThreadSafeSingletonMeta, cls
                ).__call__(*args, **kwargs)
            return cls.__INSTANCES[cls]

    def __str__(cls):
        '''
            Dunder method for ThreadSafeSingletonMeta.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(cls.__name__)
