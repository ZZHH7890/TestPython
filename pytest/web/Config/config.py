'''
Created on 2018年4月20日/上午10:42:14

@author: joker.zhang
'''
import time
import os.path

browser = "Firefox"

excel_path = os.path.dirname(os.path.abspath('.')) + "\\web\\TestData\\testData.xlsx"
login_page_url = "https://user.17track.net/zh-cn"
test_case_path = os.path.dirname(os.path.abspath('.')) + '\\web\\TestCases'
report_path = os.path.dirname(os.path.abspath('.')) + '\\web\\Report'
now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
web_report_name = "web_testReport_"+now_time+".html"
test_report = report_path + "\\" + web_report_name
pytest_cmd_path = test_case_path + " -q --html=" + test_report
