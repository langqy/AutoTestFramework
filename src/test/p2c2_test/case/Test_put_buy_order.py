# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestPutBuyOrder(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='put_buy_order').get_data()
        print self.data

    def test_put_buy_order(self):
        for case in self.data:
            send_list = [{"action": "put_buy_order", "data": case}]
            send_string = json.dumps(send_list)
            print BOCETcpClient(send_string).getData()


if __name__ == '__main__':
    unittest.main(verbosity=2)