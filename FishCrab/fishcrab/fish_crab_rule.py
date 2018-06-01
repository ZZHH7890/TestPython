
'''
Created on 2018年5月27日/上午10:18:12

@author: joker.zhang
'''
import random
from fishcrab.logger import Logger

logger = Logger(logger="BasePage").getloger()

'''
至尊宝(对皇帝)：由大王（正司令）与黑桃3 组成的特殊牌型，是所有牌型中最大的。
　　对子：两张点数相同的牌组成的牌型，在钓蟹里，这两张牌必须同为黑色或同为红色才可以组成对子，如红桃8+方块8可以成为一个对子，而红桃8+黑桃8则不能算作对子。
　　游戏中的对子包括：
　　（红桃Q+方块Q）[对天]、（红桃2+方块2）[对地]、（红桃8+方块8）、（红桃4+方块4）、（红桃6+ 方块6）、（红桃10+方块10）、（黑桃4+梅花4）、（红桃J+方块J）、（红桃7+方块7）、（黑桃10+梅花10）、（黑桃6+梅花6）、（红桃9+方块9）、（红桃5+方块5）、（黑桃7+梅花7）、（黑桃8+梅花8）。
　　天九：指任意花色的Q加上一张任意花色的9组成的牌型。
　　天九牌型包括：
　　（红桃Q+红桃9）（红桃Q+方块9）（方块Q+红桃9）（方块Q+方块9）
　　天八：指任意花色的Q加上一张任意花色的8组成的牌型。
　　天八牌型包括：
　　（红桃Q+红桃8）（红桃Q+方块8）（红桃Q+黑桃8）（红桃Q+梅花8）
　　（方块Q+红桃8）（方块Q+方块8）（方块Q+黑桃8）（方块Q+梅花8）
　　地八：指任意花色的2加上一张任意花色的8组成的牌型。
　　地八牌型包括：
　　（红桃2+红桃8）（红桃2+方块8）（红桃2+黑桃8）（红桃2+梅花8）
　　（方块2+红桃8）（方块2+方块8）（方块2+黑桃8）（方块2+梅花8）
　　杂牌：除开以上牌型的其他牌型。
'''


def card_type(player_card):
    if player_card == [('正司令', '大王'), ('黑桃', '3')]:
        print("皇帝")
        rank_value = 9999
        return rank_value 
    elif player_card == [('红桃', 'Q'), ('方块', 'Q')]:
        print("天牌对")
        rank_value = 9999
        return rank_value 
    elif player_card == [('红桃', '2'), ('方块', '2')]:
        print("地牌对")
    elif player_card == [('红桃', '8'), ('方块', '8')]:
        print("对红8") 
    elif player_card == [('红桃', '4'), ('方块', '4')]:
        print("对红4") 
    elif player_card == [('红桃', '6'), ('方块', '6')]:
        print("对红6") 
    elif player_card == [('红桃', '10'), ('方块', '10')]:
        print("对红10")  
    elif player_card == [('黑桃', '4'), ('梅花', '4')]:
        print("对黑4") 
    elif player_card == [('红桃', 'J'), ('方块', 'J')]:
        print("对红J") 
    elif player_card == [('红桃', '7'), ('方块', '7')]:
        print("对红7") 
    elif player_card == [('黑桃', '10'), ('梅花', '10')]:
        print("对黑10")  
    elif player_card == [('黑桃', '6'), ('梅花', '6')]:
        print("对黑6") 
    elif player_card == [('红桃', '9'), ('方块', '9')]:
        print("对红9") 
    elif player_card == [('红桃', '5'), ('方块', '5')]:
        print("对红5") 
    elif player_card == [('黑桃', '7'), ('梅花', '7')]:
        print("对黑7") 
    elif player_card == [('黑桃', '8'), ('梅花', '8')]:
        print("对黑8")
    elif player_card == [('红桃', 'Q'), ('红桃', '9')] or player_card == [('红桃', 'Q'), ('方块', '9')] or player_card == [('方块', 'Q'), ('红桃', '9')] or player_card == [('方块', 'Q'), ('方块', '9')]:
        print("天九牌")                                  
    elif player_card == [('红桃', 'Q'), ('红桃', '8')] or player_card == [('红桃', 'Q'), ('方块', '8')] or player_card == [('方块', 'Q'), ('红桃', '8')] or player_card == [('方块', 'Q'), ('方块', '8')] or player_card == [('红桃', 'Q'), ('黑桃', '8')] or player_card == [('红桃', 'Q'), ('梅花', '8')] or player_card == [('方块', 'Q'), ('黑桃', '8')] or player_card == [('方块', 'Q'), ('梅花', '8')]:
        print("天八牌") 
    elif player_card == [('红桃', '2'), ('红桃', '8')] or player_card == [('红桃', '2'), ('方块', '8')] or player_card == [('方块', '2'), ('红桃', '8')] or player_card == [('方块', '2'), ('方块', '8')] or player_card == [('红桃', '2'), ('黑桃', '8')] or player_card == [('红桃', '2'), ('梅花', '8')] or player_card == [('方块', '2'), ('黑桃', '8')] or player_card == [('方块', '2'), ('梅花', '8')]:
        print("地八牌")                                                
    else:
        print("杂牌算点数") 


if __name__ == '__main__':
    player_card = [('方块', 'Q'), ('红桃', '9')]
    card_type(player_card)           
