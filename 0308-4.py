#圓面積 圓周長
#同時輸出
def my_circle(m):
    area=m**2*3.14
    length=m*2*3.14
    return area,length

m=int(input())
print(my_circle(m))
print(type(my_circle(m)))