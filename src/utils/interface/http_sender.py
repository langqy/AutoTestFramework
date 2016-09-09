# -*- coding: utf-8 -*-

import requests
import json
from src.utils.logger import Logger
from src.utils.utils_exception import UnSupportMethod

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class HTTPSender(object):

    def __init__(self, url, method='GET', headers=None, cookie=None):
        """

        :param method:
        :param headers: Must be a dict. Such as headers={'Content_Type':'text/html'}
        """
        self.logger = Logger(__name__).return_logger()

        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        self.headers = headers
        self.cookie = cookie

        self._set_header()
        self._set_cookie()

    def _set_header(self):
        """设置header"""
        if self.headers:
            self.session.headers.update(self.headers)
            self.logger.info('Set headers: {0}'.format(self.headers))

    def _set_cookie(self):
        """设置cookie"""
        if self.cookie:
            self.session.cookies.update(self.cookie)
            self.logger.info('Set cookies: {0}'.format(self.cookie))

    def _check_method(self):
        """检查传入的method是否可用。"""
        if self.method not in METHODS:
            self.logger.exception(UnSupportMethod(u'不支持的method:{0}，请检查传入参数！'.format(self.method)))
        else:
            return True

    def send(self, params=None, data=None, **kwargs):
        """send request to url.If response 200,return response, else return None."""
        if self._check_method():
            response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
            self.logger.info('{0} {1}.'.format(self.method, self.url))
            if response.status_code == 200:
                self.logger.info('request success: {0}\n{1}'.format(response, response.content.strip()))
                return response
            else:
                self.logger.error('request failed: {0} {1}'.format(response, response.reason))


if __name__ == '__main__':
    sender = HTTPSender('http://www.baidu.com', 'get')
    res = sender.send()
    print res.status_code
    print res.content

