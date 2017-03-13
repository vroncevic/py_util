# encoding: utf-8
"""
app.configuration.xml.xml2object - class Xml2Object

Usage:
	from app.configuration.xml.xml2object import Xml2Object

	config_reader = Xml2Object("simple_file.xml")
	config = config_reader.get_configuration()
	# operate with configuration object
	# ...

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.abstract_get_config import AbstractGetConfig
from app.configuration.file_config import FileConfig
from bs4 import BeautifulSoup

class Xml2Object(AbstractGetConfig):
	"""
	Define class Xml2Object with attribute(s) and method(s).
	Convert a xml configuration file (xml tags) to an object with structure
	composed of sections, properties, and values.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			get_configuration - Getting a configuration from file
	"""

	__FORMAT = "xml"

	def __init__(self, configuration_file):
		"""
		:arg: xml_file - Absolute configuration file path
		:type: str
		"""
		self.__file_path = configuration_file

	def get_configuration(self):
		"""
		:return: configuration file
		:rtype: BeautifulSoup or NoneType
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Xml2Object.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "r")
					content = configuration_file.read()
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					config = BeautifulSoup(content, Xml2Object.__FORMAT)
					if content:
						configuration_file.close()
						return config
		return None
