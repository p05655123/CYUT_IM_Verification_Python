# 請試撰寫一程式，讓使用者傳入兩個整數(a,b)，然後將兩數相乘，乘積若
# 超過(含)100以上，則輸出百位以上的數字(忽略整數與十位的數字)，否則
# 輸出兩數乘積。(請上傳Product.py檔)

import math
a =int(input("請輸入一個值："))
b= int(input("請輸入一個值："))
c = a * b
if c >= 100:
    print(math.floor(c/100))
else:
    print(c)