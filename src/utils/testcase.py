# -*- coding: utf-8 -*-
import json
import unittest
from src.utils.config import DefaultConfig, Config
from src.utils.xml_reader import XMLReader
from src.utils.excel_reader import ExcelReader


DATA_PATH = DefaultConfig().data_path


class TestCaseGenerator(object):

    def __init__(self, project):
        self.project_name = project
        self.config_file = 'config_%s.ini' % self.project_name
        self.interface_file = '%s.xml' % self.project_name
        self.test_file = 'test_%s.py' % self.project_name

        interface_reader = XMLReader(DATA_PATH + self.interface_file)
        self.interfaces = interface_reader.get_all_interfaces()

    import_string = """import unittest\n"""

    def generate(self):
        with open(self.test_file, 'wb') as test_file:
            test_file.write(self.import_string)
            for interface in self.interfaces:
                class_string = 'class Test%s(unittest.TestCase):\n' % interface









