rows = int (input("行数为："))

for i in range(1,rows+1):
    print("*"*i)

for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*i)

for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*(2*i-1))