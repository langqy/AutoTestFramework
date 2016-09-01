# -*- coding: utf-8 -*-

import time


def save_time():
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


def save_date():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))















if __name__ == '__main__':
    print save_time()
    print save_date()