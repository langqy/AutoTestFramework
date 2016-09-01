# -*- coding: utf-8 -*-
import hashlib
from logger import log
from config import DefaultConfig


class Encrypt:

    def __init__(self, priv_key=None, pwd_key=None):
        if priv_key is None:
            self.priv_key = DefaultConfig().get('encrypt', 'priv_key')
        else:
            self.priv_key = priv_key

        if pwd_key is None:
            self.pwd_key = DefaultConfig().get('encrypt', 'pwd_key')
        else:
            self.pwd_key = pwd_key

    def sign(self, sign_dict):
        """传入待签名的字典，返回签名后字符串
        1.字典排序
        2.拼接，用&连接，最后拼接上私钥
        3.MD5加密"""

        dict_keys = sign_dict.keys()
        dict_keys.sort()

        string = ''
        for key in dict_keys:
            if sign_dict[key] is None:
                pass
            else:
                string += '{0}={1}&'.format(key, sign_dict[key])
        string = string[0:len(string) - 1]
        string += self.priv_key
        string = string.replace(' ', '')

        hash_string = hashlib.md5()
        hash_string.update(string)
        return hash_string.hexdigest()

    def encrypt(self, befstr, encryway='MD5'):
        if self.pwd_key:
            befstr += self.pwd_key

        if encryway == 'MD5':
            hashstr = hashlib.md5()
        elif encryway == 'SHA1':
            hashstr = hashlib.sha1()
        else:
            log(__name__, '请输入正确的加密方式 MD5 或 SHA1')
            return None

        hashstr.update(befstr)
        return hashstr.hexdigest()

if __name__ == '__main__':
    print Encrypt(pwd_key='111111').encrypt('100000307', 'MD5')
    print Encrypt(pwd_key='').encrypt('100000307111111', 'MD5')