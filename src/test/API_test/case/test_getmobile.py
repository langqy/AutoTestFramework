# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.BaseCaseOperate import BaseCaseOperate

from src.utils import ReadXML


class TestGetMobile(unittest.TestCase):
    def setUp(self):
        self.sheet_name = 'GetMobile'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_getmobile(self):
        results = BaseCaseOperate(self.url, sheet_name=self.sheet_name).run()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])

if __name__ == '__main__':
    unittest.main(verbosity=2)