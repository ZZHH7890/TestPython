'''
Created on 2018年6月4日/下午4:11:04

@author: joker.zhang
'''
'''
随意一人端开一部分牌，以端开部分最后一张点数以顺时针方向（大鬼为6，J为11，Q为12），
端牌人起数， 数到哪个人哪个人先拿牌，每人2张牌，先拿牌的人起叫。
过：
吃：只吃底注，输了只陪底注；
带：前面有多少人叫牌，就将他们的叫注全部吃进包括底注；
碰：以每人投底的最低限度为碰，
按以上例子为10元即加注10元。模拟牌局：
第一家：Q+7，叫吃；
第二家：红8+J，9点叫碰；
第三家：红7对，叫带；
第四家：2+2对，叫带。
以投底10元四人对战为例，开牌后第四家牌面最大通吃，
第一家吃底：赔40元，第二家叫碰：赔10元，
第三家叫带：底40元+第一家吃的40元+第二家碰的10元=90元，
第四家赢得前面三家综合再加上底注40元=180元。各种牌型叫法，按各玩家心理及各自牌面随意叫。
'''

'''
player_no：玩家号码
bottom_wager：底注
call_type：玩家叫牌类型（过/碰/吃/带）
'''


def get_score(player_no, bottom_wager, call_type, score):
    if call_type == '过':
        return [player_no, bottom_wager, call_type, score]
    elif call_type == '碰':
        return [player_no, bottom_wager + 10, call_type, score - 10]
    elif call_type == '吃':
        return [player_no, 2 * bottom_wager, call_type, score - bottom_wager]   
    elif call_type == '带':
        return [player_no, 2 * bottom_wager, call_type, score - bottom_wager]      
    
