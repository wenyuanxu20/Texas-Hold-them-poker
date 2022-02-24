
l = [[['♦', '2']], [['♥', '2']], [['♠', '4']], [['♠', '4']], [['♦', 'A']]]

#print(l[0][0][0])

z = []
# high card
for i in range(5):


    z.append(l[i][0][1])

print(z)

p = []

for c in z:
    if c != 'A' and c != 'J' and c != 'Q' and c != 'K':
        #z.remove(c)
        c = int(c)
        p.append(c)

p.sort()

countt = []
for i in z:

    countt.append(p.count(i))


print(countt)

if countt.count(2) == 2:
    print('pair')

elif countt.count(2) == 4:
    print('two pairs')
