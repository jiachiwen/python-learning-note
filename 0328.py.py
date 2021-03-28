'擲骰子遊戲 按下任意鍵再按ENTER骰子會擲出1-3的數字，數字代表連續輸入的次數，直到按出s再按下ENTER會贏的遊戲'

import random as r

A=str(input())

while True:
    if A=="s":
        print("you win")
        break
    else:
        print(r.randint(1,3))
        x=r.randint(1,3)
        breakpoint() #煥銘教的debug mudule
        for i in range(0,x): #試著寫出連續輸入
            print("tall") #test 上一行運作狀態
            break
