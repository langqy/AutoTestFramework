# -*- coding: utf-8 -*-

from page_header import PageHeader
from selenium.webdriver.common.by import By


class PagePreOrder(PageHeader):

    Loc_add_addr = (By.CSS_SELECTOR, 'div.add_addr>a')

    Loc_back_to_cart = (By.CLASS_NAME, 'back_to_cart')
    Loc_sub_order = (By.ID, 'sub_order')

    def choose_addr(self, addr_id):
        Loc_addr = (By.CSS_SELECTOR, 'div[data-id="{0}"]'.format(addr_id))
        self.find_element(*Loc_addr).click()

    def back_to_cart(self):
        self.find_element(*self.Loc_back_to_cart).click()

    def submit_order(self):
        self.find_element(*self.Loc_sub_order).click()


if __name__ == '__main__':
    from page_signin import PageSignIn
    from page_product_list import PageProductList
    from page_cart import PageCart
    from page_product_detail import PageProductDetail

    sign = PageSignIn(browser=1, url='http://192.168.7.228/signin')
    sign.signin(username='13919093367', password='qqqq1111')
    h = PageProductList(sign.get_driver())
    h.productlist_5()
    h.product_detail(product_id=340)
    h.switch_to_window()
    p = PageProductDetail(h.get_driver())
    p.add_cart()
    p.to_cart()
    c = PageCart(p.get_driver())
    c.product_check(product_id=340)
    c.to_settle()

    s = PagePreOrder(c.get_driver())
    s.choose_addr(8299)
    s.back_to_cart()
    # s.submit_order()
    c.wait()
    c.quit()