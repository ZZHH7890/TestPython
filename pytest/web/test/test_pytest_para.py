'''
Created on 2018年4月19日/下午2:48:39

@author: joker.zhang
'''
from selenium import webdriver
from web.PageObject.LoginPage import LoginPage
import pytest
import time

class TestPara():
    login_info =[('sellerjoker001@onts.cn','111111','卖家中心 | 17TRACK'),
             ('buyerjoker001@onts.cn','111111','控制台 | 17TRACK'),
             ('buyerjoker002@onts.cn','111111','卖家中心 | 17TRACK')]
    
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
            
    def teardown_method(self, method):
        self.driver.close()
    
    
    @pytest.mark.parametrize('login_email_text, login_pass_text, expect_value', login_info)
    def test_login(self, login_email_text, login_pass_text, expect_value):
        base_url = "https://user.17track.net/zh-cn"
        login_page = LoginPage(self.driver, base_url)
        self.driver.implicitly_wait(10)
        login_page.input_login_email(login_email_text)
        login_page.input_login_pass(login_pass_text)
        login_page.login()
        self.driver.implicitly_wait(30)
        page_title =self.driver.title
        assert page_title == expect_value 
        
#     @pytest.mark.parametrize('login_email_text, login_pass_text, expect_value', login_info)
#     def test_login(self, login_email_text, login_pass_text, expect_value):
#         driver = self.driver
#         driver.get(self.base_url)
#         driver.implicitly_wait(10)
#         driver.find_element_by_name('yq_login_name').send_keys(login_email_text)
#         driver.find_element_by_name('yq_login_pwd').send_keys(login_pass_text)
#         driver.find_element_by_id('yq-login-submit').click()
#         driver.implicitly_wait(30)
#         page_title =driver.title
#         assert page_title == expect_value  

              
# 
if __name__ == '__main__':
    reportPath = "C:\\Users\\Administrator\\eclipse-workspace\\YQTrack.Test.Automation\\Web_Automation\\web\\Report\\report\\"
    nowTime = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    reportName = "testReport_"+nowTime+".html"
    testReport = reportPath + reportName
    cmdPath = "-q --html=" + testReport
    pytest.main(cmdPath)
       
