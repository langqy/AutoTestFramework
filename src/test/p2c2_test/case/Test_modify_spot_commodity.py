# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestModifySpotCommodity(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='modify_spot_commodity').get_data()

    # 接口修改，不允许修改commodity_id
    # def modify_commodity_id_back(self, case):
    #     temp = case["old_commodity_id"]
    #     case["old_commodity_id"] = case["new_commodity_id"]
    #     case["new_commodity_id"] = temp
    #     send_list = [{"action": "modify_spot_commodity", "data": case}]
    #     send_string = json.dumps(send_list)
    #     BOCETcpClient(send_string).getData()


    def test_modify_spot_commodity(self):
        # data = {
        #     "commodity_id": "commodity_id",
        #     "name": "name",
        #     "contract_factor": 1,
        #     "margin_algr": 1,
        #     "margin_rate_b": 1,
        #     "margin_rate_s": 1,
        #     "pay_out_algr": 1,
        #     "pay_out_rate": 1,
        #     "settle_added_tax": 1,
        #     "fee_algr": 1,
        #     "fee_rate_b": 1,
        #     "fee_rate_s": 1,
        #     "common_is_all_money": 1,
        #     "min_quantity_move": 1,
        #     "min_price_move": 1,
        #     "spread_down_lmt": 1,
        #     "spread_algr": 1,
        #     "spread_up_lmt": 1,
        #     "last_price": 1,
        #     "is_spot_match": 1,
        #     "sort_id": 1,
        #     "status": 1,
        #     "min_settle_move_qty": 1
        # }

        for index, case in enumerate(self.data):
            # print case
            send_list = [{"action": "modify_spot_commodity", "data": case}]
            send_string = json.dumps(send_list)
            # print index + 3,
            # print case
            print index + 3,
            print BOCETcpClient(send_string).getData()

            # self.modify_commodity_id_back(case)
            # break


if __name__ == '__main__':
    unittest.main(verbosity=2)