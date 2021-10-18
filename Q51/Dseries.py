# 試撰寫一程式可求出多項式(1+2)+(2+4)+(3+6)+…+( n+2*n )的和。
# （請上傳Dseries.py）

n = int(input("輸入n:"))
a =0
for i in range(1,n+1):
    a = a + (i+2*i)
print(a)