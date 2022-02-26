from n_of_a_kind import is_noak
from straight import is_straight
from flush import is_flush
from straight_flush import is_straight_flush



card = [[['♥', '1']], [['♥', '1']], [['♥', '2']], [['♥', '2']], [['♥', '11']]]
res = []

x = is_noak(card)
print('is_noak',x)
res.append(x)

x = is_straight(card)
print('is_straight',x[0])
res.append(x[0])

x = is_flush(card)
print('is_flush',x)
res.append(x)




print(res)

if res == [[], [], []]:
    res = ['High card!']
print(res)