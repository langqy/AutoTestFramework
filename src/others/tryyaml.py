# -*- coding: utf-8 -*-

import yaml


y = yaml.load(file('D:\\py\\AutoTestFramework\\data\\test.yaml', 'r'))

for i in y:
    print i

print y[3]['test'][12]['strn']
print y[3]['test'][13]['strn2']