# 已知兩個整數n和d，請你找出n這個值，會有多少個因數可以被d整除。
# 輸入說明：每筆測試資料包含兩個以空白隔開的數字n及d，其n ( 0 < n < 1000000 )，
# 而d ( 2 ≤ d < 1000 )。輸出說明：對於每筆測試資料，輸出n這個值，會有多少個因數
# 可以被d整除。(請上傳Divide.py)

n =int(input("n:"))
d =int(input("d:"))

a = 0
for i in range(1,n+1):
    if n % i == 0:
        if i % d == 0:
            a = a + 1

print(a)