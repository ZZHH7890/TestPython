'''
Created on 2018年4月18日/下午2:17:04

@author: joker.zhang
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from web.Config.config import browser
from web.Common.logger import Logger

logger = Logger(logger="BasePage").getloger()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
    
    def open_browser(self, browser="Firefox"):
        logger.info("打开%s浏览器", browser)
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
            logger.info("打开浏览器是吧%s", msg)
            print(msg)
                     
    def find_element(self, *element):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_element(*element)
        except:
            logger.info("未能找到页面元素%s", element)
            print("未能找到页面元素", element)
        
    def input_text(self, element, text):
        logger.info("输入值为 %s", text)
        self.find_element(*element).send_keys(text)
    
    def click(self, element):
        logger.info("点击的元素为  %s", element)
        self.driver.find_element(*element).click()
    
    def get_page_title(self):
        logger.info("当前页面title %s", self.driver.title)
        return self.driver.title
    
    def move_to_element(self, element):
        element = self.find_element(*element)
        ActionChains(self.driver).move_to_element(element).perform()
        
