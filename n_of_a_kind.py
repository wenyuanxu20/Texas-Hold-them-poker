def noak(l):

    #print(l[0][0][0])

    z = []
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

    if countt.count(2) == 2:
        print('Pair!')

    elif countt.count(2) == 4:
        print('Two pairs!')

    elif countt.count(3) == 3:
        print('Three of a kind!')

    elif countt.count(4) == 4:
        print('Four of a kind!')


l = [[['♦', '7']], [['♥', '2']], [['♠', '3']], [['♠', 'A']], [['♦', 'A']]]

r = noak(l)