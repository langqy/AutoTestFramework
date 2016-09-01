# -*- coding: utf-8 -*-

from page_header import PageHeader
from selenium.webdriver.common.by import By


class ParameterError(Exception):
    pass


class PageProductList(PageHeader):

    Loc_sort_operation_1 = (By.CSS_SELECTOR, 'div.products-operations div:nth-child(1)')
    Loc_sort_operation_2 = (By.CSS_SELECTOR, 'div.products-operations div:nth-child(2)')
    Loc_sort_operation_3 = (By.CSS_SELECTOR, 'div.products-operations div:nth-child(3)')
    Loc_sort_operation_4 = (By.CSS_SELECTOR, 'div.products-operations div:nth-child(4)')
    Loc_isquantity = (By.ID, 'isquantity')

    def sort_1(self):
        self.find_element(*self.Loc_sort_operation_1).click()

    def sort_2(self):
        self.find_element(*self.Loc_sort_operation_2).click()

    def sort_3(self):
        self.find_element(*self.Loc_sort_operation_3).click()

    def sort_4(self):
        self.find_element(*self.Loc_sort_operation_4).click()

    def show_have_quantity(self):
        self.find_element(*self.Loc_isquantity).click()

    def product_detail(self, product_id=None, product_name=None):
        if product_id:
            Loc_by_productid = (By.CSS_SELECTOR, 'div.result-list a[href$="/{0}"]'.format(product_id))
            self.find_element(*Loc_by_productid).click()
        elif product_name:
            Loc_by_productname = (By.CSS_SELECTOR, 'div.result-list p[title*="{0}"]'.format(product_name))
            self.find_element(*Loc_by_productname).click()
        else:
            self.quit()
            raise ParameterError('参数product_id和product_name不可均为None！')


if __name__ == '__main__':
    p = PageProductList(PageHeader(browser=1, url='http://192.168.7.228/').get_driver())
    p.productlist_3()
    # p.sort_4()
    # p.show_have_quantity()
    # p.show_have_quantity()
    # p.sort_1()
    # p.product_detail(product_id=348)
    p.product_detail(product_name='奇葩规格大米2')
    p.product_detail(product_name='大米')
    p.switch_to_window(partial_url='348', partial_title=u'奇葩规格')
    # p.product_detail()
    p.wait(1)
    p.quit()