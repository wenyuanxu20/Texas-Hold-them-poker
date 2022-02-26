l = [[['♦', 'A']], [['♥', '10']], [['♠', '11']], [['♠', '12']], [['♦', '13']]]


def is_straight(l):
    global p
    z = []
    res = []
    # pair/two pairs/Three/Four
    for i in range(5):
        z.append(l[i][0][1])

    #print('牌面数值：', z)



    p = []

    for c in z:
        if c != 'A':
            #z.remove(c)
            c = int(c)
            p.append(c)

    p.sort()


    #print('排序后的牌面数值：',p)
    flush_card = []


    for i in range(len(p) - 1):
        if p[i] + 1 == p[i + 1]:
            flush_card.append(1)

    if not 'A' in z:
        if sum(flush_card) == 4:
            res.append('Straight!')
            #print('Straight!')

    elif sum(flush_card) == 3 and p[0] == 2:
            res.append('Straight!')
            #print('Straight!')

    else:
        if sum(flush_card) == 3 and p[3] == 13:
            res.append('Straight!')
            #print('Straight!')

    return res,p