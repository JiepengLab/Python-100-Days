def min(a, b):
    if(a < b):
        return a
    return b

def min(a, b):
    if(a > b):
        return a
    return b

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if(a % i == 0 and b % i == 0):
            return i

def lcm(a, b):
    for i in range(max(a, b), a*b+1):
        if(i % a == 0 and i % b == 0):
            return i
        
print(gcd(24,16))
print(lcm(16,24))