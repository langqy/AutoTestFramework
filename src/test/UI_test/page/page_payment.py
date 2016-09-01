# -*- coding: utf-8 -*-

from page_header import PageHeader
from selenium.webdriver.common.by import By


class PagePayment(PageHeader):

    Loc_password = (By.ID, 'password')
    Loc_sub_pay = (By.CSS_SELECTOR, 'div.pay-btn>button')

    def password(self, password):
        self.find_element(*self.Loc_password).clear()
        self.find_element(*self.Loc_password).send_keys(password)

    def pay(self):
        self.find_element(*self.Loc_sub_pay).click()


if __name__ == '__main__':
    from page_signin import PageSignIn
    from page_product_list import PageProductList
    from page_cart import PageCart
    from page_product_detail import PageProductDetail
    from page_preorder import PagePreOrder

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
    # s.back_to_cart()
    s.submit_order()

    pa = PagePayment(s.get_driver())
    pa.password('111111')
    pa.pay()
    c.wait()
    c.quit()