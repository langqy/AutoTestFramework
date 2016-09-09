# -*- coding: utf-8 -*-
"""此类用来生成测试文件，从数据文件中读取测试用例，从xml中读取接口配置，组织到测试文件中。

一个接口是一个class，每一条测试用例是一个method。

"""
from src.utils.config import DefaultConfig, Config
from src.utils.xml_reader import XMLReader
from src.utils.excel_reader import ExcelReader
from src.utils.logger import Logger


DATA_PATH = DefaultConfig().data_path


class TestCaseGenerator(object):

    def __init__(self, project):
        self.logger = Logger(__name__).return_logger()

        self.project_name = project
        self.config_file = 'config_%s.ini' % self.project_name
        self.interface_file = '%s.xml' % self.project_name
        self.test_file = 'test_%s.py' % self.project_name

        self.interface_reader = XMLReader(self.interface_file)
        self.tags = self.interface_reader.get_tags()

    def generate(self):
        with open(self.test_file, 'wb') as test_file:
            test_file.write(self.import_string)
            for tag in self.tags:
                # interface = self.interface_reader.get_url(tag)

                class_string = self.get_class(tag)
                test_file.write(class_string)

                test_file.write('\n\n\n')

    @property
    def import_string(self):
        import_string = """# -*- coding: utf-8 -*-\nimport unittest\nimport json\n"""
        rest_flag = webservice_flag = socket_flag = 0
        for tag in self.tags:
            interface_type = self.interface_reader.get_type(tag).lower()
            if interface_type in ['rest', 'restful', 'http']:
                rest_flag = 1
            elif interface_type == 'webservice':
                webservice_flag = 1
            elif interface_type in ['tcp', 'socket']:
                socket_flag = 1
            else:
                self.logger.error(u'没有找到合适的接口类型')
        if rest_flag:
            import_string += 'import requests\n'
        if webservice_flag:
            import_string += 'import suds\n'
        if socket_flag:
            import_string += 'import socket\n'
        import_string += 'from src.utils.logger import Logger\n\n'
        return import_string

    def get_class(self, tag):
        data_file = self.interface_reader.get_file(tag)
        sheet = self.interface_reader.get_sheet(tag)
        excel_reader = ExcelReader(data_file, sheet=sheet)

        interface_type = self.interface_reader.get_type(tag).lower()

        class_string = 'class Test%s(unittest.TestCase):\n\n' % tag

        # todo: rest webservice socket

        if interface_type in ['rest', 'restful', 'http']:
            setup_string = self.get_rest_setup(tag)
            cases_string = ''
            teardown_string = self.get_rest_teardown(tag)

            for num, case in enumerate(excel_reader.data):
                case_string = self.get_rest_test(tag, num, case)
                cases_string += case_string

            class_string += setup_string + teardown_string + cases_string
        return class_string


    def get_rest_setup(self, tag):
        setup_string = """    def setUp(self):\n        pass\n\n"""

        return setup_string

    def get_rest_teardown(self, tag):
        teardown_string = """    def tearDown(self):\n        pass\n\n"""
        return teardown_string


    def get_rest_test(self, tag, num, case):
        method = self.interface_reader.get_method(tag)
        interface_url = self.interface_reader.get_url(tag)
        test_string = """    def test_%s_%d(self):\n        pass\n\n""" % (tag, num)
        return test_string



    def get_setup(self, interface):
        pass


    def get_test(self, interface):
        pass

    def get_teardown(self, interface):
        pass



if __name__ == '__main__':
    g = TestCaseGenerator('zhigou')
    # print g.interfaces
    g.generate()
    # print g.import_string









