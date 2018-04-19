'''
Created on 2018年4月19日/下午4:34:30

@author: joker.zhang
'''

from selenium import webdriver
from web.pageObject.LoginPage import LoginPage
import pytest
from web.dataPro.conftest import *

class TestPara():
    
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
            
    def teardown_method(self, method):
        self.driver.close()
    
    
    @pytest.mark.parametrize('login_email_text, login_pass_text, expect_value', login_info)
    def test_login(self, login_email_text, login_pass_text, expect_value):
        base_url = "https://user.17track.net/zh-cn"
        login_page = LoginPage(self.driver, base_url)
        self.driver.implicitly_wait(10)
        login_page.input_login_email(login_email_text)
        login_page.input_login_pass(login_pass_text)
        login_page.login()
        self.driver.implicitly_wait(30)
        page_title =self.driver.title
        assert page_title == expect_value 