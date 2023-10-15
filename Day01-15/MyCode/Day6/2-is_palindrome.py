
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

is_palindrome(0)
