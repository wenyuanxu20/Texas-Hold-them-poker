l = [[['♦', 'A']], [['♦', '10']], [['♦', '11']], [['♦', '12']], [['♦', '13']]]


def is_flush(l):

    z = []
    res = []

    for i in range(5):
        z.append(l[i][0][0])

    #print(z)

    flush_count = []

    for i in z:
        flush_count.append(z.count(i))

    #print(flush_count)

    if flush_count.count(5) == 5:
        res.append(5) #('Flush!')
        #print('Flush!')

    return res