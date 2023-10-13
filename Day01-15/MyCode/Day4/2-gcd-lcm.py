a = int(input("输入整数a = "))
b = int(input("输入整数b = "))

min = a
max = b
if (b < a):
    min = b
    max = a

for i in range(min,0,-1):
    if a % i == 0 and b % i == 0:
        print("最大公约数为%d"%i)
        print("最小公倍数为%d"%(a*b/i))
        break