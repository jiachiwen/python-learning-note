#圓面積計算&圓周常計算

#有兩種結果，要判別顯示哪一種的
#使用布林值

#當前設定is_circle==true 要輸出園面積
def my_circle(m, is_circle=True):
    if is_circle==True:
        return m*2*3.14
    else:
        return m**2*3.14

m=int(input())
print(my_circle(m, is_circle=False))