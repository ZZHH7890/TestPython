'''
Created on 2018年4月23日/上午9:59:04

@author: joker.zhang
'''
from web.PageObject.BasePage import BasePage
from web.PageObject.LogisticsTrackPage import LogisticsTrackPage
from selenium.webdriver.common.by import By


class SellerCenterPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        
    logistics_track_tab = (By.XPATH, '//*[@id="yq-site-navbar"]/ul/li[3]')
    
    def go_to_seller_logistics_track_page(self):
        self.click(self.logistics_track_tab)
        return LogisticsTrackPage(self.driver)
    
    def get_current_page_title(self):
        return self.get_page_title()
        
