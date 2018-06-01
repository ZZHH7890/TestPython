'''
Created on 2018/4/18

@author: joker.zhang
'''
from selenium import webdriver

driver = webdriver.Chrome()
base_url = "https://user.17track.net/zh-cn"
driver.get(base_url)
driver.implicitly_wait(10)
driver.find_element_by_name('yq_login_name').send_keys('sellerjoker001@onts.cn')
driver.find_element_by_name('yq_login_pwd').send_keys('111111')
driver.find_element_by_id('yq-login-submit').click()
driver.implicitly_wait(30)
print(driver.title)
    
