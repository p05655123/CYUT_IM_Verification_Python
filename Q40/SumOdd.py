# 請撰寫java程式執行從1 到n的迴圈，計算奇數的總和。
# （請上傳SumOdd.py）

n = int(input("輸入n:"))
a = 0
for i in range(1,n+1):
    if (i % 2 != 0):
        a = a + i
        
print(a)