# -*- coding: utf-8 -*-

import yaml
from src.utils.config import DefaultConfig
from src.utils.logger import Logger


class YamlReader(object):
    """Read yaml file"""
    def __init__(self, fname):
        self.logger = Logger(__name__).return_logger()
        self.fpath = '{}\\{}'.format(DefaultConfig().data_path, fname)

        self._read()

    def _read(self):
        with open(self.fpath, 'r') as f:
            self.yaml = [x for x in yaml.load_all(f)]



if __name__ == '__main__':
    y = YamlReader('test.yaml')
    for i in y.yaml:
        print i