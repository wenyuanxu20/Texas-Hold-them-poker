# coding = utf-8
# 52张牌
# 4个花色 黑桃（Spade），红桃（Heart），方块（Diamond），梅花（Club）
# git: https://github.com/xwy964046872/poker

import random
import copy

#花色大小
type = {'Spade':4, 'Heart':3, 'Diamond':2, 'Club':1}


# 创建玩家
def gen_player(n):

    n = 1
    player = []



    print('player',player)

    return player



desk = []  # 存储桌上5张牌

pokers=[]
for i in ['♥','♠','♦','♣']:
    for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        pokers.append([i]+[j])

print('新牌：', pokers)

cards = copy.deepcopy(pokers) #生成新的一副牌用来洗牌

random.shuffle(cards)

print('洗牌后：', cards)

#print(pokers)

for n in range(5):
    ak=random.choice(cards)
    desk.append(ak)
    cards.remove(ak)

#print('桌面发5张牌：', desk)

#玩家发牌
for k in range(2):
    ak=random.choice(cards)
    player.append(ak)
    cards.remove(ak)

print('玩家手牌为',player)
Con=input("输入指令")
while Con!="END":
    if (Con=="弃牌"):
        break
    if (Con=="加注"):
        break
    else:
        print('请输入”弃牌“或”加注“或”跟注“')
        Con = input("输入指令")
        continue

#第一轮发牌
for n in range(3):
    print(desk[n])
Con=input("输入指令")
while Con!="END":
    if (Con=="弃牌"):
        break
    if (Con=="加注"):
        break
    else:
        print('请输入”弃牌“或”加注“或”跟注“')
        Con = input("输入指令")
        continue
#第二轮发牌
for n in range(4,5):
    print(desk[n])
Con=input("输入指令")
while Con!="END":
    if (Con=="弃牌"):
        break
    if (Con=="加注"):
        break
    else:
        print('请输入”弃牌“或”加注“或”跟注“')
        Con = input("输入指令")
        continue
#第三轮发牌
print(desk[4])