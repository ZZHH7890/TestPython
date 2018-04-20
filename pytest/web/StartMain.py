'''
Created on 2018年4月18日/下午2:53:48

@author: joker.zhang
'''
import unittest
import pytest
from web.testCases.TestLoginPage import TestLoginPage
from web.common import HTMLTestRunner
import time
from web.pageObject.LoginPage import LoginPage
from web.Config import config

#unittest 入口
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestLoginPage('test_login'))
#     reportPath = "C:\\Users\\17TRACK\\eclipse-workspace\\TestPython\\pytest\\report\\"
#     nowTime = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
#     reportName = "testReport_"+nowTime+".html"
#     testReport = reportPath + reportName
#     fp = open(testReport, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="我的", description="你的")
#     runner.run(suite)

#pytest 入口
if __name__ == '__main__':
    pytest.main(config.pytest_cmd_path)
