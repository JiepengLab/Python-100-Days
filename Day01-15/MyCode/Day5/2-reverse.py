x = int(input("请输入正整数x = "))
result = 0

while (x > 0):
    result = x % 10+result*10
    x = x // 10
print(result)
