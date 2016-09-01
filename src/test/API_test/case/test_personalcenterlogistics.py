# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.TestStuff import generator

from src.utils import Config

url_xml = Config().get('data', 'url_xml')
cl = generator(datafile='personalcenter.xlsx', sheet_name='PersonalcenterLogistics', userid=248)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(cl)
    unittest.TextTestRunner(verbosity=2).run(suite)