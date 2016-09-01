# -*- coding: utf-8 -*-
import unittest

from test.API_test.common.PersonalCenter import PersonalCenter
from test.API_test.common.TestStuff import generator
from tools.config import Config

url_xml = Config().get('data', 'url_xml')
u = PersonalCenter()
# print u.realname_upauthentication(realname='JJ', idcardnumber=random_number_str(length=18), idcardfronturl='/ss.jpg', idcardbackurl='/jj.jpg')
cl = generator(datafile='personalcenter.xlsx', sheet_name='RealnameUpauthentication', userid=u.userid)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(cl)
    unittest.TextTestRunner(verbosity=2).run(suite)
