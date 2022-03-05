from straight import is_straight
from flush import is_flush
import copy



def is_straight_flush(l):
    l1 = copy.deepcopy(l)
    res = []
    x = is_straight(l)
    print('x',x)
    if x[0] != []:
        if x[0][0] == 4:  #x ([4], [10, 11, 12, 13])
            y = is_flush(l1)
            #print('y', y)
            if y[0] == 5:
                res.append(8) #('Straight flush!')
    # else:
    #     pass

    #print(res)
    if x[0] != []:
        if res[0] == 8:
            if x[1][0] == 10:
                res[0] = 9 #('Royalflush!')


    return res


l  = [[['♦', 'A']], [['♦', '10']], [['♦', '11']], [['♦', '12']], [['♦', '13']]] #[[['♦', '9']], [['♥', '10']], [['♠', '10']], [['♠', '9']], [['♦', 'A']]]#

test = is_straight_flush(l)

print(test)
