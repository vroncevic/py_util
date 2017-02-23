# encoding: utf-8
"""
app.info - class AppInfo

Usage:
	from app.info import AppInfo

	info = {
		'app_name':'RCP',
		'app_version':'1.0',
		'app_build_date': '23 Feb 2017',
		'app_license':'GPLv3'
	}
	app_info = AppInfo(info)

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.name import AppName
from app.version import AppVersion
from app.build_date import BuildDate
from app.license import AppLicense

class AppInfo(AppName, AppVersion, BuildDate, AppLicense):
	"""
	Define class AppInfo with atribute(s) and method(s).
	Keep App/Tool/Script information.
	It defines:
		attribute:
			None
		method:
			__init__ - create and initial instance
	"""

	def __init__(self, info):
		"""
		@summary: Basic constructor
		@param info: Dictionary with App/Tool/Script basic info
		"""
		AppName.__init__(self, info['app_name'])
		AppVersion.__init__(self, info['app_version'])
		BuildDate.__init__(self, info['app_build_date'])
		AppLicense.__init__(self, info['app_license'])

