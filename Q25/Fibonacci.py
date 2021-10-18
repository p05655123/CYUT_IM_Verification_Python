# Fibonacci數列f1,f2,….,fn ，f1 =1; f2 =1;當n>2時，fn = fn-1+fn-2 ;設計一程式輸入
# 一整數n(1<n<100)，找出fn 。(請上傳 Fibonacci.py)

n = int(input("輸入n:"))
f=[1,1]
for i in range(2,n):
    f.append(f[i-1] + f[i-2])

print(f[n-1])