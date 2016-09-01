# -*- coding: utf-8 -*-

from BOCETcpClient import BOCETcpClient
import json


def query_spot_by_id(commodity_id):
    data = {
        "commodity_id": commodity_id,
    }

    send_list = [{"action": "query_spot_commodity_by_id", "data": data}]
    send_string = json.dumps(send_list)
    return BOCETcpClient(send_string).getData()


if __name__ == '__main__':
    print query_spot_by_id("TEST0001")