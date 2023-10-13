import math

num = int(input("请输入要检测的数："))

f = 1

if (num < 2): 
    f = 0
else :    
    for i in range(2,int(math.sqrt(num)+1)):
        if (num % i == 0):
            f = 0
            break

if (f):
    print("是素数！")
else :
    print("不是素数！")
