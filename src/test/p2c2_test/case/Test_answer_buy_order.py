# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient
from test.p2c2_test.common.get_case_from_excel import CaseData


class TestAnswerBuyOrder(unittest.TestCase):

    def setUp(self):
        self.data = CaseData(sheet_name='answer_buy_order').get_data()
        print self.data

    def test_answer_buy_order(self):
        for index, case in enumerate(self.data):
            send_list = [{"action": "answer_buy_order", "data": case}]
            send_string = json.dumps(send_list)
            print index + 3,
            print BOCETcpClient(send_string).getData()


if __name__ == '__main__':
    unittest.main(verbosity=2)