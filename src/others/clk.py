# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def clk(driver, url):
    """locate and click url"""
    locator = (By.XPATH, '//span[contains(text(), "{0}")]/../../../../a'.format(url))
    try:
        WebDriverWait(driver, 5, 0.5).until(EC.element_to_be_clickable(locator))
        try:
            moved_to_element = driver.find_element_by_xpath('//span[contains(text(), "{0}")]'.format(url))
            target_element = driver.find_element(*locator)
            ActionChains(driver).move_to_element(to_element=moved_to_element).click(target_element).perform()
            from time import sleep
            sleep(1)
            if 'm.baidu.com' in driver.current_url:
                target_element.click()
            return 1
        except:
            return 0
    except TimeoutException:
        return 0

import time
import thread
from threading import Thread
from src.utils.config import DefaultConfig
driver_path = DefaultConfig().driver_path

# class BrowserTread(Thread):
#     def __init__(self, name, n):
#         Thread.__init__(self,name=name)
#         self.n = n

def firefox(n):
    for i in range(n):
        driver1 = webdriver.Firefox()
        driver1.get('http://m.baidu.com')
        driver1.find_element_by_id('index-kw').send_keys(u'selenium 文件上传 灰蓝', Keys.ENTER)
        print clk(driver1, url='csdn')
        driver1.close()
    # thread.exit_thread()

def chrome(n):
    for i in range(n):
        driver = webdriver.Chrome(executable_path=driver_path + 'chromedriver.exe')
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(u'selenium 文件上传 灰蓝', Keys.ENTER)
        print clk(driver, url='csdn')
        driver.close()
    # thread.exit_thread()

def ie(n):
    for i in range(n):
        driver = webdriver.Chrome(executable_path=driver_path + 'IEDriverServer.exe')
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(u'selenium 文件上传 灰蓝', Keys.ENTER)
        print clk(driver, url='csdn')
        driver.close()
        # thread.exit_thread()



if __name__ == '__main__':
    # import threading
    # for i in range(50):
    #     threading.
    #     driver1 = webdriver.Firefox()
    #     driver1.get('http://m.baidu.com')
    #     driver1.find_element_by_id('index-kw').send_keys(u'selenium 文件上传 灰蓝', Keys.ENTER)
    #
    #     print clk(driver1, url='csdn')
    #
    #     # sleep(3)
    #     # print driver.current_url
    #
    #     driver1.close()
    # threads = []
    # thread1 = BrowserTread('firefox', 50)
    # thread1.firefox()
    # # thread1.join()
    #
    # thread2 = BrowserTread('chrome', 50)
    # thread2.chrome()
    # # thread2.join()
    #
    # thread3 = BrowserTread('ie', 50)
    # thread3.ie()
    # thread3.join()

    # t1 = BrowserTread

    threads = []
    t1 = Thread(target=firefox, args=(100,))
    threads.append(t1)
    t2 = Thread(target=chrome, args=(200,))
    threads.append(t2)
    # t3 = Thread(target=ie, args=(50,))
    # threads.append(t3)

    for t in threads:
        t.setDaemon(False)
        t.start()

