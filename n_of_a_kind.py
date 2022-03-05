def is_noak(l):
    #print(l[0][0][0])
    z = []
    res = []
    # pair/two pairs/Three/Four
    for i in range(5):
        z.append(l[i][0][1])

    countt = []

    for i in z:
        countt.append(z.count(i))
    #print(countt)

    if countt.count(2) == 2 and countt.count(3) != 3:
        res.append(1)#('Pair!')
        #print('Pair!')

    elif countt.count(2) == 4:
        res.append(2)#('Two pairs!')
        #print('Two pairs!')

    elif countt.count(3) == 3 and countt.count(2) != 2:
        res.append(3)#('Three of a kind!')
        #print('Three of a kind!')

    elif countt.count(3) == 3 and countt.count(2) == 2:
        res.append(6)#('Full house!')
        #print('Full house!')

    elif countt.count(4) == 4:
        res.append(7)#('Four of a kind!')
        #print('Four of a kind!')

    return res

# l = [[['♦', '3']], [['♥', '3']], [['♠', '3']], [['♠', 'A']], [['♦', 'A']]]
#
# r = noak(l)