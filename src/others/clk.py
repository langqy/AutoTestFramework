# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
driver.get('http://m.baidu.com')
driver.implicitly_wait(30)

driver.find_element_by_id('index-kw').send_keys('python',Keys.ENTER)

def clk(driver, url):
    try:
        WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="{0}"]/../../a'.format(url))))
        try:
            driver.find_element_by_xpath('//span[text()="{0}"]/../../a'.format(url)).click()
            return 1
        except:
            return 0
    except TimeoutException:
        return 0


clk(driver, url='www.python.org')

from time import sleep

sleep(3)

print driver.current_url

driver.close()