#coding:utf-8

import time

from src.utils import get_data
from src.utils import log
from src.utils import open_browser

driver = open_browser(1, 'http://192.168.7.228/signup')

phones = get_data('phone.xlsx')
for phone in phones:
    sign_phone = str(phone['phone'])
    driver.find_element_by_id('phone').clear()
    driver.find_element_by_id('phone').send_keys(sign_phone)
    driver.find_element_by_id('captcha-btn').click()
    time.sleep(2)
    if driver.find_element_by_id('captcha-btn').get_attribute('disabled'):
        log('signup {0}'.format(sign_phone), 'ok', 'INFO')
        time.sleep(60)
    else:
        log('signup {0}'.format(sign_phone), 'did not work', 'ERROR')


time.sleep(5)

driver.close()