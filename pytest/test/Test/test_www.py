'''
Created on 2018年4月25日/上午9:20:10

@author: joker.zhang
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from web.PageObject.HomePage import HomePage
import pytest
from web.DataPro.conftest import *
from web.Config import config
from web.PageObject.BasePage import BasePage
from web.Common.logger import Logger
from web.Config.config import get_WWW_screen_shot

logger = Logger(logger="TestWWWCarrier").getloger()


class TestWWWCarrier():
    
    def setup_method(self, method):
        logger.info("打开浏览器")
        self.driver = BasePage.open_browser(self, config.browser)
        self.driver.implicitly_wait(30)
            
    def teardown_method(self, method):
        self.driver.close()
    
    # 测试新增中国运输商
    @pytest.mark.skip("Finish test_YQTabChina!")     
    @pytest.mark.parametrize('carrier_key, carrier_name, tracking_NO, expect_value', YQ_Tab_China_Key)
    def test_YQTabChina(self, carrier_key, carrier_name, tracking_NO, expect_value):
        logger.info("测试数据为：(%s %s %s %s)", carrier_key, carrier_name, tracking_NO, expect_value)
        home_page = HomePage(self.driver)
        select_carrier_page = home_page.go_to_select_carrier_page()
        # 点击中国运输商tab
        select_carrier_page.click_china_tab()
        
        # 用carrierKey拼装元素，用于选择运输商页面查找
        e_xpath = '//a[@class="yqc-carrier-msg yqc-express" and @yqdata-carrierkey' + '=' + carrier_key + ']'
        element = (By.XPATH, e_xpath)
        logger.info(element)
        
        # 页面滚动到新增运输商位置，并且截图
        select_carrier_page.take_carrier_page_screen(element, get_WWW_screen_shot())
        
        # 输入新增运输商名字进行搜索，并且截图
        select_carrier_page.search_carrier(carrier_name)
        select_carrier_page.take_search_page_screen(get_WWW_screen_shot())
        
        # 点击关闭按钮，关闭选择运输商页面，返回首页
        select_carrier_page.close_select_carrier_page()
        
        # 首页输入单号，跳转到物流跟踪页面
        logistics_track_page = home_page.go_to_logistics_track_page(tracking_NO)
        
        # 截图运单查询结果
        logistics_track_page.take_logistics_track_page_screen(get_WWW_screen_shot())
                
        assert home_page.get_home_page_title() == expect_value
 
    # 测试新增国际运输商  
    @pytest.mark.skip("Finish test_YQTabInternational!") 
    @pytest.mark.parametrize('carrier_key, carrier_name, tracking_NO, expect_value', YQ_Tab_International_Key)
    def test_YQTabInternational(self, carrier_key, carrier_name, tracking_NO, expect_value):
        logger.info("测试数据为：(%s %s %s %s)", carrier_key, carrier_name, tracking_NO, expect_value)
        home_page = HomePage(self.driver)
        select_carrier_page = home_page.go_to_select_carrier_page()
        # 点击国际运输商tab
        select_carrier_page.click_international_tab()
        
        # 用carrierKey拼装元素，用于选择运输商页面查找
        e_xpath = '//a[@class="yqc-carrier-msg yqc-express" and @yqdata-carrierkey' + '=' + carrier_key + ']'
        element = (By.XPATH, e_xpath)
        logger.info(element)
        
        # 页面滚动到新增运输商位置，并且截图
        select_carrier_page.take_carrier_page_screen(element, get_WWW_screen_shot())
        
        # 输入新增运输商名字进行搜索，并且截图
        select_carrier_page.search_carrier(carrier_name)
        select_carrier_page.take_search_page_screen(get_WWW_screen_shot())
        
        # 点击关闭按钮，关闭选择运输商页面，返回首页
        select_carrier_page.close_select_carrier_page()
        
        # 首页输入单号，跳转到物流跟踪页面
        logistics_track_page = home_page.go_to_logistics_track_page(tracking_NO)
        
        # 截图运单查询结果
        logistics_track_page.take_logistics_track_page_screen(get_WWW_screen_shot())
                
        assert home_page.get_home_page_title() == expect_value

    # 测试新增全球邮政 
    @pytest.mark.skip("Finish test_YQTabGlobalPost!") 
    @pytest.mark.parametrize('carrier_key, letter_sort, carrier_name, tracking_NO, expect_value', YQ_Tab_Global_Post_Key)
    def test_YQTabGlobalPost(self, carrier_key, letter_sort, carrier_name, tracking_NO, expect_value):
        home_page = HomePage(self.driver)
        select_carrier_page = home_page.go_to_select_carrier_page()
        
        # 用letter_sort拼装元素，用于点击全球邮政所在（A,B,C.....）
        e_letter_xpath = '//a[@class=" waves-effect" and text()=\"' + letter_sort + '\"]'
        letter_element = (By.XPATH, e_letter_xpath)
        # 点击全球邮政tab
        select_carrier_page.click_global_post_tab(letter_element)
        
        # 用carrierKey拼装元素，用于选择运输商页面查找
        e_xpath = '//a[@class="yqc-carrier-msg yqc-postal" and @yqdata-carrierkey' + '=' + carrier_key + ']'
        element = (By.XPATH, e_xpath)
        logger.info(element)
        
        # 页面滚动到新增运输商位置，并且截图
        select_carrier_page.take_carrier_page_screen(element, get_WWW_screen_shot())
        
        # 输入新增运输商名字进行搜索，并且截图
        select_carrier_page.search_carrier(carrier_name)
        select_carrier_page.take_search_page_screen(get_WWW_screen_shot())
        
        # 点击关闭按钮，关闭选择运输商页面，返回首页
        select_carrier_page.close_select_carrier_page()
        
        # 首页输入单号，跳转到物流跟踪页面
        logistics_track_page = home_page.go_to_logistics_track_page(tracking_NO)
        
        # 截图运单查询结果
        logistics_track_page.take_logistics_track_page_screen(get_WWW_screen_shot())
                
        assert home_page.get_home_page_title() == expect_value
