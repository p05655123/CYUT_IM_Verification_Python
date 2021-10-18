# 請寫個程式輸入一整數 N(2<N<100)，並找出小於N的所有質數。所謂質數，
# 就是一個正整數，除了本身和 1 以外並沒有任何其他因子。例如 2，3，5，
# 7 是質數，而 4，6，8，9 則不是。(請上傳 Primer2.py)

N = int(input("輸入N:"))

for i in range(2,N):
    a = 0
    for j in range(2,i):
        if i % j == 0:
            a = a + 1
        
    if a == 0:
        print (i,end=" ")