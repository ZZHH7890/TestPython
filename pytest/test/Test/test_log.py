
'''
Created on 2018年4月21日/下午6:57:59

@author: joker.zhang
'''

import logging
 
 
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(pathname)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s ',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename=r'C:\Users\Administrator\eclipse-workspace\TestPython\pytest\web\log\log.log', filemode='w')
 
 
def login():
    while True:
        try:
            name = input('Input user name:')
            password = int(input('Input password:')) # 这里故意转成整型，触发异常
            if name == 'andy' and password == 'nopasswd':
                print('logging succeed!')
        except ValueError as e:
            logging.debug(e)
            break
 
if __name__ == '__main__':
    login()