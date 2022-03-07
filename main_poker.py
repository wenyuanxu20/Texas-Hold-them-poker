# coding = utf-8
# git: https://github.com/xwy964046872/poker


import random
import copy
from n_of_a_kind import is_noak

# class Texas():
#     def __init__(self):
#         desk = []  # 存储桌上3,4,5张牌


# 花色大小
type = {'Spade': 4, 'Heart': 3, 'Diamond': 2, 'Club': 1}


# 创建玩家
def gen_player():
    player = []
    n = int(input('Player number: '))  # 输入玩家人数
    for i in range(n):
        player.append([])
    return player


# player = gen_player(5)


def ini_game():
    desk = []  # 存储桌上3,4,5张牌
    pokers = []
    for i in ['♥', '♠', '♦', '♣']:
        for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
            pokers.append([i] + [j])
    # print('新牌：', pokers)

    cards = copy.deepcopy(pokers)  # 生成新的一副牌用来洗牌
    random.shuffle(cards)
    # print('洗牌后：', cards)

    #flop card round 1
    for n in range(3):
        community_card = random.choice(cards)
        desk.append(community_card)
        cards.remove(community_card)
    print('桌面发n张牌：', desk)

    # 玩家发牌,每人发两张手牌 dealing
    for k in range(len(player)):
        for hand_card in range(2):
            player_hand_card = random.choice(cards)
            player[k].append(player_hand_card)
            cards.remove(player_hand_card)

    print('玩家手牌为', player)


# game = ini_game(player = gen_player(5))



if __name__ == "__main__":
    player = gen_player()
    print('Players: ', player)
    ini_game()

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
