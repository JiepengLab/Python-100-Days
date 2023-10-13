while {1}:
    roll = int(input(""))
    if roll == 7 or roll == 11:
        print("Player win!")
        break
    if roll == 2 or roll == 3 or roll == 12:
        print("Zhuang win!")
        break
    print("Continue")