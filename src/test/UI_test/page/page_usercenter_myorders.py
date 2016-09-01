# -*- coding: utf-8 -*-

from page_usercenter_list import PageUserCenterList
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class PageUserCenterMyOrders(PageUserCenterList):

    Loc_order_search_content = (By.ID, 'searchContent')
    Loc_order_search = (By.CSS_SELECTOR, 'a.btn.btn-default.btn-style')

    Loc_search_date = (By.CSS_SELECTOR, 'div.search-date select')
    Loc_search_order_status = (By.CSS_SELECTOR, 'div.search-orderStatus select')

    Loc_order_ids = (By.CSS_SELECTOR, 'span[ng-bind="order.order_id"]')

    def order_search(self, content):
        self.find_element(*self.Loc_order_search_content).clear()
        self.find_element(*self.Loc_order_search_content).send_keys(content)
        self.find_element(*self.Loc_order_search).click()

    def search_date(self, value):
        Select(self.find_element(*self.Loc_search_date)).select_by_value(value)

    def search_order_status(self, value):
        Select(self.find_element(*self.Loc_search_order_status)).select_by_value(value)

    def get_order_ids(self):
        pcmo.wait()
        return [order.text for order in self.find_elements(*self.Loc_order_ids)]

    def to_pay(self, order_id):
        all_orders = self.get_order_ids()
        print all_orders
        print order_id
        if order_id not in all_orders:
            raise NoSuchElementException('没有该订单，请传入正确的订单ID！')
        else:
            self.find_element(*(By.XPATH, '//span[text()={0}]/../../..'.format(order_id))).\
                find_element(*(By.XPATH, './/a[text()="立即支付"]')).click()

if __name__ == '__main__':
    from page_signin import PageSignIn

    sign = PageSignIn(browser=1, url='http://192.168.7.228/signin')
    sign.signin(username='13919093367', password='qqqq1111')
    u = PageUserCenterList(sign.get_driver())
    u.usercenter_myzhigou()

    pcmo = PageUserCenterMyOrders(u.get_driver())
    # pcmo.order_search(u'好牌大枣')
    pcmo.search_date('1')
    pcmo.search_order_status('2')
    pcmo.get_order_ids()

    pcmo.to_pay('20160810092651100555')
    u.driver.switch_to.frame()


    u.wait()
    u.quit()
