# -*- coding: utf-8 -*-

import json
import unittest

from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestAddSpotCommodity(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='add_spot_commodity').get_data()

    def test_add_spot_commodity(self):
            # case = {
            #     "commodity_id": "TEST00025",
            #     "name": "伊利牛奶25",
            #     "contract_factor": 1,
            #     "margin_algr": 1,
            #     "margin_rate_b": 1,
            #     "margin_rate_s": 1,
            #     "pay_out_algr": 1,
            #     "pay_out_rate": 1,
            #     "settle_added_tax": 0,
            #     "fee_algr": 1,
            #     "fee_rate_b": 1,
            #     "fee_rate_s": 1,
            #     "common_is_all_money": 1,
            #     "min_quantity_move": 1,
            #     "min_price_move": 1,
            #     "spread_algr": 2,
            #     "spread_down_lmt": 3,
            #     "spread_up_lmt": 3,
            #     "last_price": 2,
            #     "is_spot_match": 1,
            #     "sort_id": 1,
            #     "status": 3,
            #     "min_settle_move_qty": 1
            # }
        for index, case in enumerate(self.data):
            send_list = [{"action": "add_spot_commodity", "data": case}]
            send_string = json.dumps(send_list)
            # log('Test_add_spot_commodity index : ', str(index+3), 'error')
            # log('Test_add_spot_commodity case  : ', str(case), 'warning')
            # log('Test_add_spot_commodity result: ', BOCETcpClient(send_string).getData(), 'error')
            print index + 3,
            print case
            print index + 3,
            print BOCETcpClient(send_string).getData()
            # print

if __name__ == '__main__':
    unittest.main(verbosity=2)