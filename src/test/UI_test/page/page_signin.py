# -*- coding: utf-8 -*-

from BasePage import BasePage
from selenium.webdriver.common.by import By


class PageSignIn(BasePage):

    Loc_username = (By.ID, 'phone')
    Loc_password = (By.ID, 'password1')
    Loc_signinbtn = (By.ID, 'signin_btn')

    def signin(self, username, password):
        self.find_element(*self.Loc_username).send_keys(username)
        self.find_element(*self.Loc_password).send_keys(password)
        self.find_element(*self.Loc_signinbtn).click()


if __name__ == '__main__':
    sign = PageSignIn(browser=1, url='http://192.168.7.228/signin')
    sign.signin(username='13919093367', password='qqqq1111')
    sign.wait(1)
    sign.close()
