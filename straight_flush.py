from straight import is_straight
from flush import is_flush
import copy



def is_straight_flush(l):
    l1 = copy.deepcopy(l)
    res = []
    x = is_straight(l)
    #print('x',x)
    if x[0][0] == 'Straight!':
        y = is_flush(l1)
        #print('y', y)
        if y[0] == 'Flush!':
            res.append('Straight flush!')

    if res[0] == 'Straight flush!':
        if x[1][0] == 10:
            res.append('Royalflush!')


    return res


# l  = [[['♦', 'A']], [['♦', '10']], [['♦', '11']], [['♦', '12']], [['♦', '13']]]
#
# test = is_straight_flush(l)
#
# print(test)
