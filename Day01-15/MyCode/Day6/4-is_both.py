import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)+1)):
        if(num % i == 0):
            return False
    return True

def is_palindrome(num):
    reverse = 0
    num_origin = num
    while(num!=0):
        x = num % 10
        reverse = reverse*10+x
        num//= 10
    if reverse == num_origin:
        return True
    else:
        return False

num = int(input("正整数："))

if is_palindrome(num) and is_prime(num):
    print("YES")