# 試利用迴圈撰寫出一程式可計算出 n! 的值。
# (請上傳Factorial.py檔) 

n = int(input("輸入n :"))
a = 1
for i in range(1,n+1):
    a = a * i
print(a)
