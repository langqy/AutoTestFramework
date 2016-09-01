# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestPutSellOrder(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='put_sell_order').get_data()

    def test_put_sell_order(self):
        case = {'trader_id':'777000011',
                'commodity_id':'CT0010',
                'quantity':'1',
                'price':'100',
                'order_ip':'192.168.1.1',
                'reg_stock_id':'BOCE-321-C50003-160812-777000011-R027057',
                'frozen_weight':'1',
                'user_id':'777000011',
                'sell_type':'1'
                }
        # for index, case in enumerate(self.data):
        # print case
        send_list = [{"action": "put_sell_order", "data": case}]
        send_string = json.dumps(send_list)
        # print index + 3,
        print BOCETcpClient(send_string).getData()


if __name__ == '__main__':
    unittest.main(verbosity=2)


