
'''
Created on 2018年5月27日/上午10:18:12

@author: joker.zhang
'''
from fishcrab.logger import Logger
from builtins import int

logger = Logger(__name__).getloger()

'''
至尊宝(对皇帝)：由大王（正司令）与黑桃3 组成的特殊牌型，是所有牌型中最大的。
　　对子：两张点数相同的牌组成的牌型，在钓蟹里，这两张牌必须同为黑色或同为红色才可以组成对子，如红桃8+方片8可以成为一个对子，而红桃8+黑桃8则不能算作对子。
　　游戏中的对子包括：
　　（红桃Q+方片Q）[对天]、（红桃2+方片2）[对地]、（红桃8+方片8）、（红桃4+方片4）、（红桃6+ 方片6）、（红桃10+方片10）、（黑桃4+梅花4）、（红桃J+方片J）、（红桃7+方片7）、（黑桃10+梅花10）、（黑桃6+梅花6）、（红桃9+方片9）、（红桃5+方片5）、（黑桃7+梅花7）、（黑桃8+梅花8）。
　　天九：指任意花色的Q加上一张任意花色的9组成的牌型。
　　天九牌型包括：
　　（红桃Q+红桃9）（红桃Q+方片9）（方片Q+红桃9）（方片Q+方片9）
　　天八：指任意花色的Q加上一张任意花色的8组成的牌型。
　　天八牌型包括：
　　（红桃Q+红桃8）（红桃Q+方片8）（红桃Q+黑桃8）（红桃Q+梅花8）
　　（方片Q+红桃8）（方片Q+方片8）（方片Q+黑桃8）（方片Q+梅花8）
　　地八：指任意花色的2加上一张任意花色的8组成的牌型。
　　地八牌型包括：
　　（红桃2+红桃8）（红桃2+方片8）（红桃2+黑桃8）（红桃2+梅花8）
　　（方片2+红桃8）（方片2+方片8）（方片2+黑桃8）（方片2+梅花8）
　　杂牌：除开以上牌型的其他牌型。
'''


def judging_card(player_card):
    
    if player_card == [('正司令', '大王'), ('黑桃', '3')] or [('黑桃', '3'), ('正司令', '大王')]:
        card_type = '皇帝'
        rank_value = 999
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]
    elif player_card == [('红桃', 'Q'), ('方片', 'Q')] or player_card == [('方片', 'Q'), ('红桃', 'Q')]:
        card_type = '天对'
        rank_value = 998
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]          
    elif player_card == [('红桃', '2'), ('方片', '2')]:
        card_type = '地对'
        rank_value = 997
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]         
    elif player_card == [('红桃', '8'), ('方片', '8')]:
        card_type = '对红8'
        rank_value = 996
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]          
    elif player_card == [('红桃', '4'), ('方片', '4')]:
        card_type = '对红4'
        rank_value = 995
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value] 
    elif player_card == [('黑桃', '4'), ('梅花', '4')] or player_card == [('黑桃', '10'), ('梅花', '10')] or player_card == [('黑桃', '6'), ('梅花', '6')]:
        card_type = '对黑4'
        rank_value = 994
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]             
    elif player_card == [('红桃', '6'), ('方片', '6')] or player_card == [('红桃', '10'), ('方片', '10')] or player_card == [('红桃', '7'), ('方片', '7')] or player_card == [('红桃', 'J'), ('方片', 'J')]:
        card_type = '对红6'
        rank_value = 993
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]        
    elif player_card == [('红桃', '9'), ('方片', '9')] or player_card == [('红桃', '5'), ('方片', '5')] or player_card == [('黑桃', '7'), ('梅花', '7')] or player_card == [('黑桃', '8'), ('梅花', '8')]:
        card_type = '对红9'
        rank_value = 992
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value] 
    elif player_card == [('红桃', 'Q'), ('红桃', '9')] or player_card == [('红桃', 'Q'), ('方片', '9')] or player_card == [('方片', 'Q'), ('红桃', '9')] or player_card == [('方片', 'Q'), ('方片', '9')]:
        card_type = '天九牌'
        rank_value = 991
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]                                         
    elif player_card == [('红桃', 'Q'), ('红桃', '8')] or player_card == [('红桃', 'Q'), ('方片', '8')] or player_card == [('方片', 'Q'), ('红桃', '8')] or player_card == [('方片', 'Q'), ('方片', '8')] or player_card == [('红桃', 'Q'), ('黑桃', '8')] or player_card == [('红桃', 'Q'), ('梅花', '8')] or player_card == [('方片', 'Q'), ('黑桃', '8')] or player_card == [('方片', 'Q'), ('梅花', '8')]:
        card_type = '天八牌'
        rank_value = 990
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]         
    elif player_card == [('红桃', '2'), ('红桃', '8')] or player_card == [('红桃', '2'), ('方片', '8')] or player_card == [('方片', '2'), ('红桃', '8')] or player_card == [('方片', '2'), ('方片', '8')] or player_card == [('红桃', '2'), ('黑桃', '8')] or player_card == [('红桃', '2'), ('梅花', '8')] or player_card == [('方片', '2'), ('黑桃', '8')] or player_card == [('方片', '2'), ('梅花', '8')]:
        card_type = '地八牌'
        rank_value = 989
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]                                                         
    else:
        card_type = '杂牌算点数'
        rank_value = get_rank_value(player_card)
        logger.info("牌型%s, 排位点数为为%s", card_type, rank_value)
        return player_card + [card_type] + [rank_value]          


# 针对杂牌，计算两张牌的和
def get_rank_value(player_card):
    card1 = (player_card[0])[1]
    card2 = (player_card[1])[1]
    if card1 == '大王':
        card1_num = 6
    elif card1 == 'Q': 
        card1_num = 2
    elif card1 == 'J': 
        card1_num = 1   
    elif card1 == '10': 
        card1_num = 0 
    else :
        card1_num = int((player_card[0])[1]) 
              
    if card2 == '大王':
        card2_num = 6
    elif card2 == 'Q': 
        card2_num = 2
    elif card2 == 'J': 
        card2_num = 1   
    elif card2 == '10': 
        card2_num = 0   
    else :
        card2_num = int((player_card[1])[1])
         
    rank_value = card1_num + card2_num
    if rank_value >= 10:
        return rank_value - 10
    else:
        return rank_value


if __name__ == '__main__':
    player_card = [('黑桃', '3'), ('正司令', '大王')]
    print(judging_card(player_card))          
