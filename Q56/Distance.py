# 撰寫一個程式，輸入兩個點的座標：(x1,y1), (x2,y2)，計算此兩點的距離。
# (請上傳Distance.py檔)


x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))

x = (x1 - x2)**2
y = (y1 - y2)**2
d = (x + y)**0.5
print(d)