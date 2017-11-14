i = 1
j = 1
k = 0
q = 0
print("Month 0: 1 pair(s) of rabbit")
while(k < 10):
    while(q < 4):
        q += 1
        print("Month {0}: {1} pair(s) of rabbit".format(q, i+j))
        k = i + j
        i = j
        j = k
    break
