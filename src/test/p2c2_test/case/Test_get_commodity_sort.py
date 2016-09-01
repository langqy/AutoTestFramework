# -*- coding: utf-8 -*-

import unittest
import json
from test.p2c2_test.common.BOCETcpClient import BOCETcpClient


class TestAddSpotCommodity(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_spot_commodity(self):
        send_list = [{"action": "get_commodity_sort"}]
        send_string = json.dumps(send_list)
        print BOCETcpClient(send_string).getData()

if __name__ == '__main__':
    unittest.main(verbosity=2)