# -*- coding: utf-8 -*-

from page_header import PageHeader
from selenium.webdriver.common.by import By


class PageProductDetail(PageHeader):

    Loc_buy_now = (By.CLASS_NAME, 'btn_one_click')
    Loc_add_cart = (By.ID, 'btn_add_cart')
    Loc_to_cart = (By.CSS_SELECTOR, 'div#addCartModal a')

    Loc_number_add = (By.CLASS_NAME, 'item_add')
    Loc_number_dec = (By.CLASS_NAME, 'item_dec')
    Loc_number = (By.ID, 'quantity')

    Loc_shop_name = (By.CSS_SELECTOR, 'div.shop_name a')

    def number_add(self):
        self.find_element(*self.Loc_number_add).click()

    def number_dec(self):
        self.find_element(*self.Loc_number_dec).click()

    def number_modify(self, num):
        self.find_element(*self.Loc_number).clear()
        self.find_element(*self.Loc_number).send_keys(num)

    def buy_now(self):
        self.find_element(*self.Loc_buy_now).click()

    def add_cart(self):
        self.find_element(*self.Loc_add_cart).click()

    def to_shop(self):
        self.find_element(*self.Loc_shop_name).click()

    def to_cart(self):
        self.find_element(*self.Loc_to_cart).click()


if __name__ == '__main__':
    from page_signin import PageSignIn
    from page_product_list import PageProductList
    sign = PageSignIn(browser=1, url='http://192.168.7.228/signin')
    sign.signin(username='13919093367', password='qqqq1111')
    h = PageProductList(sign.get_driver())
    h.productlist_5()
    h.product_detail(product_id=340)
    h.switch_to_window()
    p = PageProductDetail(h.get_driver())
    p.number_add()
    # p.wait(1)
    # p.number_dec()
    # p.wait(1)
    # p.number_modify(10)
    # p.wait(1)
    # p.buy_now()
    p.add_cart()
    p.to_cart()
    # p.to_shop()
    p.wait()
    p.quit()