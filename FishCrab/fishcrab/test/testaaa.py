'''
Created on 2018年6月1日/下午5:10:15

@author: joker.zhang
'''

# 扑克牌大小
while True:
    try:
        line = input()
        line0 , line1 = line[0].split() , line[1].split()

        def transJQKA2(line):
            for i in range(len(line)):
                if line[i] == 'J':
                    line[i] = 11
                if line[i] == 'Q':
                    line[i] = 12
                if line[i] == 'K':
                    line[i] = 13
                if line[i] == 'A':
                    line[i] = 14
                if line[i] == '2':
                    line[i] = 15
            return line

        line0 , line1 = transJQKA2(line0) , transJQKA2(line1)
        if line[0] == 'joker JOKER' or line[1] == 'joker JOKER':
            print('jokerJOKER') 
        elif len(line0) == len(line1):
            if int(line0[0]) > int(line1[0]):
                print(line[0])
            else:
                print(line[1]) 
        elif len(line0) == 4:
            print(line[0]) 
        elif len(line1) == 4:
            print(line[1]) 
        else:
            print('ERROR') 
    except:
        break
