'''
Created on 2018年4月25日/上午10:08:37

@author: joker.zhang
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://carrierlist.17track.net/zh-cn")
driver.find_element_by_xpath('//a[@class=" waves-effect" and text()="全球邮政"]').click()
element = (By.XPATH, '//p[@title="Macau Post"]')

# s = driver.find_elements_by_xpath('//p[@title="Albanian Post"]')
s = driver.find_elements(*element)
print(s[0])
driver.execute_script("arguments[0].scrollIntoView();", s[0])

time.sleep(10)
driver.close()
