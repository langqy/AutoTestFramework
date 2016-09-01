# -*- coding: utf-8 -*-
from randomGen import random_string
import string
CODEMAP = string.digits + string.ascii_uppercase
WMap = [3, 7, 9, 10, 5, 8, 4, 2]


def get_C9(bref):
    # C9=11-MOD（∑Ci(i=1→8)×Wi,11）
    sum = 0
    for ind, i in enumerate(bref):
        Ci = CODEMAP.index(i)
        Wi = WMap[ind]
        sum += Ci * Wi

    C9 = 11 - (sum % 11)
    if C9 == 10:
        C9 = 'X'
    elif C9 == 11:
        C9 = '0'

    return str(C9)


def get_an_organizationcode():
    bref_str = random_string(8).upper()
    C9 = get_C9(bref_str)
    organization_code = '{0}-{1}'.format(bref_str, C9)
    return organization_code


def check_organizationcode(code):
    ERROR = '组织机构代码证错误!'
    if '-' in code:
        bref, C9_check = code.split('-')
    else:
        C9_check = code[-1:]
        bref = code[:-1]

    if len(bref) != 8 or len(C9_check) != 1:
        return ERROR + '（本体或校验码长度不符合要求）'
    else:
        try:
            C9_right = get_C9(bref)
        except ValueError:
            return ERROR + '(本体错误)'
        if C9_check != C9_right:
            return ERROR + '（校验码错误）'
        else:
            return '验证通过，组织机构代码证格式正确！'


if __name__ == '__main__':
    rand_or = get_an_organizationcode()
    print rand_or
    # print check_organizationcode('WV0X1KYT-X')
    # print check_organizationcode('WV0X1KYT-5')
    # print check_organizationcode('WV0X1K-5')
    # print check_organizationcode('WV0X1KYT-50')
    # print check_organizationcode('WV0X1KY@-5')
    # print check_organizationcode('WV0X1KYT5')


