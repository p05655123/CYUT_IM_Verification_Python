# 給一個偶數n，請你將n 分解成兩個質數的和，也就是說，這兩個質數
# 相加的和必須等於n。輸入說明：輸入一個數字，數字的範圍為[4, 10000]
# 間的偶數。輸出說明：對輸入的每筆測試資料，分別輸出 2 個質數，用一
# 個空白做為區隔，請由小到大排列(以第一個找到的符合的答案為主)。

def is_prime(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
    

n = int(input('請輸入一個範圍為4-10000之間的數字:'))
for i in range(1,n):
    if is_prime(i):
        if is_prime(n-i):
            print(i,n-i)
            break

