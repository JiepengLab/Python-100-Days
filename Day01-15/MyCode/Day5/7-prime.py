from math import sqrt

for i in range(2, 101):
    f = 1
    for j in range(2, int(sqrt(i))+1):
        if i != 2 and i % j == 0:
            f = 0
    if f == 1:
        print(i, end=' ')
