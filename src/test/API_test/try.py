# -*- coding: utf-8 -*-

import json

import requests
from useless.sign import sign

# m = hashlib.md5()
# m.update('qqqq1111')
# print m.hexdigest()
#
# m1 = hashlib.sha1()
# m1.update('qqqq1111')
# print m1.hexdigest()

# import requests
# import json
#
# mob = {'p_mobile':'13691466409'}
#
# from tools.sign import sign
# after = sign(mob, '84b0d211449da13fc9db1c1555e3ef00')
# print 'after sign() {0}'.format(after)
#
# mob['sign'] = after
# inparam = json.dumps(mob)
# s = requests.session()
# s.headers.update({'Content-Type': 'application/json'})
# # r = s.post('http://192.168.7.227:8080/zhigou/P_User__GetMobile', data=inparam)
# # print r.content
# print json.loads(s.post('http://192.168.7.227:8080/zhigou/P_Merchant__GetApplyList', json.dumps(
#     {"p_userid": 26, "sign": sign({"p_userid": 26})})).content)['p_status']
#
# deny = {"p_opid": 1, "p_merchantid": 29, "p_status": 4, "p_approvememo": "deny"}
# deny['sign'] = sign(deny)
# j = s.post('http://192.168.7.227:8080/zhigou/P_Merchant__ApproveApply', json.dumps(deny))
# print j.content

# import cx_Oracle
# con = cx_Oracle.connect('zhigouceshi/zhigouceshi@192.168.7.226:1521/ZHIGOU')
# cur = con.cursor()
# cur.execute("select merchantid from user_merchant t where t.userid='58'")
# count = cur.fetchone()
# print count[0]
# cur.close()
# con.close()

import sys
print sys.path
path = sys.path
path.append(r'e:\d.txt')
for i in path:
    print i
print sys.path