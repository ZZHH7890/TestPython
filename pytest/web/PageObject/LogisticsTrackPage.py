'''
Created on 2018年4月23日/上午10:09:49

@author: joker.zhang
'''
from web.PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By


class LogisticsTrackPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        
    def get_current_page_title(self):
        return self.get_page_title()
        
        
