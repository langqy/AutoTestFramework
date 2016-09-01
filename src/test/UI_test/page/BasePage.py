# -*- coding: utf-8 -*-

from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from src.utils.browser import Browser


class ParameterError(Exception):
    pass


class BasePage:
    def __init__(self, driver=None, browser=1, url=''):
        self.driver = open_browser(browser=browser, url=url) if driver is None else driver
        self.current_window = self.driver.current_window_handle

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def wait(self, time=3):
        sleep(time)

    def execute(self, js):
        self.driver.execute_script(js)

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    # 寻找某元素
    def find_element_by_id(self, value):
        return self.driver.find_element_by_id(value)

    def find_element_by_name(self, value):
        return self.driver.find_element_by_name(value)

    def find_element_by_class_name(self, value):
        return self.driver.find_element_by_class_name(value)

    def find_element_by_tag_name(self, value):
        return self.driver.find_element_by_tag_name(value)

    def find_element_by_link_text(self, value):
        return self.driver.find_element_by_link_text(value)

    def find_element_by_partial_link_text(self, value):
        return self.driver.find_element_by_partial_link_text(value)

    def find_element_by_css_selector(self, value):
        return self.driver.find_element_by_css_selector(value)

    def find_element_by_xpath(self, value):
        return self.driver.find_element_by_xpath(value)

    # 寻找一组元素
    def find_elements_by_id(self, value):
        return self.driver.find_elements_by_id(value)

    def find_elements_by_name(self, value):
        return self.driver.find_elements_by_name(value)

    def find_elements_by_class_name(self, value):
        return self.driver.find_elements_by_class_name(value)

    def find_elements_by_tag_name(self, value):
        return self.driver.find_elements_by_tag_name(value)

    def find_elements_by_link_text(self, value):
        return self.driver.find_elements_by_link_text(value)

    def find_elements_by_partial_link_text(self, value):
        return self.driver.find_elements_by_partial_link_text(value)

    def find_elements_by_css_selector(self, value):
        return self.driver.find_elements_by_css_selector(value)

    def find_elements_by_xpath(self, value):
        return self.driver.find_elements_by_xpath(value)

    def switch_to_window(self, partial_url='', partial_title=''):
        '''切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则必须传入参数来确定要跳转到哪个窗口
        '''
        all_windows = self.driver.window_handles
        flag = 0
        if len(all_windows) == 1:
            print 'only 1 window!'
        elif len(all_windows) == 2:
            other_window = all_windows[1-all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
            flag = 1
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if not partial_url and not partial_title:
                    raise ParameterError('窗口多于三个，请传入参数定位window！')
                elif partial_url and partial_title and partial_url in self.driver.current_url and partial_title in self.driver.title:
                    flag = 1
                    break
                elif not partial_title and partial_url in self.driver.current_url:
                    flag = 1
                    break
                elif not partial_url and partial_title in self.driver.title:
                    flag = 1
                    break
        if flag:
            print self.driver.current_url, self.driver.title
        else:
            raise ParameterError('并无匹配的窗口，请检查传入参数！')

