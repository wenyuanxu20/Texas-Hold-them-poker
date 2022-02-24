# coding = utf-8
# 52张牌
# 4个花色 黑桃（Spade），红桃（Heart），方块（Diamond），梅花（Club）
# git: https://github.com/xwy964046872/poker
# home test
# Card type：
# High card: 5张牌没有一样的，也组不成顺子
# Pair：有一个对子，A最大，2最小
# Two pairs：有两对
# Three of a kind: 有三张一样的
# Straight: 顺子 （7 8 9 10 J） 花色不同，A可以当最大的，也可以当最小的
# Flush：同花，五张牌花色相同即可
# Full house：葫芦，三条带一对
# Four of a kind: 四条/金刚，4张一样的牌
# Straight flush: 同花顺，顺子+同花色
# Royal flush: 皇家同花顺，10-A的同花顺，三万分之一



import random
import copy

#花色大小
type = {'Spade':4, 'Heart':3, 'Diamond':2, 'Club':1}


# 创建玩家
def gen_player(n):
    player = []
    for i in range(n):
        player.append([])
    print('player',player)
    return player

player = gen_player(5)


def ini_game():

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
    for k in range(len(player)):
        ak = random.choice(cards)
        player[k].append(ak)
        cards.remove(ak)

    print('玩家手牌为',player)

game = ini_game()


# Con=input("输入指令")
# while Con!="END":
#     if (Con=="弃牌"):
#         break
#     if (Con=="加注"):
#         break
#     else:
#         print('请输入”弃牌“或”加注“或”跟注“')
#         Con = input("输入指令")
#         continue
#
# #第一轮发牌
# for n in range(3):
#     print(desk[n])
# Con=input("输入指令")
# while Con!="END":
#     if (Con=="弃牌"):
#         break
#     if (Con=="加注"):
#         break
#     else:
#         print('请输入”弃牌“或”加注“或”跟注“')
#         Con = input("输入指令")
#         continue
# #第二轮发牌
# for n in range(4,5):
#     print(desk[n])
# Con=input("输入指令")
# while Con!="END":
#     if (Con=="弃牌"):
#         break
#     if (Con=="加注"):
#         break
#     else:
#         print('请输入”弃牌“或”加注“或”跟注“')
#         Con = input("输入指令")
#         continue
# #第三轮发牌
# print(desk[4])