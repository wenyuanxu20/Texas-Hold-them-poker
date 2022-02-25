def noak(l):

    #print(l[0][0][0])

    z = []
    res = []
    # pair/two pairs/Three/Four
    for i in range(5):


        z.append(l[i][0][1])

    print('牌面数值：',z)

    # p = []
    #
    # for c in z:
    #     if c != 'A':
    #         #z.remove(c)
    #         c = int(c)
    #         p.append(c)
    #
    # p.sort()
    #
    # print('排序后的牌面数值：',p)

    countt = []

    for i in z:

        countt.append(z.count(i))


    print(countt)

    if countt.count(2) == 2 and countt.count(3) != 3:
        res.append('Pair!')
        print('Pair!')

    elif countt.count(2) == 4:
        res.append('Two pairs!')
        print('Two pairs!')

    elif countt.count(3) == 3 and countt.count(2) != 2:
        res.append('Three of a kind!')
        print('Three of a kind!')

    elif countt.count(3) == 3 and countt.count(2) == 2:
        res.append('Full house!')
        print('Full house!')

    elif countt.count(4) == 4:
        res.append('Four of a kind!')
        print('Four of a kind!')

    return res


l = [[['♦', '3']], [['♥', '3']], [['♠', '3']], [['♠', 'A']], [['♦', 'A']]]

r = noak(l)