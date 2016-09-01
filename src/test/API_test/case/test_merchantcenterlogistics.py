# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.TestStuff import generator

from src.utils import Config

url_xml = Config().get('data', 'url_xml')
# buyer = OnlinePurchase(248)
# print buyer.ShoppingCartAdd(merchant=1708, product=164, countnum=1, spectypegroup_id='112*114')
# print buyer.PresettlementCreate()
# print buyer.OrderAdd()
# print buyer.Purchase_Pay()
# m = MerchantCenter(1892)
# print m.prepare(order_id=m.get_not_prepare_order_from_db())

cl = generator(datafile='merchantcenter.xlsx', sheet_name='MerchantcenterLogistics', userid=1892)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(cl)
    unittest.TextTestRunner(verbosity=2).run(suite)

