# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.PersonalCenter import PersonalCenter
from test.API_test.common.TestStuff import generator

from src.utils import Config

url_xml = Config().get('data', 'url_xml')

u = PersonalCenter()
u.collection_add(merchantid=30)
u.collection_add(merchantid=29)
u.collection_add(product_id=1)
u.collection_add(product_id=2)
u.collection_add(merchantid=29, product_id=2)

cl = generator(datafile='personalcenter.xlsx', sheet_name='CollectionGet', userid=u.userid)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(cl)
    unittest.TextTestRunner(verbosity=2).run(suite)