#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2018年4月20日/下午11:28:03

@author: joker.zhang
'''
import logging  
import os.path  
import time 

def getloger():
    #创建一个logger
    logger = logging.getLogger(__name__)
    #log等级总开关
    logger.setLevel(logging.INFO)
    #写入文件
    now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.path.abspath('.')) + '\\web\\log'  
    log_name = log_path + "\\" + now_time + ".log"  
    logfile = log_name
    #创建一个file_handler,指定utf-8
    fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
    #输出到file的log等级开关
    fh.setLevel(logging.DEBUG)
    #定义file_handler的输出格式
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d] %(funcName)s ')
    fh.setFormatter(formatter)
    #将file_handler添加到logger
    logger.addHandler(fh)
    return logger
        
