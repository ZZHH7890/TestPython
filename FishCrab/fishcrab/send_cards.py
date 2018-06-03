
'''
Created on 2018年5月27日/下午2:19:07

@author: joker.zhang
'''
import random
from fishcrab.logger import Logger
from builtins import int
from fishcrab.fish_crab_rule import judging_card
from operator import itemgetter

logger = Logger(__name__).getloger()

'''
   牌数：
《钓蟹》游戏使用一副扑克牌中的32张进行游戏，分别是：
　　红桃：2，4，5，6，7，8，9，10，J，Q
　　方片：2，4，5，6，7，8，9，10，J，Q
　　黑桃：3，4，6，7，8，10
　　梅花：4，6，7，8，10
　　大王（正司令）一张
'''


def send_cards():
    cardList = [('正司令', '大王'),
                ('梅花', '4'), ('梅花', '6'), ('梅花', '7'), ('梅花', '8'), ('梅花', '10'),
                ('黑桃', '3'), ('黑桃', '4'), ('黑桃', '6'), ('黑桃', '7'), ('黑桃', '8'), ('黑桃', '10'),
                ('方片', '2'), ('方片', '4'), ('方片', '5'), ('方片', '6'), ('方片', '7'), ('方片', '8'), ('方片', '9'), ('方片', '10'), ('方片', 'J'), ('方片', 'Q'),
                ('红桃', '2'), ('红桃', '4'), ('红桃', '5'), ('红桃', '6'), ('红桃', '7'), ('红桃', '8'), ('红桃', '9'), ('红桃', '10'), ('红桃', 'J'), ('红桃', 'Q') ]
    
    player_sum = input("请输入玩家人数：")
      
    logger.info("钓螃玩家人数为: (%s)", player_sum)
    
    play_card_num = 2 * int(player_sum)
    logger.info("发牌总数为: (%s)", play_card_num)
    
    cardRand = random.sample(cardList, play_card_num)
    logger.info("发牌的牌为: (%s)", cardRand)
    list_sort = []
    for i in range(0, play_card_num, 2):
        logger.info("循环中i的值为: (%s)", i)
        player_card = cardRand[i:i + 2]
        player_no = int(i / 2 + 1)
        player_card = [player_no] + judging_card(player_card)
        logger.info("第%s个玩家拿的牌为: (%s)", player_no, player_card)
        print(player_card)
        temp_tuple = tuple(player_card)
        list_sort.append(temp_tuple)
        
    list_sort = sorted(list_sort, key=itemgetter(4), reverse=True) 
    print(list_sort)   


if __name__ == '__main__':
    send_cards()
    
