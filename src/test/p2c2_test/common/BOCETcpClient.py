# -*- coding: utf-8 -*-
import socket


class BOCETcpClient:

    def __init__(self, send_string):
        self.send_string = send_string

    def getData(self):
        return self._send()

    def _send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.6.63', 10001))

        sock.send(self.send_string)
        rec = sock.recv(10240)
        sock.close()
        return rec.decode('unicode-escape').encode('utf-8')

if __name__ == '__main__':
    import json
    data = {
        "page": 1,
        "size": 10,
    }
    send_list = [{"action": "query_spot_commodity_by_page", "data": data}]
    send_string = json.dumps(send_list)
    print BOCETcpClient(send_string).getData()