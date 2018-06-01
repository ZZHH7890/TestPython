'''
Created on 2018年4月27日/下午4:28:55

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


@pytest.fixture(scope='module')
def set_up_module(request):
    print("only ones")
    driver = BasePage.open_browser(config.browser)
    driver.get("https://user.17track.net/zh-cn")
    driver.implicitly_wait(30)
    n = 5

    def tear_down_module():
        driver.close()

    request.addfinalizer(tear_down_module) 
    return n 


def test_a(set_up_module):
    n = set_up_module
    assert n == 5


def test_b(set_up_module):
    n = set_up_module
    assert n == 4    

