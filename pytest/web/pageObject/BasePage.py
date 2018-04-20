'''
Created on 2018年4月18日/下午2:17:04

@author: joker.zhang
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
    
    def open_browser(self, browser="Firefox"):
        try:
            if browser == "Firefox" :
                driver = webdriver.Firefox()
                return driver
            elif browser == "Chrome" :
                driver = webdriver.Chrome()
                return driver
            elif browser == "IE" :
                driver = webdriver.Ie()
                return driver
            else:
                print("找不到browser driver")
                
        except Exception as msg:
            print(msg)
                     
    def find_element(self, *element):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_element(*element)
        except:
            print("未能找到页面元素", element)
        
    def  input_text(self, element, text):
        self.find_element(*element).send_keys(text)
    
    def click(self, element):
        self.driver.find_element(*element).click()
        
        
        
