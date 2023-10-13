for i in range(100, 1000):
    x1 = i // 100
    x2 = (i - x1*100)//10
    x3 = i % 10
    if i == x1*x1*x1 + x2*x2*x2 + x3*x3*x3:
        print(i)
