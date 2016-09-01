# -*- coding: utf-8 -*-
"""创建一个自定义日志类，将代码中的错误格式化输出到统一的文件中"""
import datetime
import logging
import traceback

from config import DefaultConfig


def get_log_level():
    """获取日志文件的记录级别，日志中会记录所有大于等于此级别的信息"""
    try:
        log_level = DefaultConfig().get('log', 'level').upper()
    except:
        log_level = logging.ERROR
    return log_level


def get_log_file():
    """获取日志文件位置"""
    date = datetime.date.today()
    try:
        log_file = DefaultConfig().get('log', 'path') + 'test.' + str(date) + '.log'
    except:
        from src.utils import LOG_PATH
        log_file = LOG_PATH + 'test.' + str(date) + '.log'
    return log_file


def record_log(logger, message, level):
    """判断级别并输出日志"""
    log_file = get_log_file()
    error_level = level.lower()
    if error_level == 'critical':
        logger.critical(message)
    elif error_level == 'error':
        logger.error(message)
    elif error_level == 'warning':
        logger.warning(message)
    elif error_level == 'info':
        logger.info(message)
    else:
        logger.debug(message)

    # 如果不是自定义字符串，是exception的话，输出traceback
    if type(message) != str and type(message) != unicode:
        with open(log_file, 'a') as f:
            traceback.print_stack(file=f)
        traceback.print_stack()


def log(name, message, level='error'):
    """logger模块的log方法，提供标准输出到指定的日志，接受三个参数，报错位置、错误信息以及错误级别"""
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    if not logger.handlers:
        #  file handler, file输出的级别由配置文件中定义
        log_record_level = get_log_level()
        log_file = get_log_file()
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_record_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        #  console handler, console只输出ERROR和CRITICAL
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_record_level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    record_log(logger, message, level)


if __name__ == '__main__':
    log('Parser', 'hello', 'info')
    log('Parser', 'world', 'error')