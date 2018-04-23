'''
Created on 2018年4月18日/下午2:05:54

@author: joker.zhang
'''
from web.PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from web.PageObject.SellerCenterPage import SellerCenterPage
from web.Common.logger import Logger

logger = Logger(logger="LoginPage").getloger()


class LoginPage(BasePage):

    def __init__(self, driver, login_page_url):
        self.driver = driver
        self.base_url = login_page_url
        self.driver.get(self.base_url)
        
    login_name = (By.NAME, 'yq_login_name')
    login_pass = (By.NAME, 'yq_login_pwd')
    login_btn = (By.ID, 'yq-login-submit')
    qq_btn = (By.NAME, 'qq-btn')

    def input_login_email(self, text):
        logger.info("向%s输入值为 %s", self.login_name, text)
        self.input_text(self.login_name, text)
            
    def input_login_pass(self, text):
        logger.info("向%s输入值为 %s", self.login_pass, text)
        self.input_text(self.login_pass, text)

    def click_login_btn(self):
        self.click(self.login_btn)
    
    def click_qq_btn(self):
        self.click(self.qq_btn)
        
    def move_to_qq_btn(self):
        self.move_to_element(self.qq_btn)
    
    def go_to_seller_center_page(self):
        self.click(self.login_btn)
        return SellerCenterPage(self.driver)
    
    def get_current_page_title(self):
        return self.get_page_title()
    
    def take_qq_btn_screen_shot(self):
        self.take_screen(self.qq_btn)
        
