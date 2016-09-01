# -*- coding: utf-8 -*-

from page_header import PageHeader
from selenium.webdriver.common.by import By


class PageUserCenterList(PageHeader):

    Loc_list_myorders = (By.CSS_SELECTOR, 'li#myOrders>a')
    Loc_list_userinfo = (By.CSS_SELECTOR, 'li#userInfo>a')
    Loc_list_realname = (By.CSS_SELECTOR, 'li#realName>a')
    Loc_list_address = (By.CSS_SELECTOR, 'li#address>a')
    Loc_list_myFavors = (By.CSS_SELECTOR, 'li#myFavors>a')

    def list_myorders(self):
        self.find_element(*self.Loc_list_myorders).click()

    def list_userinfo(self):
        self.find_element(*self.Loc_list_userinfo).click()

    def list_realname(self):
        self.find_element(*self.Loc_list_realname).click()

    def list_address(self):
        self.find_element(*self.Loc_list_address).click()

    def list_myfavors(self):
        self.find_element(*self.Loc_list_myFavors).click()


if __name__ == '__main__':
    from page_signin import PageSignIn

    sign = PageSignIn(browser=1, url='http://192.168.7.228/signin')
    sign.signin(username='13919093367', password='qqqq1111')
    u = PageUserCenterList(sign.get_driver())
    u.usercenter_myzhigou()
    u.list_address()
    u.wait(1)
    u.list_myorders()
    u.wait(1)
    u.list_realname()
    u.wait(1)
    u.list_userinfo()
    u.wait(1)
    u.list_myfavors()

    u.wait()
    u.quit()
