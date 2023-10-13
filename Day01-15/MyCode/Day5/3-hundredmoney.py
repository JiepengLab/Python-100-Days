for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, 101, 3):
            if 5*i+3*j+k//3 == 100 and i+j+k == 100:
                print("%d, %d, %d" % (i, j, k))
