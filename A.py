from n_of_a_kind import is_noak
from straight import is_straight
from flush import is_flush
from straight_flush import is_straight_flush


def max_card_type(card):
    # card_type = {
    #     'High card':0,
    #     'Pair':1,
    #     'Two pairs':2,
    #     'Three of a kind':3,
    #     'Straight':4,
    #     'Flush':5,
    #     'Full house':6,
    #     'Four of a kind':7,
    #     'Straight flush':8,
    #     'Royal flush':9
    # }

    res = []

    x = is_noak(card)
    #print('is_noak',x)
    res.append(x)

    x = is_straight(card)
    #print('is_straight',x[0])
    res.append(x[0])

    x = is_flush(card)
    #print('is_flush',x)
    res.append(x)

    x = is_straight_flush(card)
    #print('is_straight_flush', x)
    res.append(x)


    #print(res)

    if res == [[], [], []]:
        res = [0]
    #print(res)

    #print('牌型最大值: ', max(res))

    return max(res)


card = [[['♦', '9']], [['♥', '10']], [['♠', '10']], [['♠', '9']], [['♦', 'A']]] #[[['♥', '10']], [['♥', '11']], [['♥', '12']], [['♥', '13']], [['♥', 'A']]]

x = max_card_type(card)  #x ([4], [10, 11, 12, 13])

print(x)