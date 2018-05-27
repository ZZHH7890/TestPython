
'''
Created on 2018年5月27日/下午7:07:20

@author: joker.zhang
'''

player_card = [('方块', '2'), ('梅花', '8')]
if player_card == [('方块', 'Q'), ('方块', '8')] or [('红桃', 'Q'), ('黑桃', '8')] or player_card == [('红桃', 'Q'), ('梅花', '8')] or player_card == [('方块', 'Q'), ('黑桃', '8')] or player_card == [('方块', 'Q'), ('梅花', '8')]:
    print(True)
else:
    print(False)    