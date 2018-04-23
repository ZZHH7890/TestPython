'''
Created on 2018年4月18日/下午2:40:01

@author: joker.zhang
'''
import unittest
from selenium import webdriver
from web.PageObject.LoginPage import LoginPage


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        print("START")
        self.driver = webdriver.Firefox()
        
    def tearDown(self):
        self.driver.close()
        print("OVER")
        
    def test_login(self):
        base_url = "https://user.17track.net/zh-cn"
        login_email_text = "sellerjoker001@onts.cn"
        login_pass_text = "111111"
        login_page = LoginPage(self.driver, base_url)
        self.driver.implicitly_wait(10)
        login_page.input_login_email(login_email_text)
        login_page.input_login_pass(login_pass_text)
        login_page.login()
        self.driver.implicitly_wait(30)
        print(self.driver.title)
        self.assertEqual(1, 2)
    
