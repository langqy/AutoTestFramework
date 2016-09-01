# -*- coding: utf-8 -*-

from page_header import PageHeader
from selenium.webdriver.common.by import By


class PageCart(PageHeader):

    Loc_to_settle = (By.ID, 'settle_btn')
    Loc_checkall = (By.ID, 'checkAll')

    def product_check(self, product_id):
        Loc_product_checkbox = (By.CSS_SELECTOR, 'input[id$=_{0}]'.format(product_id))
        self.find_element(*Loc_product_checkbox).click()

    def check_all(self):
        self.find_element(*self.Loc_checkall).click()

    def to_settle(self):
        self.find_element(*self.Loc_to_settle).click()


if __name__ == '__main__':
    from page_signin import PageSignIn
    from page_product_list import PageProductList

    sign = PageSignIn(browser=1, url='http://192.168.7.228/signin')
    sign.signin(username='13919093367', password='qqqq1111')
    h = PageProductList(sign.get_driver())
    h.cart()
    c = PageCart(h.get_driver())
    c.product_check(product_id=340)
    c.check_all()
    # c.to_settle()
    c.wait()
    c.quit()