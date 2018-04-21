'''
Created on 2018年4月18日

@author: joker.zhang
'''
import unittest
from web.Common import HTMLTestRunner
from test.FirstWebDriver import FirstWebDriver

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstWebDriver('test_login'))
    htmlPath = "C:\\Users\\17TRACK\\eclipse-workspace\\pytest\\report\\testReport.html"
    fp = open(htmlPath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="我的", description="你的")
    runner.run(suite)