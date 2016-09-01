# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.TestStuff import generator

from src.utils import Config

url_xml = Config().get('data', 'url_xml')

# u = User().signup()
# on = OnlinePurchase(u)
# on.ReceiveaddrAdd()
# on.ReceiveaddrAdd()
# on.ShoppingCartAdd()
# on.ShoppingCartAdd(merchant=29, product=2, countnum=2, spectypegroup_id='6*7')
# on.PresettlementCreate()
# on.OrderAdd()
# print on.OrderGet()

cl = generator(datafile='personalcenter.xlsx', sheet_name='PersonalGethistorybill', userid=1678)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(cl)
    unittest.TextTestRunner(verbosity=2).run(suite)