# -*- coding: utf-8 -*-

import win32gui
import win32con
import os
from time import sleep


class FileUpload(object):
    def __init__(self, element):
        self.Element = element
        self.window_open_flag = 0
        self.files = ''

    def __files(self, files):
        self.files = ''
        if type(files) == list:
            for f in files:
                self.files += '"{0}" '.format(f)
        elif type(files) == str:
            self.files = files

    def upload_by_win32(self, files):
        self._window_open()
        self.__files(files)

        # find upload window
        upload = win32gui.FindWindow('#32770', None)

        # find Edit
        ComboBoxEx32 = win32gui.FindWindowEx(upload, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)

        # find confirm button
        button = win32gui.FindWindowEx(upload, 0, 'Button', None)

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, self.files)
        win32gui.SendMessage(upload, win32con.WM_COMMAND, 1, button)

    def upload_by_autoit(self, files):
        self._window_open()
        self.__files(files)

        upfile = os.path.abspath('upfile_autoit.exe')
        os.system('{0} {1}'.format(upfile, self.files))  # 调用exe，上传文件

    def _window_open(self):
        if self.window_open_flag == 0:
            self.Element.click()
            sleep(1)

    def upload(self, files, way=1):
        self._window_open()
        if way == 1:
            self.upload_by_win32(files)
        elif way == 2:
            self.upload_by_autoit(files)
        else:
            raise



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://sahitest.com/demo/php/fileUpload.htm')
    File = FileUpload(driver.find_element_by_id('file'))
    File.upload_by_win32('d:\\baidu.py')
    File.upload_by_autoit(['d:\\1.html', 'd:\\baidu.py'])
    File.upload(['d:\\1.html', 'd:\\baidu.py'])
    sleep(2)
    driver.quit()

