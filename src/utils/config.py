# -*- coding: utf-8 -*-
"""解析配置文件，获取配置

实例化Config类，并传入相应config文件路径。可获取config文件中的配置项。

For example:

    cf = Config(path='D:\py\AutoTestFramework\config\config.ini')
    print cf.get('path', '')


实例化DefaultConfig类，可获取指定一些配置做为属性，可直接访问该属性，能够简便许多。

For example:

    cf = DefaultConfig()
    print cf.db_connect
    print cf.log_path

"""

import os
from ConfigParser import ConfigParser, NoSectionError, NoOptionError
from src.utils.utils_exception import ConfigFileException, ConfigError


# 获取当前文件绝对路径，从而获得config层路径
UTILS_PATH = os.path.split(os.path.realpath(__file__))[0]
CONFIG_PATH = UTILS_PATH + '\\..\\..\\config\\'  # config层


class Config(ConfigParser):
    def __init__(self, filename='config.ini'):
        ConfigParser.__init__(self)
        self.path = CONFIG_PATH + filename
        if os.path.exists(self.path):
            self.read(self.path)
        else:
            raise ConfigFileException('Config file not exists or not available.Please check {}.'.format(self.path))

    def _mysql_connect(self):
        """Get sqlalchemy database connection string."""
        return 'mysql+{0}://{1}:{2}@{3}:{4}/{5}?charset=utf8'.format(
            self.get('db', 'driver'),
            self.get('db', 'user'),
            self.get('db', 'pwd'),
            self.get('db', 'host'),
            self.get('db', 'port'),
            self.get('db', 'db_name')
        )

    def _oracle_connect(self):
        """Get Oracle database connection string."""
        return '{0}/{1}@{2}:{3}/{4}'.format(
            self.get('db', 'user'),
            self.get('db', 'pwd'),
            self.get('db', 'host'),
            self.get('db', 'port'),
            self.get('db', 'db_name')
        )

    @property
    def db_connect(self):
        db_driver = self.get('db', 'driver').lower()
        try:
            if db_driver == 'mysql':
                return self._mysql_connect()
            elif db_driver == 'oracle':
                return self._oracle_connect()
        except NoSectionError and NoOptionError:
            raise ConfigError('[db] section is required. And [db] section must have these options:'
                              '"driver", "user", "pwd", "host", "port", "db_name"')


class DefaultConfig(Config):
    """
        -properties:
            db_connect  : Return database string which can use to connect to database.
            base_path   : Return [path].base value.
            log_path    : Return [path].log value or default log path.
            report_path : Return [path].report value or default report path.
            data_path   : Return [path].data value or default data path.
            driver_path : Return default driver path.
    """
    def __init__(self):
        Config.__init__(self)

    @property
    def base_path(self):
        try:
            return self.get('path', 'base')
        except NoSectionError and NoOptionError:
            raise ConfigError('[path] section and "base" option is required.')

    @property
    def log_path(self):
        try:
            return self.get('path', 'log')
        except NoSectionError and NoOptionError:
            return self.base_path + '\\log\\'

    @property
    def report_path(self):
        try:
            return self.get('path', 'report')
        except NoSectionError and NoOptionError:
            return self.base_path + '\\report\\'

    @property
    def data_path(self):
        try:
            return self.get('path', 'data')
        except NoSectionError and NoOptionError:
            return self.base_path + '\\data\\'

    @property
    def driver_path(self):
        return self.base_path + '\\drivers\\'


if __name__ == '__main__':
    cf = Config()
    print cf.get('db', 'port')

    defaultcf = DefaultConfig()
    print defaultcf.db_connect

    print defaultcf.base_path
    print defaultcf.data_path
    print defaultcf.driver_path
    print defaultcf.log_path
    print defaultcf.report_path
