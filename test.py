import itertools
from A import max_card_type


l = [1, 2, 3, 4, 5, 6]
card = [[['♦', '9']], [['♥', '10']], [['♠', '10']], [['♠', '9']], [['♦', 'A']], [['♦', '10']],[['♦', '4']]]

# for i in itertools.combinations('BCDEF', 2):
#     print(''.join(i),end=" ")
# 输出 BC BD BE BF CD CE CF DE DF EF

list1 = [1, 3, 4, 5]
list2 = list(itertools.combinations(card, 5))
#print(list2)

res = []

for i in list2:
    i = list(i)
    #print(i)
    res.append(max_card_type(i))

print(max(res))

