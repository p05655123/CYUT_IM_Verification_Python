# 請建立 Java程式，讀入一個整數n，並使用迴圈計算下列數學運算式的值： 
# 1*1+2*2+3*3~+n*n 。 ( 請上傳 Series.py 檔 )

n = int(input("輸入n:"))
s= 1
for i in range(1,n+1):
    s = s +(i * i)
print(s-1)