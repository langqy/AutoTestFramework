# -*- coding: utf-8 -*-

import datetime
import unittest

from case import Test_delete_spot_commodity, Test_query_spot_commodity_by_id,Test_query_spot_commodity_by_page
from src.utils import Config
from src.utils import HTMLTestRunner


def get_suite():
    p2c2_suite = unittest.TestSuite()

    p2c2_suite.addTest(unittest.findTestCases(Test_query_spot_commodity_by_id))
    p2c2_suite.addTest(unittest.findTestCases(Test_query_spot_commodity_by_page))
    # p2c2_suite.addTest(unittest.findTestCases(Test_add_spot_commodity))
    p2c2_suite.addTest(unittest.findTestCases(Test_delete_spot_commodity))
    # p2c2_suite.addTest(unittest.findTestCases(Test_modify_spot_commodity))

    return p2c2_suite


if __name__ == '__main__':
    file_name = Config().get('report', 'path') + 'TestReport_{0}.html'\
            .format(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))

    runner = HTMLTestRunner(
        stream=file(file_name, 'wb'),
        title=u'P2C2用例执行报告',
        description=u'P2C2用例执行报告'
    )
    runner.run(get_suite())