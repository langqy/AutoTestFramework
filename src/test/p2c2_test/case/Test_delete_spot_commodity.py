# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestDeleteSpotCommodity(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='delete_spot_commodity').get_data()

    def test_delete_spot_commodity(self):
        # data = {
        #     "commodity_id": "commodity_id"
        # }
        for case in self.data:

            send_list = [{"action": "delete_spot_commodity", "data": case}]
            send_string = json.dumps(send_list)
            print BOCETcpClient(send_string).getData()

if __name__ == '__main__':
    unittest.main(verbosity=2)