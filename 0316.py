'英文字母戳戳樂'
'rule: 請輸入任意小寫英文字母，每次輸入的字母皆不同且不可重複'
'輸入後會出現一個任意數字(1-3)之間，假若出現2請再輸入2次英文小寫字母'
'直到輸入特定字母即戰敗'

import random as r

while True:
    A=str(input())

    if A!="s":
        print(r.randint(1,3))
        continue
    else:
        break
print("game over")
    
    