.. toctree::
 :hidden:
 
 self
 modules

Python Utilities
============================

ats_utilities is framework for building Apps/Tools/Scripts.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

INSTALLATION
-----------------------------
Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/ats_utilities/releases

To install this set of modules type the following:

.. code-block:: bash

    tar xvzf ats_utilities-x.y.z.tar.gz
    cd ats_utilities-x.y.z/python-libs
    python setup.py install

DEPENDENCIES
-----------------------------
ats_utilities requires other modules and libraries:

.. code-block:: bash

    yaml
    bs4
    configparser
    colorama
    pathlib

LIBRARY STRUCTURE
-----------------------------
ats_utilities is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png

Framework structure:

.. code-block:: bash

    .
    ├── ats_utilities/
    │   ├── abstract/
    │   │   └── __init__.py
    │   ├── ats_info.py
    │   ├── cfg_base.py
    │   ├── config/
    │   │   ├── base_read_config.py
    │   │   ├── base_write_config.py
    │   │   ├── cfg/
    │   │   │   ├── cfg2object.py
    │   │   │   ├── __init__.py
    │   │   │   └── object2cfg.py
    │   │   ├── check_base_config.py
    │   │   ├── config_context_manager.py
    │   │   ├── file_checking.py
    │   │   ├── ini/
    │   │   │   ├── ini2object.py
    │   │   │   ├── __init__.py
    │   │   │   └── object2ini.py
    │   │   ├── __init__.py
    │   │   ├── json/
    │   │   │   ├── __init__.py
    │   │   │   ├── json2object.py
    │   │   │   └── object2json.py
    │   │   ├── xml/
    │   │   │   ├── __init__.py
    │   │   │   ├── object2xml.py
    │   │   │   └── xml2object.py
    │   │   └── yaml/
    │   │       ├── __init__.py
    │   │       ├── object2yaml.py
    │   │       └── yaml2object.py
    │   ├── console_io/
    │   │   ├── error.py
    │   │   ├── __init__.py
    │   │   ├── success.py
    │   │   ├── verbose.py
    │   │   └── warning.py
    │   ├── exceptions/
    │   │   ├── ats_attribute_error.py
    │   │   ├── ats_bad_call_error.py
    │   │   ├── ats_file_error.py
    │   │   ├── ats_key_error.py
    │   │   ├── ats_lookup_error.py
    │   │   ├── ats_type_error.py
    │   │   ├── ats_value_error.py
    │   │   └── __init__.py
    │   ├── ini_base.py
    │   ├── __init__.py
    │   ├── json_base.py
    │   ├── logging/
    │   │   ├── ats_logger_base.py
    │   │   ├── ats_logger_file.py
    │   │   ├── ats_logger_name.py
    │   │   ├── ats_logger.py
    │   │   ├── ats_logger_status.py
    │   │   └── __init__.py
    │   ├── option/
    │   │   ├── ats_option_parser.py
    │   │   └── __init__.py
    │   ├── register/
    │   │   └── __init__.py
    │   ├── xml_base.py
    │   └── yaml_base.py
    └── setup.py

COPYRIGHT AND LICENCE
-----------------------------

GPL v3 https://www.gnu.org/licenses/gpl-3.0

Copyright (C) 2018 by https://vroncevic.github.io/ats_utilities/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.