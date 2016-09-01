# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestQuerySpotCommodityByID(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='query_spot_commodity_by_id').get_data()
        # print self.data

    def test_query_spot_commodity_by_id(self):
        # case = {
        #     "commodity_id":"TEST4690",
        # }

        for case in self.data:
            send_list = [{"action": "query_spot_commodity_by_id", "data": case}]
            send_string = json.dumps(send_list)
            print BOCETcpClient(send_string).getData()


if __name__ == '__main__':
    unittest.main(verbosity=2)