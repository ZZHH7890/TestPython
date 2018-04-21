'''
Created on 2018年4月19日/下午7:08:45

@author: joker.zhang
'''
avalue = 'aa'
myTuple =(avalue,)
yourTuple =("bbc",)
myList = [('aa','bb')]
afterTuple = myTuple + yourTuple
aaTuple = (afterTuple,)
afterList = myList.append(aaTuple)
print(afterTuple)
print(afterList)