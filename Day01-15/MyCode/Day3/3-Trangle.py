import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a+b > c and a+c >b and b+c>a:
    print("周长为%f"%(a+b+c))
    p = (a+b+c)/2
    print("面积为%f"%math.sqrt(p*(p-a)*(p-b)*(p-c)))
else:
    print("不能构成三角形")
