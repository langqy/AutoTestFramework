# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.User import User
from test.API_test.common.newusercheck import NewUserCheck

from src.utils import ReadXML


class TestAddStep1(unittest.TestCase):
    def setUp(self):
        self.sheet_name = 'AddStep1'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)
        self.userid = User().signup()

    def test_addstep1(self):
        results = NewUserCheck(self.url, sheet_name=self.sheet_name, userid=self.userid).docase3()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
