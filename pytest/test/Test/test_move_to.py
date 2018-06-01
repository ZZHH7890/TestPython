'''
Created on 2018年4月23日/下午3:26:15

@author: joker.zhang
'''

from selenium import webdriver
from web.PageObject.LoginPage import LoginPage
import pytest
from web.DataPro.conftest import *
from web.Config import config
from web.PageObject.BasePage import BasePage
import time


class TestMove():
    
    def setup_method(self, method):
        self.driver = BasePage.open_browser(self, config.browser)
        self.driver.implicitly_wait(30)
            
    def teardown_method(self, method):
        self.driver.close()
    
    @pytest.mark.parametrize('login_email_text, login_pass_text, expect_value', login_info)
    def test_login(self, login_email_text, login_pass_text, expect_value):
        login_page_url = config.login_page_url
        login_page = LoginPage(self.driver, login_page_url)
        login_page.input_login_email(login_email_text)
        login_page.input_login_pass(login_pass_text)
        login_page.move_to_qq_btn()
        time.sleep(5)
        page_title = self.driver.title
        assert page_title == expect_value 
