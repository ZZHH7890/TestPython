'''
Created on 2018年4月18日/下午2:17:04

@author: joker.zhang
'''

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
              
    def find_element(self, *element):
        return self.driver.find_element(*element)
    
    def input_text(self, element, text):
        self.find_element(*element).send_keys(text)
    
    def click(self, element):
        self.driver.find_element(*element).click()
        
        
        
