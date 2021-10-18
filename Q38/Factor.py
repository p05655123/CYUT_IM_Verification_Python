# 試撰寫一程式可由鍵盤輸入一個正整數N, 然後求其所有的因數。
# (請上傳Factor.py檔) 

N = int(input("輸入N:"))

for i in range(1,N+1):
    if (N % i == 0):
        print(i,end=" ")