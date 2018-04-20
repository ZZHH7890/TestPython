'''
Created on 2018年4月18日/下午2:05:54

@author: joker.zhang
'''
from web.pageObject.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver, login_page_url):
        self.driver = driver
        self.base_url = login_page_url
        self.driver.get(self.base_url)
        
    login_name = (By.NAME, 'yq_login_name')
    login_pass = (By.NAME, 'yq_login_pwd')
    login_btn = (By.ID, 'yq-login-submit')

    def input_login_email(self, text):
        self.input_text(self.login_name, text)
            
    def input_login_pass(self, text):
        self.input_text(self.login_pass, text)

    def login(self):
        self.click(self.login_btn)
        
        
