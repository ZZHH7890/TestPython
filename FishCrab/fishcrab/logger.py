#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2018年4月20日/下午11:28:03

@author: joker.zhang
'''
import logging  
import os.path  
import time 
from fishcrab.config import get_now_time


class Logger(object):

    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(__name__)
        if not self.logger.handlers:
            # log等级总开关
            self.logger.setLevel(logging.INFO)
            # 写入文件
            log_path = os.path.dirname(os.path.abspath('.')) + '\\log'
            if not os.path.exists(log_path):
                os.makedirs(log_path) 
            log_name = log_path + "\\" + get_now_time() + ".log"  
            logfile = log_name
            # 创建一个file_handler,指定utf-8
            fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
            # 输出到file的log等级开关
            fh.setLevel(logging.DEBUG)
            # 定义file_handler的输出格式
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d] %(funcName)s ')
            fh.setFormatter(formatter)
            # 将file_handler添加到logger
            self.logger.addHandler(fh)

    def getloger(self):      
        return self.logger
        
