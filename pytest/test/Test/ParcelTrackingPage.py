'''
Created on 2018年4月23日/上午10:09:49

@author: joker.zhang

'''
from web.PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from web.PageObject.SelectCarrierPage import SelectCarrierPage
from selenium.webdriver.support.wait import WebDriverWait
from web.Common import my_expected_conditions as my_EC
from web.Common.logger import Logger

logger = Logger(logger="ParcelTrackingPage").getloger()


# 首页输入单号点击查询按钮，跳转到的物流跟踪页面
class ParcelTrackingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver 
        js = 'localStorage.setItem("tourDone", true);'
        self.excecute_js(js) 
        
    # 运单列表只有一个查询结果时文本位置    
    search_result = (By.XPATH, '//div[@class ="yqcr-ps yq-track-order"]/div/p[2]')
    
    # 点击页面右上角添加查询单号加号按钮
    add_tracking_no_btn = (By.XPATH, '//div[@class ="navbar-header pull-right"]/ul/li[5]')  
    
    # 点击右上角加号按钮后，弹出的输入查询单号文本框    
    track_box = (By.XPATH, '//pre[@class = " CodeMirror-line "]')
    
    # 添加按钮
    add_btn = (By.XPATH, '//div[@class ="yq-more-track-container"]/div[2]/button')
    
    # 查询结果列表，第一个结果的运输商位置
    carrier_location = (By.XPATH, '//div[@class = "from"]/div/div/i')
    
    # 查询结果列表，第一个结果的删除按钮位置
    remove_order_btn = (By.XPATH, '//button[@cmd ="delTrackNo"]')
    
    # 点击删除按钮后，提示页面中确认按钮位置
    confirm_del_btn = (By.XPATH, '//div[@class="modal-footer"]/button[2]')
    
    # 向导关闭按钮，第一次查询运单会出现查询向导
    close_guide_btn = (By.XPATH, '//a[@class ="introjs-button introjs-skipbutton"]')
    
    # 向文本框中输入查询单号
    def input_track_NO(self, text):
        self.click(self.add_tracking_no_btn)
        self.input_text_by_action(self.track_box, text)
        self.click(self.add_btn)
        
    # 点击查询按钮
    def click_track_btn(self):
        self.click(self.track_btn) 
        
    # 点击第一个结果的运输商位置，跳转到选择运输商页面
    def go_to_select_carrier_page(self):
        self.click(self.carrier_location)
        return SelectCarrierPage(self.driver)
    
    # 删除查询结果中第一个运单结果（最上面）
    def remove_order(self):
        self.move_to_element(self.search_result)
        self.click(self.remove_order_btn)
        # 点击删除按钮后，需要点击确认按钮
        self.click(self.confirm_del_btn)
    
    # 先判断页面中查询中状态是否改变，然后截取物流跟踪页面全屏
    def take_parcel_tracking_page_screen(self, screen_shot):
        text_temp = "查询中"
        WebDriverWait(self.driver, 30).until(my_EC.text_to_be_present_not_in_element(self.search_result, text_temp))
        self.take_full_screen(screen_shot)
    
    # 返回上一个页面
    def back_last_page(self):
        self.back()    
        
    def get_parcel_tracking_page_title(self):
        return self.get_page_title()
    
    # 获取单个运单查询结果文字
    def get_search_result_text(self):
        search_result_text = self.get_element_text(self.search_result)
        return search_result_text
    
    # 点击向导关闭按钮
    def click_close_guide_btn(self):
        if self.is_element_located(self.close_guide_btn, 5):
            self.click(self.close_guide_btn)
            logger.info("查询向导出现，点击成功")  
        else:
            logger.info("查询向导没有出现，不用点击")    
     
