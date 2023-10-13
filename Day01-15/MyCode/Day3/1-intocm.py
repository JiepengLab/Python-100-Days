value = float(input("输入数值："))
unit = input("输入单位：")
if unit == "in":
    print("%f in = %f cm"%(value, value*2.54))
elif unit == "cm":
    print("%f cm = %f in"%(value, value/2.54))
else:
    print("单位错误，请输入'in'或'cm'")
