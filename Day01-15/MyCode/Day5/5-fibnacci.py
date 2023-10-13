n = int(input(""))

x1 = 1
x2 = 1

if n > 2:
    for i in range(n):
        if(i == 0 or i == 1):
            print(1)
        else:
            x1, x2 = x2, x1+x2
            print(x2)
elif n == 1:
    print(1)
elif n == 2:
    print(1)
    print(1)