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

is_prime(113)