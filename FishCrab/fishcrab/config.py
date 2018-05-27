'''
Created on 2018年4月20日/上午10:42:14

@author: joker.zhang
'''
import time


# 生成当前日期
def get_now_time():
    time.sleep(1)
    now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    return now_time

