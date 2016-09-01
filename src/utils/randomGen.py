# -*- coding: utf-8 -*-
"""随机产生手机号，随机产生字符串"""
import randomGen
import string


def random_phone_number():
    """随机产生手机号"""
    return randomGen.choice(['139', '136', '151', '158']) + ''.join(randomGen.choice('0123456789') for i in range(8))


def random_string(length=1):
    """随机产生长度为length的字符串"""
    return ''.join(randomGen.sample(string.ascii_letters + string.digits, length))


def list_to_str(list_in):
    str_out = ''
    for i in list_in:
        str_out += str(i)
    return str_out


def random_number_str(length=1):
    """随机产生长度为length的数字串"""
    return ''.join(list_to_str([randomGen.randint(0, 9) for i in range(length)]))

if __name__ == '__main__':
    print random_phone_number()
    print random_string()
    print random_string(8)
    print random_number_str(18)