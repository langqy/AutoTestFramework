# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestQueryCommodityOrder(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='query_commodity_order').get_data()

    def test_query_commodity_order(self):
        for index, case in enumerate(self.data):
            send_list = [{"action": "query_commodity_order", "data": case}]
            send_string = json.dumps(send_list)
            print index + 3,
            # print case
            print BOCETcpClient(send_string).getData()
            # print

if __name__ == '__main__':
    unittest.main(verbosity=2)