'''
Created on 2018/4/18

@author: joker.zhang
'''
import unittest
from selenium import webdriver


class FirstWebDriver(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://user.17track.net/zh-cn"
        
    def tearDown(self):
        self.driver.close()
        
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(10)
        driver.find_element_by_name('yq_login_name').send_keys('sellerjoker001@onts.cn')
        driver.find_element_by_name('yq_login_pwd').send_keys('111111')
        driver.find_element_by_id('yq-login-submit').click()
        self.driver.implicitly_wait(30)
        print(self.driver.title)
        self.assertEqual(1, 2)

    

    
