'''
Created on 2018年4月23日/上午9:56:51

@author: joker.zhang
'''

from selenium import webdriver
import time
from web.PageObject.LoginPage import LoginPage
import pytest
from web.DataPro.conftest import *
from web.Config import config
from web.PageObject.BasePage import BasePage
from web.Common.logger import Logger

logger = Logger(logger="BasePage").getloger()


class TestSeller():
    
    def setup_method(self, method):
        logger.info("打开浏览器")
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
        seller_center_page = login_page.go_to_seller_center_page()
        seller_center_page.take_logistics_track_tab_screen_shot()
        logger.info(seller_center_page.get_seller_center_page_title())
        time.sleep(5)
        logistics_track_page = seller_center_page.go_to_seller_logistics_track_page()
        page_title = logistics_track_page.get_logistics_track_page_title()
        time.sleep(2)
        logger.info(page_title)
        assert page_title == expect_value 
