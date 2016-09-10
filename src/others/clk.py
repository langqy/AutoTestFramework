# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from threading import Thread
from src.utils.config import DefaultConfig
import random
driver_path = DefaultConfig().driver_path


def clk(driver, url):
    """locate and click url"""
    locator = (By.XPATH, '//span[contains(text(), "{0}")]/../../../../a'.format(url))
    try:
        WebDriverWait(driver, 5, 0.5).until(EC.element_to_be_clickable(locator))
        try:
            moved_to_element = driver.find_element_by_xpath('//span[contains(text(), "{0}")]'.format(url))
            target_element = driver.find_element(*locator)
            ActionChains(driver).move_to_element(to_element=moved_to_element).click(target_element).perform()
            sleep(1)
            if 'm.baidu.com' in driver.current_url:
                target_element.click()
            return 1
        except:
            return 0
    except TimeoutException:
        return 0

KEYWORDS = [u'selenium 兼容 灰蓝', u'selenium 时间 灰蓝', u'selenium 文件上传 灰蓝', u'selenium 坑 灰蓝',
            u'selenium editor 灰蓝', u'selenium 结构设计 灰蓝', u'selenium ActionChains 灰蓝', u'selenium alert 灰蓝',
            u'selenium checkbox 灰蓝', u'selenium Select 灰蓝', u'selenium 网页内嵌 灰蓝', u'selenium 映射表 灰蓝',
            u'selenium 导航栏 灰蓝', u'selenium active_element 灰蓝', u'selenium close 灰蓝', u'selenium Keys 灰蓝',
            u'selenium 输出报告 示例 灰蓝', u'selenium autoit命令行 灰蓝']


def firefox(n):
    for i in range(n):
        driver = webdriver.Firefox()
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(random.choice(KEYWORDS), Keys.ENTER)
        print clk(driver, url='csdn')
        driver.close()
        sleep(1)


def chrome(n):
    for i in range(n):
        driver = webdriver.Chrome(executable_path=driver_path + 'chromedriver.exe')
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(random.choice(KEYWORDS), Keys.ENTER)
        print clk(driver, url='csdn')
        driver.close()
        sleep(1)


def ie(n):
    for i in range(n):
        driver = webdriver.Ie(executable_path=driver_path + 'IEDriverServer.exe')
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(random.choice(KEYWORDS), Keys.ENTER)
        clk(driver, url='csdn')
        driver.close()


def phantomjs(n):
    for i in range(n):
        driver = webdriver.PhantomJS(executable_path=driver_path + 'IEDriverServer.exe')
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(random.choice(KEYWORDS), Keys.ENTER)
        clk(driver, url='csdn')
        driver.close()


def flush(browser, n):
    for i in range(n):
        if browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser.lower() == 'chrome':
            driver = webdriver.Chrome(executable_path=driver_path + 'chromedriver.exe')
        elif browser.lower() == 'ie':
            driver = webdriver.Ie(executable_path=driver_path + 'IEDriverServer.exe')
        elif browser.lower() == 'phantomjs':
            driver = webdriver.PhantomJS(executable_path=driver_path + 'phantomjs.exe')
        driver.get('http://m.baidu.com')
        driver.find_element_by_id('index-kw').send_keys(random.choice(KEYWORDS), Keys.ENTER)
        clk(driver, url='csdn')
        sleep(1)
        print driver.find_element_by_class_name('article_t').text,
        print driver.find_element_by_xpath('//p[@class="date"]/i[2]').text
        # sleep(1)
        driver.close()
        # driver.quit()
        sleep(1)


if __name__ == '__main__':
    # for i in range(50):
    #     driver1 = webdriver.Firefox()
    #     driver1.get('http://m.baidu.com')
    #     driver1.find_element_by_id('index-kw').send_keys(u'selenium 文件上传 灰蓝', Keys.ENTER)
    #
    #     print clk(driver1, url='csdn')
    #
    #     # sleep(3)
    #     # print driver.current_url

    threads = []
    t1 = Thread(target=flush, args=('phantomjs', 10))
    threads.append(t1)
    t2 = Thread(target=flush, args=('phantomjs', 10))
    threads.append(t2)
    t3 = Thread(target=flush, args=('phantomjs', 10))
    threads.append(t3)
    t4 = Thread(target=flush, args=('phantomjs', 10))
    threads.append(t4)

    import os
    def killphantomjs():
        os.system('taskkill /f /im phantomjs.exe')

    # t_kill = Thread(target=killphantomjs, args=(60,))
    # threads.append(t_kill)

    for t in threads:
        t.setDaemon(False)
        t.start()


    # killphantomjs()
